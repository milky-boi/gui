# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 02:11:11 2019

@author: mile
"""
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

from DataEdit import DataEdit_

LARGE_FONT = ('Verdana', 12)
MID_FONT = ('Verdana', 10)
SMALL_FONT = ('Verdana', 8)

class GraphPage_(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label= tk.Label(self, text='Graph page', font=MID_FONT)
        label.pack(pady=10,padx=10)
        
        ttk.Button(self, text='Draw')
        
        f = Figure(figsize=(5,5), dpi=100)
        
        a = f.add_subplot(111)
        #a.plot([1,2,3], [6,7,8])
        #a.plot(df_1['datetime'], df_1['mean'])
        
        #xfmt = mdates.DateFormatter('%d-%m-%y %H:%M')
        #a.xaxis.set_major_formatter(xfmt)        
        canvas = FigureCanvasTkAgg(f, self)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)
   
    def select_col(df, start):      
        start_row  = int(start)
        end_row = int(start)+30
        df = df[start_row:end_row]
        return df
        
    def split_for_graph(self, start_bsl_morning, start_1st_expo, start_bsl_noon, start_2nd_expo):
        """
        odabrane vrijednosti razdvajaju data frame na 4 manja framea 
        """
  
        df_1 = self.controller.df.copy()
        df_1 = GraphPage_.select_col(df_1, start_bsl_morning)
        
        df_2 = self.controller.df.copy()
        df_2 = GraphPage_.select_col(df_2, start_1st_expo)
        
        df_3 = self.controller.df.copy()
        df_3 = GraphPage_.select_col(df_3, start_bsl_noon)
        
        df_4 = self.controller.df.copy()
        df_4 = GraphPage_.select_col(df_4, start_2nd_expo)
        
        
        f = Figure(figsize=(5,5), dpi=100)
        
        a = f.add_subplot(111)
        a.plot(df_1['datetime'], df_1['mean'])    
        

        #print(df_1)
        #print('-----------------------------')
        print(df_1['mean'])

