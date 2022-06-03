import tkinter as tk
import tkinter.ttk as ttk
import pandas as pd
from class_mainFrame import *
from function_Analysis import *
class analysisBox():
    def __init__(self, root):
        self.data = root.getData()
        window = tk.Tk()
        wrapper = tk.LabelFrame(window, text="Data Information")
        wrapper.pack()
        wrapper2 = tk.LabelFrame(window, text="Data Statistic")
        wrapper2.pack()
        def info():
            infos = tk.Tk()
            infos.title("Informations")
            lbl1 = tk.Label(infos, text = displaydict(getfirstlook(self.data)), anchor='w', justify='left')
            lbl1.pack()
            infos.mainloop()
            
        btn1 = tk.Button(wrapper, text="Basic Information", command=info)
        #btn1.pack()
        def nullGraphic():
            show_msno_matrix(self.data)
            
        btn2 = tk.Button(wrapper, text="Null Graphic", command=nullGraphic)
        #btn2.pack()

        def view():
                tree = ttk.Treeview(wrapper)
                tree.pack()
                cols = list(self.data.columns)
                tree["columns"] = cols
                print(types)
                types = list(getDataTypes(self.data).values())

                for i in cols:
                    tree.column(i, anchor="w")
                    tree.heading(i, text=i, anchor='w')
                for index, row in self.data[:5].iterrows():
                    tree.insert("",0,text=index,values=list(row))
                tree.insert("", 0,text = "", values = " ")
                tree.insert("", 0, text = "Types", values = types)

        def statistics():
            stats = gettots(filterNumeric(self.data)).transpose()
            treeview=ttk.Treeview(wrapper2, column = stats.columns)
            treeview.column("#0", width=50)
          
            cols = list(stats.columns)
            treeview["columns"] = cols
            for i in cols:
                treeview.column(i, anchor="w")
                treeview.heading(i, text=i, anchor='w')
            for index, row in stats.iterrows():
                treeview.insert("",0,text=index,values=list(row))
            treeview.pack()
        btn3 = tk.Button(wrapper, text = "Basic Statistics", command = statistics)
        #btn3.pack()
        view()
        statistics()
        window.title("Analysis Box")
        window.geometry("720x600")
        window.resizable(True, True)
        window.mainloop()

