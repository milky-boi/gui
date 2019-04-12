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


LARGE_FONT = ('Verdana', 12)
MID_FONT = ('Verdana', 10)
SMALL_FONT = ('Verdana', 8)

class GraphPage_(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label= tk.Label(self, text='Graph page', font=MID_FONT)
        label.pack(pady=10,padx=10)
        
        f = Figure(figsize=(5,5), dpi=100)
        
        a = f.add_subplot(111)
        #a.plot(self.controller.df[1], self.controller.df[2])

        #xfmt = mdates.DateFormatter('%d-%m-%y %H:%M')
        #a.xaxis.set_major_formatter(xfmt)
        
        canvas = FigureCanvasTkAgg(f, self)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        
