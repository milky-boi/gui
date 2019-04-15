# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 21:27:14 2019

@author: mile
"""
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog

import pandas as pd 
import numpy as np
import DataPage


class DataEdit_:
      
    def select_cols_rows(self, start_col, end_col, start_row, end_row):
        """ data frame se razdvaja na df_info i df_data, u df_info uzeti su
        stupci sa informacijama iz tablice(datum, vrijeme, sum, mean, std)
        dok su u df_data brojcane vrijednsoti mjerenja   
        nakon seleckcije redaka i stupaca vrsi se promjena naziva stupaca u 
        df_data da odabrane jedinke budu poredane od broja 1
        """
        start_col = int(start_col)-1
        print(start_col)
        end_col = int(end_col)-1
        print(type(start_col))
        print(end_col)
        print(type(end_col))
        df_info = self.controller.df.iloc[:, :3]
        #ovdje cemo pozvati funkciju clear_data() koja ce dio tablice procistiti 
        df_data = self.controller.df.iloc[:, 3:]
        #print(df_info)
        #odabiremo jedinke koje smo unjeli u entryu
        df_data = df_data.loc[:, start_col:end_col]
        
        #postavljamo redne vrojeve od 1 na dalje
        header = []
        len_df = len(df_data.columns)+1
        for i in range(1,len_df):
            header.append(i) 
        df_data.columns = header
        
        #spajamo sve u jedan dat frame 
        df = pd.concat([df_info, df_data], axis=1, sort=False)
        
        #ovdje vrsimo selekciju redaka
        start_row = int(start_row)
        end_row = int(end_row)

        self.controller.df = df[start_row:end_row]
        #vrijednosti se brisu zbog druge selekcije nad podatcima
        start_row=None
        end_row=None

        DataEdit_.clear_data(self)
        self.controller.df = DataEdit_.get_stats(self)
        
        print('columns selected')  
        
    def clear_data(self):
        """
        ova funkcija brise nepotrebne stupce koji nisu jedinke i kreira
        stupac time koji je u formatu dd-mm-yyyy hh:mm:ssss imati na umu 
        da se nakon time stupca dodaju 3 nova stupca gdje se racunaju vrijednosti
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
        """
        df = self.controller.df.copy()
        
        df['mean'] = df.iloc[:,7:].mean(axis=1) 
        df['std'] = df.iloc[:,7:].std(axis=1) 
        df['sum'] = df.iloc[:,7:].sum(axis=1) 
        print('uspjesno df')    
        return df
    
    def save_to_xlsx(df):
        """spremanje data framea u xlsx formatu"""

        df.to_excel("selected_data.xlsx")
        print('pohranjeno u xlsx')
    
    def save_to_txt(df):
        """spremanje data framea u txt formatu"""
        
        df.to_csv('selcted_data.txt', header=True, index=False, sep='\t', float_format='%.3f') 
        
        print('pohranjeno u txt')
    
    def select_col(df, start):      
        start_row  = int(start)
        end_row = int(start)+30
        df = df[start_row:end_row]
        return df
        
    def split_for_graph(self, start_bsl_morning, start_1st_expo, start_bsl_noon, start_2nd_expo):
        """
        odabrane vrijednosti razdvajaju data frame na 4 manja framea i crta 
        se graf za vrijednosti
        """
  
        df_1 = self.controller.df.copy()
        df_1 = DataEdit_.select_col(df_1, start_bsl_morning)
        
        df_2 = self.controller.df.copy()
        df_2 = DataEdit_.select_col(df_2, start_1st_expo)
        
        df_3 = self.controller.df.copy()
        df_3 = DataEdit_.select_col(df_3, start_bsl_noon)
        
        df_4 = self.controller.df.copy()
        df_4 = DataEdit_.select_col(df_4, start_2nd_expo)
        
        
        #print(df_1)
        #print('-----------------------------')
        #print(df_1['mean'])
        
        
        
    
    