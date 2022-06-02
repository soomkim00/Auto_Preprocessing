import tkinter as tk
import tkinter.ttk as ttk
from unittest import TextTestResult
import pandas as pd
from class_mainFrame import *
from function_Analysis import *
class analysisBox():
    def __init__(self, root):
        self.data = root.getData()
        window = tk.Tk()
        wrapper = tk.LabelFrame(window, text="Data Information")
        wrapper.pack()
        wrapper2 = tk.LabelFrame(window, text="Column Information")
        wrapper2.pack()
        def info():
            infos = tk.Tk()
            infos.title("Informations")
            lbl1 = tk.Label(infos, text = displaydict(getfirstlook(self.data)), anchor='w', justify='left')
            lbl1.pack()
            infos.mainloop()
            
        btn1 = tk.Button(wrapper, text="Basic Information", command=info)
        btn1.pack()
        def nullGraphic():
            show_msno_matrix(self.data)
            
        btn2 = tk.Button(wrapper, text="Null Graphic", command=nullGraphic)
        btn2.pack()

        def statistics():
            new_window = tk.Tk()
            stats = gettots(filterNumeric(self.data))
            treeview=ttk.Treeview(new_window, column = stats.columns)
            treeview.column("#0", width=40)
          
            cols = list(stats.columns)
            treeview["columns"] = cols
            for i in cols:
                treeview.column(i, anchor="w")
                treeview.heading(i, text=i, anchor='w')
            for index, row in stats.iterrows():
                treeview.insert("",0,text=index,values=list(row))
            treeview.pack()
        btn3 = tk.Button(wrapper, text = "Basic Statistics", command = statistics)
        btn3.pack()
        window.title("Analysis Box")
        window.geometry("720x600")
        window.resizable(False, False)
        window.mainloop()

