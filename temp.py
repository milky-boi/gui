# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd 

df_1 = pd.read_excel('individual_result_table_1.xlsx', index_col=0 )
df_2 = pd.read_excel('individual_result_table_2.xlsx', index_col=0 )
df_3 = pd.read_excel('individual_result_table_2.xlsx', index_col=0 )

bsl_vs_first_exp_1 = df_1['BSLvs1st'].value_counts()
bsl_vs_first_exp_2 = df_2['BSLvs1st'].value_counts()
bsl_vs_first_exp_3 = df_3['BSLvs1st'].value_counts()

values_bsl_vs_first = [bsl_vs_first_exp_1, bsl_vs_first_exp_2, bsl_vs_first_exp_3]
result_bsl_vs_first = pd.DataFrame(values_bsl_vs_first)
result_bsl_vs_first = result_bsl_vs_first.reset_index(drop=True)
result_bsl_vs_first['Number of flies'] = result_bsl_vs_first.iloc[:,:].sum(axis=1)   

result_bsl_vs_first['Decrease'] = result_bsl_vs_first['D'].div(result_bsl_vs_first['Number of flies'])
result_bsl_vs_first['Decrease'] = result_bsl_vs_first['Decrease']*100
result_bsl_vs_first['Same'] = result_bsl_vs_first['S'].div(result_bsl_vs_first['Number of flies'])
result_bsl_vs_first['Same'] = result_bsl_vs_first['Same']*100
result_bsl_vs_first['Increase'] = result_bsl_vs_first['I'].div(result_bsl_vs_first['Number of flies'])
result_bsl_vs_first['Increase'] = result_bsl_vs_first['Increase']*100

#.fillna(0)
first_second_exp_1 = df_1['1stvs2nd'].value_counts()
first_second_exp_2 = df_2['1stvs2nd'].value_counts()
first_second_exp_3 = df_3['1stvs2nd'].value_counts()

values_first_second = [first_second_exp_1, first_second_exp_2, first_second_exp_3]
result_first_second = pd.DataFrame(values_first_second)
result_first_second = result_first_second.reset_index(drop=True)
result_first_second['Number of flies'] = result_first_second.iloc[:,:].sum(axis=1)   

result_first_second['Decrease'] = result_first_second['D'].div(result_first_second['Number of flies'])
result_first_second['Decrease'] = result_first_second['Decrease']*100
result_first_second['Same'] = result_first_second['S'].div(result_first_second['Number of flies'])
result_first_second['Same'] = result_first_second['Same']*100
result_first_second['Increase'] = result_first_second['I'].div(result_first_second['Number of flies'])
result_first_second['Increase'] = result_first_second['Increase']*100


bsl_first_second_exp_1 = df_1['BSLvs1stvs2nd'].value_counts()
bsl_first_second_exp_2 = df_2['BSLvs1stvs2nd'].value_counts()
bsl_first_second_exp_3 = df_3['BSLvs1stvs2nd'].value_counts()

values_bsl_first_second = [bsl_first_second_exp_1,
                           bsl_first_second_exp_2,
                           bsl_first_second_exp_3]

#, columns=['False', 'B']
result_bsl_first_second = pd.DataFrame(values_bsl_first_second)

result_bsl_first_second = result_bsl_first_second.reset_index(drop=True)
result_bsl_first_second['Number of flies'] = result_bsl_first_second.iloc[:,:].sum(axis=1)  

result_bsl_first_second['Senistized'] = result_bsl_first_second['B'].div(result_bsl_first_second['Number of flies'])
result_bsl_first_second['Senistized'] = result_bsl_first_second['Senistized']*100
result_bsl_first_second['NS'] = result_bsl_first_second['False'].div(result_bsl_first_second['Number of flies'])
result_bsl_first_second['NS'] = result_bsl_first_second['NS']*100

result_bsl_vs_first.to_excel('result_bsl_vs_first.xlsx')
result_first_second.to_excel('result_first_second.xlsx')
result_bsl_first_second.to_excel("result_bsl_first_second.xlsx")

"""
same = df_1['BSLvs1stvs2nd'].value_counts()
"""