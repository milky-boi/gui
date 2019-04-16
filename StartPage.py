import tkinter as tk
from tkinter import ttk
import pandas as pd 
from tkinter import filedialog

from DataPage import DataPage_
from GraphPage import GraphPage_
from DataEdit import DataEdit_
LARGE_FONT = ('Verdana', 12)
MID_FONT = ('Verdana', 10)
SMALL_FONT = ('Verdana', 8)

class StartPage_(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label= tk.Label(self, text='Start page', font=MID_FONT)
        label.pack(pady=10,padx=10)
        button1 = ttk.Button(self, text='Browse files', 
                                command=self.browse).pack()
        button3 = ttk.Button(self, text='Data page',
                                command=lambda: controller.show_frame(DataPage_)).pack()
        button4 = ttk.Button(self, text='Graph page',
                                command=lambda: controller.show_frame(GraphPage_)).pack()

    #ima više logike da je browse tu nego u DataApp
    def browse(self):
        filepath = filedialog.askopenfilename(
            initialdir = r"C:\\Users\\Desktop\\gui-master",
            title = "Select file",
            filetypes = (('txt','*.txt'),
            ("all files","*.*"))) 
        #controller je tk koji je pozvao ovaj prozor, odnosno DataApp, znači ovo sprema pandas dataframe u globalnu varijablu u DataApp
        pd.set_option('display.max_rows', None)
        #pd.set_option('display.max_rows', None, 'display.max_columns', None)

        self.controller.df = pd.read_csv(filepath, sep='\t', header=None)
        DataEdit_.clear_data(self)
        self.controller.df = DataEdit_.get_stats(self)