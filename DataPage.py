import tkinter as tk
from tkinter import ttk

from DataEdit import DataEdit_

LARGE_FONT = ('Verdana', 12)
MID_FONT = ('Verdana', 10)
SMALL_FONT = ('Verdana', 8)

class DataPage_(tk.Frame):
    #učitavanje pandas podataka u tablicu
    def on_show_frame(self, event):
        T = tk.Text(self, height=20, width=140, wrap=None)
        T.grid(row=2, column=4, columnspan=14, rowspan=14, padx=10, pady=10)
        T.insert(tk.END, self.controller.df)
        
    def rows_and_col_select(self, start_col, end_col,
       start_time_s1, end_time_s1):
    
        """ova funkcija se poziva da bi se od unesenih podataka napravili data
        frameovi
        """        
        
    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)
        tk.Label(self, text='Data page', font=MID_FONT).grid(pady=10,padx=10)
        ttk.Button(self, text='Browse', ).grid(row=1)
        
        #controller je tk koji je pozvao ovaj prozor, odnosno DataApp, postavljamo ga na self kako bi mogli gore u on_show_frame pristupiti df-u i učitati ga u tablicu
        self.controller = controller
        #inicijaliziranje slušača za event koji pokreće funkciju učitavanja podataka iz pandasa u tablicu nakon što je otvoren ovaj prozor
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
        
        #ttk.Label(self, text='Time selection:', font=MID_FONT).grid(row=6, column=0)    
               
        ttk.Label(self, text="Start time:" , font=SMALL_FONT).grid(row=8)
        ttk.Label(self, text="End time:", font=SMALL_FONT).grid(row=9)       
               
        start_row = tk.StringVar()
        end_row =tk.StringVar()           
        self.start_row = ttk.Entry(self, textvariable=start_row).grid(row=8, column=1)     
        self.end_row = ttk.Entry(self, textvariable=end_row).grid(row=9, column=1)                    


        
        ttk.Button(self, text='Load data', command=lambda: DataEdit_.select_cols_rows(self,start_col.get(),
                                                                                         end_col.get(),
                                                                                         start_row.get(),
                                                                                         end_row.get())).grid(row=10, column=1, padx=10, pady=10)
        

        
         
         