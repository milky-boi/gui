import tkinter as tk
from tkinter import ttk
import pandas as pd 
from tkinter import filedialog

from StartPage import StartPage_
from DataPage import DataPage_
from GraphPage import GraphPage_

LARGE_FONT = ('Verdana', 12)
MID_FONT = ('Verdana', 10)
SMALL_FONT = ('Verdana', 8)



class DataApp_(tk.Tk):
    
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)     
        tk.Tk.wm_title(self, "DF select")
        
        container = tk.Frame(self)        
        container.pack(side='top', fill='both', expand=True)        
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        
        #globalna varijabla sa panda podacima koju mogu korisitti svi frejmovi nakon što su podaci učitani
        self.df = pd.DataFrame()

        self.frames = {}      
        for F in (StartPage_, DataPage_, GraphPage_):
            frame = F(container, self)        
            self.frames[F] = frame       
            frame.grid(row=0, column=0, sticky='nsew')       
        self.show_frame(StartPage_)

    def show_frame(self, cont):   
        frame = self.frames[cont]       
        frame.tkraise()

        #event koji se odašilje kada je bilo koji frejm otvoren
        frame.event_generate("<<ShowFrame>>")
        