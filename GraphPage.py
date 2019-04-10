# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 02:11:11 2019

@author: mile
"""
import tkinter as tk
from tkinter import ttk
import pandas as pd 
from tkinter import filedialog

LARGE_FONT = ('Verdana', 12)
MID_FONT = ('Verdana', 10)
SMALL_FONT = ('Verdana', 8)

class GraphPage_(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label= tk.Label(self, text='Graph page', font=MID_FONT)
        label.pack(pady=10,padx=10)