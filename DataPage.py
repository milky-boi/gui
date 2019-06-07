import tkinter as tk
from tkinter import ttk
from tkinter import filedialog

import pandas as pd

from DataEdit import DataEdit_
from GraphPage import GraphPage_
from IndividualReport import IndividualReport_

#import GraphPage
LARGE_FONT = ('Verdana', 12)
MID_FONT = ('Verdana', 10)
SMALL_FONT = ('Verdana', 8)

class DataPage_(tk.Frame):
    """
    """
    #učitavanje pandas podataka u tablicu
    def on_show_frame(self, event):
        T = tk.Text(self, height=30, width=120, wrap=None)
        T.grid(row=2, column=4, columnspan=14, rowspan=14, padx=10, pady=10)
        T.insert(tk.END, self.controller.df)

    
    def filter_data(self,start_col,end_col,start_row,end_row):
        DataEdit_.select_cols_rows(self,start_col,end_col, start_row, end_row)
        T = tk.Text(self, height=30, width=120, wrap=None)
        T.grid(row=2, column=4, columnspan=14, rowspan=14, padx=10, pady=10)
        T.insert(tk.END, self.controller.df)

    def browse(self):
        filepath = filedialog.askopenfilename(
            initialdir = r"C:\\Users\\Desktop\\gui-master",
            title = "Select file",
            filetypes = (('txt','*.txt'),
            ("all files","*.*")))
        #controller je tk koji je pozvao ovaj prozor, odnosno DataApp, znači ovo sprema pandas dataframe u globalnu varijablu u DataApp
        pd.set_option('display.max_rows', None)
        pd.set_option('display.max_rows', None, 'display.max_columns', None)

        self.controller.df = pd.read_csv(filepath, sep='\t', header=None)
        DataEdit_.clear_data(self)
        self.controller.df = DataEdit_.get_stats(self)
        self.on_show_frame(self)

    #def split_table(self, start_bsl_morning, start_1st_expo, start_bsl_noon, start_2nd_expo):
    #    DataEdit_.split_for_graph(self, start_bsl_morning, start_1st_expo, start_bsl_noon, start_2nd_expo)
        
    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)
        tk.Label(self, text='Data edit').grid(pady=10,padx=10)
        
        ttk.Button(self, text='Browse files',
                   command=self.browse).grid(row=1)
        
        ttk.Button(self, text='Population',
                   command=lambda: controller.show_frame(GraphPage_)).grid(row=1, column=4)
        
        ttk.Button(self, text='Individual',
                   command=lambda: controller.show_frame(IndividualReport_)).grid(row=1, column=6)
        
        #controller je tk koji je pozvao ovaj prozor, odnosno DataApp, postavljamo 
        #ga na self kako bi mogli gore u on_show_frame pristupiti df-u i učitati ga u tablicu
        self.controller = controller
        #inicijaliziranje slušača za event koji pokreće funkciju učitavanja podataka 
        #iz pandasa u tablicu nakon što je otvoren ovaj prozor
        self.bind("<<ShowFrame>>", self.on_show_frame)

        #########ROWS AND COLUMNS SELECTION COL0####################################
        ttk.Label(self, text='Select flies:', font=MID_FONT).grid(row=2, column=1)           
        ttk.Label(self, text="Start column:" , font=SMALL_FONT).grid(row=3)
        ttk.Label(self, text="End column:", font=SMALL_FONT).grid(row=4)       
        
        start_col = tk.StringVar()
        end_col =tk.StringVar()     
        self.start_col = ttk.Entry(self, textvariable=start_col).grid(row=3, column=1)     
        self.end_col = ttk.Entry(self, textvariable=end_col).grid(row=4, column=1)                    

        """           s1 selection COL1            """
        ttk.Label(self, text='Time selection:', font=MID_FONT).grid(row=6, column=1)    
        ttk.Label(self, text="Start time:" , font=SMALL_FONT).grid(row=8)
        ttk.Label(self, text="End time:", font=SMALL_FONT).grid(row=9)       
               
        start_row = tk.StringVar()
        end_row =tk.StringVar()           
        self.start_row = ttk.Entry(self, textvariable=start_row).grid(row=8, column=1)     
        self.end_row = ttk.Entry(self, textvariable=end_row).grid(row=9, column=1)                    
        
        ttk.Button(self, text='Select main table', command=lambda: DataPage_.filter_data(self, start_col.get(),
                                                                                         end_col.get(),
                                                                                         start_row.get(),
                                                                                         end_row.get())).grid(row=10, column=1, padx=10, pady=10)
        
        ttk.Label(self, text="BSL morning:" , font=SMALL_FONT).grid(row=11)
        ttk.Label(self, text="1st expo:", font=SMALL_FONT).grid(row=12)       
        ttk.Label(self, text="BSL noon:", font=SMALL_FONT).grid(row=13)       
        ttk.Label(self, text="2nd expo:", font=SMALL_FONT).grid(row=14)       
              
        start_bsl_morning = tk.StringVar()
        start_1st_expo = tk.StringVar()
        start_bsl_noon = tk.StringVar()
        start_2nd_expo = tk.StringVar()
        
        self.start_bsl_morning = ttk.Entry(self, textvariable=start_bsl_morning).grid(row=11, column=1)     
        self.start_1st_expo = ttk.Entry(self, textvariable=start_1st_expo).grid(row=12, column=1)     
        self.start_bsl_noon = ttk.Entry(self, textvariable=start_bsl_noon).grid(row=13, column=1)     
        self.start_2nd_expo = ttk.Entry(self, textvariable=start_2nd_expo).grid(row=14, column=1)     
        
        
        
        ttk.Button(self, text='Split table',
                   command=lambda: GraphPage_.split_for_graph(
                           self,
                           start_bsl_morning.get(),
                           start_1st_expo.get(),
                           start_bsl_noon.get(),
                           start_2nd_expo.get())).grid(row=15, column=1, padx=10, pady=10)
        
        
        
        ttk.Button(self, text='Save XLSX',
                   command=lambda: DataEdit_.save_to_xlsx(self.controller.df)).grid(row=20, column=4) 
        ttk.Button(self, text='Save TXT',
                   command=lambda: DataEdit_.save_to_txt(self.controller.df)).grid(row=20, column=5) 
        
               