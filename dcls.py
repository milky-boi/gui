# -*- coding: utf-8 -*-
"""
Created on Tue Feb 26 14:31:58 2019

@author: mile
"""
import pandas as pd 
from dateutil.parser import parse
import dateutil
from dateutil.parser import *
from datetime import *

class Data:
    
    df = pd.DataFrame()

    start_col = 0
    end_col = 0
    start_row = 0
    end_row = 0
    
    def __init__(self, path):
        self.path = path
        
    @classmethod
    def data_frame(cls, path):
        cls.path=path
        df = pd.read_csv(cls.path, sep='\t', header=None)
        
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
        
        print('REZZZZZ: ' + str(df_info['datetime']))
        
        df_info['mean'] = None 
        df_info['std'] = None
        df_info['sum'] = None
        df_info = df_info.drop(columns=['broj', 'date', 'time'])
        
        cls.df = pd.concat([df_info, df_data], axis=1, sort=False)
        
        #print(cls.df.head())
        return df
    
    @classmethod
    def select_col(cls, start_col, end_col):
        """ data frame se razdvaja na df_info i df_data, u df_info uzeti su
        stupci sa informacijama iz tablice(datum, vrijeme, sum, mean, std)
        dok su u df_data brojcane vrijednsoti mjerenja   
        nakon seleckcije redaka i stupaca vrsi se promjena naziva stupaca u 
        df_data da odabrane jedinke budu poredane od broja 1
        """
        
        cls.start_col = start_col-1
        cls.end_col = end_col
        print(start_col)
        print(end_col)
        print(cls.df.shape)
        df_info = cls.df.iloc[:, :7]
        df_data = cls.df.iloc[:, 7:]
        
        df_data = df_data.iloc[:, start_col:end_col]
        header = []
        len_df = len(df_data.columns)+1
        for i in range(1,len_df):
            header.append(i) 
        df_data.columns = header
        
        cls.df = pd.concat([df_info, df_data], axis=1, sort=False)
        
        print('columns selected')  
        print(cls.df.shape)
        return cls.df
    
    @classmethod
    def select_rows(cls, start_row, end_row):
        """
        odabir redaka u data frameu, vraca novi data frame
        """
        cls.start_row = start_row
        cls.end_row = end_row

        df = cls.df[cls.start_row:cls.end_row]
        cls.start_row=None
        cls.end_row=None
        return df
    
    @classmethod
    def get_stats(cls):
        """
        izracunavanje vrijednosti za stupce mean, sum, std
        """
        
        df = cls.df.copy()
        df['mean'] = df.iloc[:,7:].mean(axis=1) 
        df['std'] = df.iloc[:,7:].std(axis=1) 
        df['sum'] = df.iloc[:,7:].sum(axis=1) 

        cls.df = df
        print('uspjesno df')        
        return df

    def display_data(self):
        print('displaying data... ')
        df_col = self.df.head()
        print(df_col)
    