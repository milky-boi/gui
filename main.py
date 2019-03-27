import matplotlib
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
#from matplotlib.backends.backend_tkagg import NavigationToolbar2TkAgg
#from matplotlib.backends.backend_qt4agg import NavigationToolbar2QT
from matplotlib.figure import Figure
from matplotlib import style
import matplotlib.dates as mdates

import tkinter as tk
from tkinter import filedialog
from tkinter import ttk

import pandas as pd 
import dcls


LARGE_FONT = ('Verdana', 12)
MID_FONT = ('Verdana', 10)
SMALL_FONT = ('Verdana', 8)
style.use('ggplot')


class DataApp(tk.Tk):
    #filepath = r'C:/Users/mile/Desktop/biotech/DAM 1 bin/CTRL -3.txt' 
    #filepath = r' '  
    _start_col = tk.IntVar
    _end_col = tk.IntVar    
    _start_row = tk.IntVar   
    _start_col = tk.IntVar

    df_1 = pd.DataFrame()
    df_2 = pd.DataFrame()
    df_3 = pd.DataFrame()
    df_4 = pd.DataFrame()
        
    #filepath = tk.StringVar
    #df = pd.DataFrame()
    df = pd.read_csv(filepath, sep='\t', header=None)
    
    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)     
        tk.Tk.iconbitmap(self, default='clienticon.ico')
        tk.Tk.wm_title(self, "Data edit Milky boi app")
        
        container = tk.Frame(self)        
        container.pack(side='top', fill='both', expand=True)        
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        
        self.frames = {}      
        for F in (StartPage, DataPage, GraphPage):
            frame = F(container, self)        
            self.frames[F] = frame       
            frame.grid(row=0, column=0, sticky='nsew')       
        self.show_frame(StartPage)
        
        
    def show_frame(self, cont):      
        frame = self.frames[cont]
        frame.tkraise()
        
    def browse():
        """dohvacanje putanje do filea koji zelimo ucitati, potom se vrijednost
        filename treba pretvoriti u df
        """
        ###PROBLEM
        filepath = filedialog.askopenfilename(initialdir = r"C:\Users\mile\Desktop\biotech",
                                              title = "Select file",
                                              filetypes = (('txt','*.txt'),
                                                           ("all files","*.*")))
        DataApp.df = pd.read_csv(filepath, sep='\t', header=None)   
        return filepath
        
        
    def rows_and_col_select(start_col, end_col,
           start_time_s1, end_time_s1,
           start_time_s2, end_time_s2,
           start_time_s3, end_time_s3,
           start_time_s4, end_time_s4):
        
        """ova funkcija se poziva da bi se od unesenih podataka napravili data
        frameovi
        """        
        
        DataApp.df = dcls.Data.select_col(int(start_col), int(end_col))
        DataApp.df = dcls.Data.get_stats()
        
        DataApp.df_1 = DataApp.df
        DataApp.df_1 = dcls.Data.select_rows(int(start_time_s1), int(end_time_s1))
        
        DataApp.df_2 = DataApp.df
        DataApp.df_2 = dcls.Data.select_rows(int(start_time_s2), int(end_time_s2))
        
        DataApp.df_3 = DataApp.df
        DataApp.df_3 = dcls.Data.select_rows(int(start_time_s3), int(end_time_s3))
        
        DataApp.df_4 = DataApp.df
        DataApp.df_4 = dcls.Data.select_rows(int(start_time_s4), int(end_time_s4))
        
        
class StartPage(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label= tk.Label(self, text='Start page', font=MID_FONT)
        label.pack(pady=10,padx=10)
        
        button1 = ttk.Button(self, text='Browse files', command=DataApp.browse)
        button1.pack()
        
        """
        potrebno je prilikom otvaranja ove stranice napraviti prikaz ucitanog
        data framea u text widgetu
        """
        button2 = ttk.Button(self, text='Data selection page',
                             command=lambda: start())
        button2.pack()
        
        button3 = ttk.Button(self, text='Graph page', command=lambda: controller.show_frame(GraphPage))
        button3.pack()
        
        def start():
            """
            trebala bi pozivati 2 funkcije, 1 za prikaz stranice a druga za update 
            koji bi trebao prikazati df
            """
            controller.show_frame(DataPage)
            #DataPage.show_all_clicked()
            
        
class DataPage(tk.Frame):
    
    broj = 1000

    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)
        example = tk.StringVar()
        example.set(DataApp.df)
        
        def show_all_clicked(self):  
            df=DataApp.df
            
            example.set(df)
            T.after(100, update_all)
        def update_all(self):
            T.delete('1.0', tk.END)
            T.insert(tk.END, DataApp.df)
        
        def s1_clicked():  
            df_1=DataApp.df_1
            pd.set_option('display.max_rows', None,
                          'display.max_columns', None)
            example.set(df_1)
            print(type(example))
            T.after(100, update_s1)
        def update_s1():
            T.delete('1.0', tk.END)
            T.insert(tk.END, DataApp.df_1)
            
        def s2_clicked():  
            df=DataApp.df_2
            
            example.set(df)
            T.after(100, update_s2)
        def update_s2():
            T.delete('1.0', tk.END)
            T.insert(tk.END, DataApp.df_2)
            
        def s3_clicked():  
            df=DataApp.df_3
            
            example.set(df)
            T.after(100, update_s3)
        def update_s3():
            T.delete('1.0', tk.END)
            T.insert(tk.END, DataApp.df_3)
            
        def s4_clicked():  
            df=DataApp.df_4
            
            example.set(df)
            T.after(100, update_s4)
                        
        def update_s4():
            T.delete('1.0', tk.END)
            T.insert(tk.END, DataApp.df_4)
            
        
        tk.Label(self, text='Data page', font=MID_FONT).grid(row=0)
        
        button1 = ttk.Button(self, text='Start page', command=lambda: controller.show_frame(StartPage))
        button1.grid(row=0, column=1)
      
        button2 = ttk.Button(self, text='Show S1', command= s1_clicked)
        button2.grid(row=1, column=4)
        button3 = ttk.Button(self, text='Show S2', command=s2_clicked)
        button3.grid(row=1, column=5)
        button4 = ttk.Button(self, text='Show S3', command=s3_clicked)
        button4.grid(row=1, column=6)
        button5 = ttk.Button(self, text='Show S4', command=s4_clicked)
        button5.grid(row=1, column=7)
        button5 = ttk.Button(self, text='Show all', command=show_all_clicked)
        button5.grid(row=1, column=8)
        
        
        self.df = dcls.Data.data_frame(DataApp.filepath)
        #########ROWS AND COLUMNS SELECTION COL0####################################
        ttk.Label(self, text='Pick columns', font=MID_FONT).grid(row=1, column=1)           
        ttk.Label(self, text="Start column:" , font=SMALL_FONT).grid(row=2)
        ttk.Label(self, text="End column:", font=SMALL_FONT).grid(row=3)       
        
        start_col = tk.StringVar()
        end_col =tk.StringVar()     
        self.start_col = ttk.Entry(self, textvariable=start_col).grid(row=2, column=1)     
        self.end_col = ttk.Entry(self, textvariable=end_col).grid(row=3, column=1)                    

        """           s1 selection COL1            """
        ttk.Label(self, text='Pick rows', font=MID_FONT).grid(row=5, column=1)    
        
        ttk.Label(self, text='S1', font=MID_FONT).grid(row=6, column=0)    
               
        ttk.Label(self, text="Start time:" , font=SMALL_FONT).grid(row=7)
        ttk.Label(self, text="End time:", font=SMALL_FONT).grid(row=8)       
               
        start_time_s1 = tk.StringVar()
        end_time_s1 =tk.StringVar()           
        self.start_time_s1 = ttk.Entry(self, textvariable=start_time_s1).grid(row=7, column=1)     
        self.end_time_s1 = ttk.Entry(self, textvariable=end_time_s1).grid(row=8, column=1)                    

        """           s2 selection COL1            """
        ttk.Label(self, text='S2', font=MID_FONT).grid(row=9) 
        ttk.Label(self, text="Start time:" , font=SMALL_FONT).grid(row=10)
        ttk.Label(self, text="End time:", font=SMALL_FONT).grid(row=11)
        
        start_time_s2 =tk.StringVar()
        end_time_s2 =tk.StringVar()   
        self.start_time_s2 = ttk.Entry(self, textvariable=start_time_s2).grid(row=10, column=1)            
        self.end_time_s2 = ttk.Entry(self, textvariable=end_time_s2).grid(row=11, column=1)
        
        """           s3 selection COL1            """
        ttk.Label(self, text='S3', font=MID_FONT).grid(row=12, column=0)    
        ttk.Label(self, text="Start time:" , font=SMALL_FONT).grid(row=13)
        ttk.Label(self, text="End time:", font=SMALL_FONT).grid(row=14)       
        
        start_time_s3 = tk.StringVar()
        end_time_s3 =tk.StringVar()   
        self.start_time_s3 = ttk.Entry(self, textvariable=start_time_s3).grid(row=13, column=1)     
        self.end_time_s3 = ttk.Entry(self, textvariable=end_time_s3).grid(row=14, column=1)                    
        
        """           s4 selection COL1            """
        ttk.Label(self, text='S4', font=MID_FONT).grid(row=15)  
        ttk.Label(self, text="Start time:" , font=SMALL_FONT).grid(row=16)
        ttk.Label(self, text="End time:", font=SMALL_FONT).grid(row=17)

        start_time_s4 =tk.StringVar()
        end_time_s4 =tk.StringVar()   
        self.start_time_s4 = ttk.Entry(self, textvariable=start_time_s4).grid(row=16, column=1)            
        self.end_time_s4 = ttk.Entry(self, textvariable=end_time_s4).grid(row=17, column=1)


        
        ttk.Button(self, text='Load data', command=lambda: DataApp.rows_and_col_select(start_col.get(),
                                                                        end_col.get(),
                                                                        start_time_s1.get(),
                                                                        end_time_s1.get(),
                                                                        start_time_s2.get(),
                                                                        end_time_s2.get(),
                                                                        start_time_s3.get(),
                                                                        end_time_s3.get(),
                                                                        start_time_s4.get(),
                                                                        end_time_s4.get())).grid(row=18, column=1, padx=10, pady=10)
        
        
        
        ttk.Button(self, text='Save XLSX', command= show_all_clicked).grid(row=20, column=8) 
        ttk.Button(self, text='Save TXT', command= show_all_clicked).grid(row=20, column=9) 
               
        
        
        
        # Horizontal (x) Scroll bar
        xscrollbar = ttk.Scrollbar(self, orient='horizontal')
        xscrollbar.grid(column=4, row=19, columnspan=17,  sticky='swe')
        
        # Vertical (y) Scroll Bar
        yscrollbar = ttk.Scrollbar(self)
        yscrollbar.grid(column=19, row=2, rowspan=17,  sticky='ens')
        
        T = tk.Text(self, height=20, width=140, wrap=None,
                    xscrollcommand=xscrollbar.set,
                    yscrollcommand=yscrollbar.set)
        T.grid(row=2, column=4, columnspan=14, rowspan=17, padx=10, pady=10)
        
        #quote = pd.read_csv(DataApp.filepath, sep='\t', header=None)
        T.insert(tk.END, example)
        xscrollbar.config(command=T.xview)
        yscrollbar.config(command=T.yview)

        #ttk.Scrollbar(T, orient="horizontal")
        #button4 = ttk.Button(self, text='Save new table', command= whenclicked).grid(row=14, column=3)   
        
                                  
class GraphPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label= tk.Label(self, text='Graph page', font=MID_FONT)
        label.pack(pady=10,padx=10)
        
        button1 = ttk.Button(self, text='Start page', command=lambda: controller.show_frame(StartPage))
        button1.pack()
        
        f = Figure(figsize=(5,5), dpi=100)
        
        a = f.add_subplot(111)
        a.plot(DataApp.df[3], DataApp.df[16])

        #xfmt = mdates.DateFormatter('%d-%m-%y %H:%M')
        #a.xaxis.set_major_formatter(xfmt)
        
        canvas = FigureCanvasTkAgg(f, self)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        
        ##toolbar = NavigationToolbar2TkAgg(canvas, self)
        ##toolbar.update()
        ##canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)        

  

app = DataApp()
app.mainloop()



    

 