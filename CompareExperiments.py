# -*- coding: utf-8 -*-
"""
Created on Thu May 16 13:24:37 2019

@author: mile
"""
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import pandas as pd

import DataPage
from DataEdit import DataEdit_

LARGE_FONT = ('Verdana', 12)
MID_FONT = ('Verdana', 10)
SMALL_FONT = ('Verdana', 8)

class CompareExperiments_(tk.Frame):
    def on_show_frame(self, event: object) -> object:
        T = tk.Text(self, height=35, width=80, wrap=None)
        T.grid(row=4, columnspan=4, rowspan=20, padx=10, pady=10)
        
        T.insert(tk.END, self.controller.exp_comp_results)
    def compare_experiments(self, df_1, df_2, df_3):
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

        result_bsl_vs_first.to_excel('result_bsl_vs_first.xlsx')
        result_first_second.to_excel('result_first_second.xlsx')
        result_bsl_first_second.to_excel("result_bsl_first_second.xlsx")

        self.controller.exp_comp_results = result_bsl_vs_first
        self.on_show_frame(self)
        pass

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label= tk.Label(self, text='Experiment comparing', font=MID_FONT)
        label.grid(pady=10,padx=10)     
        ttk.Button(self, text='Data page',
                   command=lambda: controller.show_frame(DataPage.DataPage_)).grid(column=1)

        ttk.Button(self, text='Browse experiment 1',
                   command=self.browse_exp_1).grid(row=1, padx=10, pady=10)
        ttk.Button(self, text='Browse experiment 2',
                   command=self.browse_exp_2).grid(row=2, padx=10, pady=10)
        ttk.Button(self, text='Browse experiment 3',
                   command=self.browse_exp_3).grid(row=3, padx=10, pady=10)
        ttk.Button(self, text='Split table',
                   command=lambda: CompareExperiments_.compare_experiments(
                       self,
                       self.controller.df_exp_1,
                       self.controller.df_exp_2,
                       self.controller.df_exp_3)).grid(row=3, column=1, padx=10, pady=10)

        self.bind("<<ShowFrame>>", self.on_show_frame)

    def browse_exp_1(self):
        filepath = filedialog.askopenfilename(
            initialdir = r"C:\\Users\\Desktop\\gui-master",
            title = "Select file",
            filetypes = (('xlsx','*.xlsx'),
            ("all files","*.*")))
        #controller je tk koji je pozvao ovaj prozor, odnosno DataApp, znači ovo sprema pandas dataframe u globalnu varijablu u DataApp
        pd.set_option('display.max_rows', None)
        pd.set_option('display.max_rows', None, 'display.max_columns', None)

        self.controller.df_exp_1 = pd.read_excel(filepath, index_col=0 )

    def browse_exp_2(self):
        filepath = filedialog.askopenfilename(
            initialdir = r"C:\\Users\\Desktop\\gui-master",
            title = "Select file",
            filetypes = (('xlsx','*.xlsx'),
            ("all files","*.*")))
        #controller je tk koji je pozvao ovaj prozor, odnosno DataApp, znači ovo sprema pandas dataframe u globalnu varijablu u DataApp
        pd.set_option('display.max_rows', None)
        pd.set_option('display.max_rows', None, 'display.max_columns', None)

        self.controller.df_exp_2 = pd.read_excel(filepath, index_col=0 )

    def browse_exp_3(self):
        filepath = filedialog.askopenfilename(
            initialdir = r"C:\\Users\\Desktop\\gui-master",
            title = "Select file",
            filetypes = (('xlsx','*.xlsx'),
            ("all files","*.*")))
        #controller je tk koji je pozvao ovaj prozor, odnosno DataApp, znači ovo sprema pandas dataframe u globalnu varijablu u DataApp
        pd.set_option('display.max_rows', None)
        pd.set_option('display.max_rows', None, 'display.max_columns', None)

        self.controller.df_exp_3 = pd.read_excel(filepath, index_col=0 )

