import tkinter as tk
from tkinter import ttk
import pandas as pd 
from tkinter import filedialog

LARGE_FONT = ('Verdana', 12)
MID_FONT = ('Verdana', 10)
SMALL_FONT = ('Verdana', 8)


class DataApp(tk.Tk):
    df = pd.DataFrame()
    
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)     
        tk.Tk.wm_title(self, "DF select")
        
        container = tk.Frame(self)        
        container.pack(side='top', fill='both', expand=True)        
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        
        self.frames = {}      
        for F in (StartPage, DataPage):
            frame = F(container, self)        
            self.frames[F] = frame       
            frame.grid(row=0, column=0, sticky='nsew')       
        self.show_frame(StartPage)
        
    def browse():
        filepath = filedialog.askopenfilename(initialdir = r"C:\Users\ ",
                                              title = "Select file",
                                              filetypes = (('txt','*.txt'),
                                                           ("all files","*.*")))
        DataApp.df = pd.read_csv(filepath, sep='\t', header=None)  
        #ovdje sam probao insertati dataframe da ga se prikaze al ne zeli
        #pokusao sam vaijabli example takodjer proslijediti vrijednostr isto nece
        #DataPage.T.insert(tk.END, DataApp.df)
        """
        def show_all_clicked(self):  
            df=DataApp.df
            
            example.set(df)
            T.after(100, update_all)
        def update_all(self):
            T.delete('1.0', tk.END)
            T.insert(tk.END, DataApp.df)
        """
        #s ovom funkcijom sam pokusao updateati vrijednost koja se
        #prikazuje u text widgetu
        DataPage.T.delete('1.0', tk.END)
        DataPage.T.insert(tk.END, DataApp.df)        
            
    def show_frame(self, cont):      
        frame = self.frames[cont]       
        frame.tkraise()
        
class StartPage(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label= tk.Label(self, text='Start page', font=MID_FONT)
        label.pack(pady=10,padx=10)
        
        button1 = ttk.Button(self, text='Browse files', command=DataPage.browse)
        button1.pack()

        button3 = ttk.Button(self, text='Data page',
                             command=lambda: controller.show_frame(DataPage))
        button3.pack()
           
class DataPage(tk.Frame):
    
    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)
        label= tk.Label(self, text='Data page', font=MID_FONT)
        label.pack(pady=10,padx=10)
        button1 = ttk.Button(self, text='Start page', command=lambda: controller.show_frame(StartPage))
        button1.pack()
              
        example = pd.DataFrame()
        example = DataApp.df
        
        #data frame iz browse funkcije ovdje prikazujemo
        T = tk.Text(self, height=20, width=140, wrap=None)
        T.pack()
        T.insert(tk.END, example)
    
app = DataApp()
app.mainloop()
