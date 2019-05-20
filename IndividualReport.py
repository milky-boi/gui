# -*- coding: utf-8 -*-
"""
Created on Wed May  1 04:05:50 2019

@author: mile
"""

import tkinter as tk
from tkinter import ttk


import DataPage
import DataEdit
import GraphPage

LARGE_FONT = ('Verdana', 12)
MID_FONT = ('Verdana', 10)
SMALL_FONT = ('Verdana', 8)

class IndividualReport_(tk.Frame):
    def on_show_frame(self, event):
        T = tk.Text(self, height=35, width=80, wrap=None)
        T.grid(row=2, columnspan=2, rowspan=20, padx=10, pady=10)
        

        T.insert(tk.END, self.controller.result)
        
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label= tk.Label(self, text='Individiual report page', font=MID_FONT)
        label.grid(pady=10,padx=10)     
        ttk.Button(self, text='Data page',
                   command=lambda: controller.show_frame(DataPage.DataPage_)).grid(column=1)
        
        self.bind("<<ShowFrame>>", self.on_show_frame)


