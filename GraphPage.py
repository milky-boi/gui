import tkinter as tk
from tkinter import ttk

import matplotlib
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
#from matplotlib.backends.backend_tkagg import NavigationToolbar2TkAgg
#from matplotlib.backends.backend_qt4agg import NavigationToolbar2QT
from matplotlib.figure import Figure
from matplotlib import style
import matplotlib.dates as mdates

import pandas as pd 
import DataPage

LARGE_FONT = ('Verdana', 12)
MID_FONT = ('Verdana', 10)
SMALL_FONT = ('Verdana', 8)

class GraphPage_(tk.Frame):
    df_1 = 0
    df_2 = 0
    df_3 = 0
    df_4 = 0
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label= tk.Label(self, text='Graph page', font=MID_FONT)
        label.pack(pady=10,padx=10)       
        ttk.Button(self, text='Data page',
                   command=lambda: controller.show_frame(DataPage.DataPage_)).pack()

        self.bind("<<ShowGraph>>", self.plot_graph)
        
    def select_col(df, start):      
        start_row  = int(start)
        end_row = int(start)+30
        df = df[start_row:end_row]
        df = df.reset_index(drop=True)
        return df
    
    def plot_graph(self, event):
        global df_1
        global df_2
        global df_3
        global df_4
        
        f = Figure(figsize=(5,5), dpi=100)
        a = f.add_subplot(111)
        
        a.plot(df_1['mean'])
        a.plot(df_2['mean'])
        a.plot(df_3['mean'])
        a.plot(df_4['mean'])
        a.legend(['bsl morning', '1st expo', 'bsl noon', '2nd expo'])
        canvas = FigureCanvasTkAgg(f, self)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)
    
    def split_for_graph(self, start_bsl_morning, start_1st_expo, start_bsl_noon, start_2nd_expo):
        """
        odabrane vrijednosti razdvajaju data frame na 4 manja framea 
        """
        global df_1
        global df_2
        global df_3
        global df_4
        df = self.controller.df.copy()
        df_1 = GraphPage_.select_col(df, start_bsl_morning)
        df_2 = GraphPage_.select_col(df, start_1st_expo)
        df_3 = GraphPage_.select_col(df, start_bsl_noon)
        df_4 = GraphPage_.select_col(df, start_2nd_expo)
        
        df_1_t = df_1.transpose()
        df_1_t = df_1_t.drop(df_1_t.index[0:4])
        df_1_t = df_1_t.reset_index(drop=True)
        df_1_t = df_1_t.iloc[:,0:5]
        df_1_t['BSL morning'] = df_1_t.mean(axis=1) 
        df_1_t = df_1_t['BSL morning']
                
        df_2_t = df_2.transpose()
        df_2_t = df_2_t.drop(df_2_t.index[0:4])
        df_2_t = df_2_t.reset_index(drop=True)
        df_2_t = df_2_t.iloc[:,0:5]
        df_2_t['1st adm'] = df_2_t.mean(axis=1) 
        df_2_t = df_2_t['1st adm']
        
        df_3_t = df_3.transpose()
        df_3_t = df_3_t.drop(df_3_t.index[0:4])
        df_3_t = df_3_t.reset_index(drop=True)
        df_3_t = df_3_t.iloc[:,0:5]
        df_3_t['BSL noon'] = df_3_t.mean(axis=1) 
        df_3_t = df_3_t['BSL noon']
        
        df_4_t = df_4.transpose()
        df_4_t = df_4_t.drop(df_4_t.index[0:4])
        df_4_t = df_4_t.reset_index(drop=True)
        df_4_t = df_4_t.iloc[:,0:5]
        df_4_t['2nd adm'] = df_4_t.mean(axis=1) 
        df_4_t = df_4_t['2nd adm']
        
        frames = [df_1_t, df_2_t, df_4_t]

        result = pd.concat(frames, axis=1)
        
        result['BSLvs1st'] = 'S'
        result['BSLvs1st'] = result['BSLvs1st'].where(result['BSL morning'] <= result['1st adm'], 'D' )
        result['BSLvs1st'] = result['BSLvs1st'].where(result['BSL morning'] >= result['1st adm'], 'I' )
        
        result['1stvs2nd'] = 'S'
        result['1stvs2nd'] = result['1stvs2nd'].where(result['1st adm'] <= result['2nd adm'], 'D' )
        result['1stvs2nd'] = result['1stvs2nd'].where(result['1st adm'] >= result['2nd adm'], 'I' )
        
        result['BSLvs1stvs2nd'] = 'B'
        result['BSLvs1stvs2nd'] = result['BSLvs1stvs2nd'].where((result['BSLvs1st']=='I') & (result['1stvs2nd']=='I'), 'False')
        print (result['BSLvs1st'].shape)
        print (result['1stvs2nd'].shape)
        print(result.shape)
        self.controller.result = result
        
        print(result.head(5))



