import pandas as pd 
from datetime import datetime, timedelta

from GraphPage import GraphPage_

class DataEdit_:
      
    def select_cols_rows(self, start_col, end_col, start_row, end_row):
        """
        :rtype: object
        :param start_col:
        :param end_col:
        :param start_row:
        :param end_row:
        """


        start_col = int(start_col)
        end_col = int(end_col)

        df_info = self.controller.df.iloc[:, :4]
        
        #ovdje cemo pozvati funkciju clear_data() koja ce dio tablice procistiti 
        df_data = self.controller.df.iloc[:, 4:]
        header = []
        len_df = len(df_data.columns)+1
        for i in range(1,len_df):
            header.append(i) 
        df_data.columns = header
        #print(df_info)
        #odabiremo jedinke koje smo unjeli u entryu
        df_data = df_data.loc[:, int(start_col):int(end_col)]

        #postavljamo redne vrojeve od 1 na dalje
        header = []
        len_df = len(df_data.columns)+1
        for i in range(1,len_df):
            header.append(i) 
        df_data.columns = header
        
        #spajamo sve u jedan dat frame 
        df = pd.concat([df_info, df_data], axis=1, sort=False)
        
        #ovdje vrsimo selekciju redaka
        start_time = datetime.strptime(start_row, '%Y-%m-%d %H:%M')
        end_time = datetime.strptime(end_row, '%Y-%m-%d %H:%M')

        df['datetime'] = pd.to_datetime(df['datetime'])

        self.controller.df = df.loc[df['datetime'].dt.time.between(start_time.time(), end_time.time())]
        self.controller.df = self.controller.df.reset_index(drop=True)
        #vrijednosti se brisu zbog druge selekcije nad podatcima
        start_row=None
        end_row=None
        
    def clear_data(self):
        """
        ova funkcija brise nepotrebne stupce koji nisu jedinke i kreira
        stupac time koji je u formatu dd-mm-yyyy hh:mm:ssss imati na umu 
        da se nakon time stupca dodaju 3 nova stupca gdje se racunaju vrijednosti

        :rtype: object
        """
        df = self.controller.df
        
        header = []
        header.append('broj')
        header.append('date')
        header.append('time')
        
        len_df = len(df.columns)-2
        for i in range(1,len_df):
            header.append(i)  
        
        df.columns = header

        df_info = df.iloc[:, :3]
        df_data = df.iloc[:, 3:]
        
        df_info['datetime'] = df.date + ' ' + df.time
        df_info = pd.to_datetime(df_info.stack()).unstack()
        
        
        df_info['mean'] = None 
        df_info['std'] = None
        df_info['sum'] = None
        df_info = df_info.drop(columns=['broj', 'date', 'time'])
        
        self.controller.df = pd.concat([df_info, df_data], axis=1, sort=False)
        
    def get_stats(self):
        """"
        ovdje se izracunavaju statisticke vrijednosti koje se pohranjhuju u 
        stupce tablice a to su: average, sum i stdev

        :rtype: object
        """
        df = self.controller.df.copy()
        
        df['mean'] = df.iloc[:,7:].mean(axis=1) 
        df['std'] = df.iloc[:,7:].std(axis=1) 
        df['sum'] = df.iloc[:,7:].sum(axis=1)     
        return df
    
    def save_to_xlsx(df):
        df.to_excel("results/selected_data.xlsx")

    def save_to_txt(df):
        df.to_csv('results/selcted_data.txt', header=True, index=False, sep='\t', float_format='%.3f')

    def save_result_to_xlsx(df):
        df.to_excel("results/individual_result_table.xlsx")

    def save_result_to_txt(df):
        df.to_csv('results/individual_result_table.txt', header=True, index=False, sep='\t', float_format='%.3f')


    def select_col(df, start):
        start_time = datetime.strptime(start, '%H:%M')
        end_time = start_time + timedelta(minutes=30)

        df['datetime'] = pd.to_datetime(df['datetime'])
        df = df.loc[df['datetime'].dt.time.between(start_time.time(), end_time.time())]

        df = df.reset_index(drop=True)

        return df



    def split_for_graph(self, start_bsl_morning, start_1st_expo, start_bsl_noon, start_2nd_expo):
        """
        odabrane vrijednosti razdvajaju data frame na 4 manja framea
        """
        global df_1
        global df_2
        global df_3
        global df_4
        # print(start_1st_expo)

        df = self.controller.df.copy()
        df_1 = DataEdit_.select_col(df, start_bsl_morning)
        df_2 = DataEdit_.select_col(df, start_1st_expo)
        df_3 = DataEdit_.select_col(df, start_bsl_noon)
        df_4 = DataEdit_.select_col(df, start_2nd_expo)

        self.controller.df_1 = df_1
        self.controller.df_2 = df_2
        self.controller.df_3 = df_3
        self.controller.df_4 = df_4

        df_1_t = df_1.transpose()
        df_1_t = df_1_t.drop(df_1_t.index[0:4])
        df_1_t = df_1_t.reset_index(drop=True)
        df_1_t = df_1_t.iloc[:, 0:5]
        df_1_t['BSL_morning'] = df_1_t.mean(axis=1)
        df_1_t = df_1_t['BSL_morning']

        df_2_t = df_2.transpose()
        df_2_t = df_2_t.drop(df_2_t.index[0:4])
        df_2_t = df_2_t.reset_index(drop=True)
        df_2_t = df_2_t.iloc[:, 0:5]
        df_2_t['first_adm'] = df_2_t.mean(axis=1)
        df_2_t = df_2_t['first_adm']

        df_3_t = df_3.transpose()
        df_3_t = df_3_t.drop(df_3_t.index[0:4])
        df_3_t = df_3_t.reset_index(drop=True)
        df_3_t = df_3_t.iloc[:, 0:5]
        df_3_t['BSL_noon'] = df_3_t.mean(axis=1)
        df_3_t = df_3_t['BSL_noon']

        df_4_t = df_4.transpose()
        df_4_t = df_4_t.drop(df_4_t.index[0:4])
        df_4_t = df_4_t.reset_index(drop=True)
        df_4_t = df_4_t.iloc[:, 0:5]
        df_4_t['second_adm'] = df_4_t.mean(axis=1)
        df_4_t = df_4_t['second_adm']

        frames = [df_1_t, df_2_t, df_4_t]

        result = pd.concat(frames, axis=1)

        result['BSLvs1st'] = 'S'
        result['BSLvs1st'] = result['BSLvs1st'].where(result['BSL_morning'] <= result['first_adm'], 'D')
        result['BSLvs1st'] = result['BSLvs1st'].where(result['BSL_morning'] >= result['first_adm'], 'I')

        result['1stvs2nd'] = 'S'
        result['1stvs2nd'] = result['1stvs2nd'].where(result['first_adm'] <= result['second_adm'], 'D')
        result['1stvs2nd'] = result['1stvs2nd'].where(result['first_adm'] >= result['second_adm'], 'I')

        result['BSLvs1stvs2nd'] = 'B'
        result['BSLvs1stvs2nd'] = result['BSLvs1stvs2nd'].where(
            (result['BSLvs1st'] == 'I') & (result['1stvs2nd'] == 'I'), 'False')

        self.controller.result = result

        df_ave = self.controller.df.copy()

        df_ave['datetime'] = pd.to_datetime(df_ave['datetime'])
        df_ave.index = df_ave['datetime']
        df_p = df_ave.resample('H').mean()

        df_p['Hour'] = df_ave['datetime'].dt.hour

        df_hour_ave = pd.DataFrame(df_p['mean'])

        self.controller.df_hour_ave = df_hour_ave

        #GraphPage_.plot_graph(self)

    def compare_experiments(self, df_1, df_2, df_3):
        """
        :param df_1:
        :param df_2:
        :param df_3:

        :rtype: object
        """
        df_1 = df_1
        df_2 = df_2
        df_3 = df_3

        bsl_vs_first_exp_1 = df_1['BSLvs1st'].value_counts()
        bsl_vs_first_exp_2 = df_2['BSLvs1st'].value_counts()
        bsl_vs_first_exp_3 = df_3['BSLvs1st'].value_counts()

        values_bsl_vs_first = [bsl_vs_first_exp_1, bsl_vs_first_exp_2, bsl_vs_first_exp_3]
        result_bsl_vs_first = pd.DataFrame(values_bsl_vs_first)
        result_bsl_vs_first = result_bsl_vs_first.reset_index(drop=True)
        result_bsl_vs_first['Number of flies'] = result_bsl_vs_first.iloc[:, :].sum(axis=1)

        result_bsl_vs_first['Decrease'] = result_bsl_vs_first['D'].div(result_bsl_vs_first['Number of flies'])
        result_bsl_vs_first['Decrease'] = result_bsl_vs_first['Decrease'] * 100
        result_bsl_vs_first['Same'] = result_bsl_vs_first['S'].div(result_bsl_vs_first['Number of flies'])
        result_bsl_vs_first['Same'] = result_bsl_vs_first['Same'] * 100
        result_bsl_vs_first['Increase'] = result_bsl_vs_first['I'].div(result_bsl_vs_first['Number of flies'])
        result_bsl_vs_first['Increase'] = result_bsl_vs_first['Increase'] * 100

        # .fillna(0)
        first_second_exp_1 = df_1['1stvs2nd'].value_counts()
        first_second_exp_2 = df_2['1stvs2nd'].value_counts()
        first_second_exp_3 = df_3['1stvs2nd'].value_counts()

        values_first_second = [first_second_exp_1, first_second_exp_2, first_second_exp_3]
        result_first_second = pd.DataFrame(values_first_second)
        result_first_second = result_first_second.reset_index(drop=True)
        result_first_second['Number of flies'] = result_first_second.iloc[:, :].sum(axis=1)

        result_first_second['Decrease'] = result_first_second['D'].div(result_first_second['Number of flies'])
        result_first_second['Decrease'] = result_first_second['Decrease'] * 100
        result_first_second['Same'] = result_first_second['S'].div(result_first_second['Number of flies'])
        result_first_second['Same'] = result_first_second['Same'] * 100
        result_first_second['Increase'] = result_first_second['I'].div(result_first_second['Number of flies'])
        result_first_second['Increase'] = result_first_second['Increase'] * 100

        bsl_first_second_exp_1 = df_1['BSLvs1stvs2nd'].value_counts()
        bsl_first_second_exp_2 = df_2['BSLvs1stvs2nd'].value_counts()
        bsl_first_second_exp_3 = df_3['BSLvs1stvs2nd'].value_counts()

        values_bsl_first_second = [bsl_first_second_exp_1,
                                   bsl_first_second_exp_2,
                                   bsl_first_second_exp_3]

        # , columns=['False', 'B']
        result_bsl_first_second = pd.DataFrame(values_bsl_first_second)

        result_bsl_first_second = result_bsl_first_second.reset_index(drop=True)
        result_bsl_first_second['Number of flies'] = result_bsl_first_second.iloc[:, :].sum(axis=1)

        result_bsl_first_second['Senistized'] = result_bsl_first_second['B'].div(
            result_bsl_first_second['Number of flies'])
        result_bsl_first_second['Senistized'] = result_bsl_first_second['Senistized'] * 100
        result_bsl_first_second['NS'] = result_bsl_first_second['False'].div(result_bsl_first_second['Number of flies'])
        result_bsl_first_second['NS'] = result_bsl_first_second['NS'] * 100

        ##############################

        ranges = [0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, 7, 9, 15]

        bsl_morning_1 = df_1.BSL_morning.groupby(pd.cut(df_1.BSL_morning, ranges)).count()
        first_exp_1 = df_1.first_adm.groupby(pd.cut(df_1.first_adm, ranges)).count()
        second_exp_1 = df_1.second_adm.groupby(pd.cut(df_1.second_adm, ranges)).count()

        frames_1 = [bsl_morning_1, first_exp_1, second_exp_1]
        result_1 = pd.concat(frames_1, axis=1)
        #result_1 = result_1.T

        bsl_morning_2 = df_2.BSL_morning.groupby(pd.cut(df_2.BSL_morning, ranges)).count()
        first_exp_2 = df_2.first_adm.groupby(pd.cut(df_2.first_adm, ranges)).count()
        second_exp_2 = df_2.second_adm.groupby(pd.cut(df_2.second_adm, ranges)).count()

        frames_2 = [bsl_morning_2, first_exp_2, second_exp_2]
        result_2 = pd.concat(frames_2, axis=1)
        #result_2 = result_2.T

        bsl_morning_3 = df_3.BSL_morning.groupby(pd.cut(df_3.BSL_morning, ranges)).count()
        first_exp_3 = df_3.first_adm.groupby(pd.cut(df_3.first_adm, ranges)).count()
        second_exp_3 = df_3.second_adm.groupby(pd.cut(df_3.second_adm, ranges)).count()

        frames_3 = [bsl_morning_3, first_exp_3, second_exp_3]
        result_3 = pd.concat(frames_3, axis=1)
        #result_3 = result_3.T

        main_frames = [result_1, result_2, result_3]
        sort_by_range_table = pd.concat(main_frames, axis=1)

        with pd.ExcelWriter('results/exp_compare.xlsx') as writer:
            result_bsl_vs_first.to_excel(writer, sheet_name='result_bsl_vs_first')
            result_first_second.to_excel(writer, sheet_name='result_first_second')
            result_bsl_first_second.to_excel(writer, sheet_name='result_bsl_first_second')
            sort_by_range_table.to_excel(writer, sheet_name='sort_by_range_table')


        self.controller.exp_comp_results = sort_by_range_table
        self.on_show_frame(self)
        pass

        
        
        
    
    