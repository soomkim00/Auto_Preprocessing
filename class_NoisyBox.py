import tkinter as tk
import tkinter.ttk as ttk
import pandas as pd
from class_mainFrame import *
from function_Noisy import *
import datetime as dt


class NoisyBox():
    def __init__(self, root):
        df = root.getData()
        window =  tk.Tk()
        self.options = {}
        self.log = []
        
        cols = list(filterNumeric(df).columns)
        for c in cols:
            self.options[c] = ['Default', 'Do Nothing', 'Do Nothing']
     
        wrapper = tk.LabelFrame(window, text="Select Column")
        wrapper.grid(row=0, column = 0, ipadx= 18, padx = 10, pady = 10)
        wrapper2 = tk.LabelFrame(window, text="Select Options")
        wrapper2.grid(row=1, column = 0, padx=10, pady=10)
        wrapper3 = tk.LabelFrame(window, text= "Selected Options", relief="flat", bd=2, width=1000)
        wrapper3.grid(row=0, column = 1, rowspan=2, padx=10, pady=10, sticky="n", ipady = 30)
        self.treeview=ttk.Treeview(wrapper3, column = ["Time", "Column", "Method"])
        self.treeview["columns"] = ["Time", "Column", "Method"]
        self.treeview.column("#0", width=33)
        self.treeview.heading("#0", text="num")
        for i in range(len(self.treeview["columns"])):
            self.treeview.heading(self.treeview["columns"][i], text = self.treeview["columns"][i], anchor="w")
        self.treeview.column("#1", width = 109)
        self.treeview.column("#2", width = 150)
        self.treeview.pack()

        def insertLog(option):
            self.treeview.insert("", "end", text = len(self.log)+1, values = option, iid=len(self.log))


        label1 = tk.Label(wrapper, text = "Column")
        label1.grid(row=0, column=0, padx = 10, pady = 10)
        
        mycombo = ttk.Combobox(wrapper, height = 15, values = [["Column Not Selected"]]+cols, width=30)
        mycombo.current(0)
        mycombo.grid(row = 0, column = 1)

        def colOptions():
            colName = mycombo.get()
            self.options[colName] = [mycombo1.get()]
            insertLog((dt.datetime.now(), colName, mycombo1.get()))
            self.log.append((dt.datetime.now(), colName, mycombo1.get()))
            

        btnSaveOptions = tk.Button(wrapper2, text="Save Column Options", command=colOptions)
        btnSaveOptions.grid(row = 4, column=0, padx=10, pady=10)

        outlier_method = ["[Q1-1.5*IQR, Q3+1.5*IQR]이외값 제거"]  
        label2 = tk.Label(wrapper2, text = "처리 방법   :")
        label2.grid(row=0, column=0, padx = 10, pady = 10)
        
        mycombo1 = ttk.Combobox(wrapper2, height = 15, values = outlier_method, width=30)
        mycombo1.current(0)
        mycombo1.grid(row = 0, column = 1, padx = 5, pady = 5)



        def selectData():
            global outlier_method_select
            outlier_method_select = mycombo1.get()
            print(outlier_method_select)

        btn_selectData = tk.Button(wrapper2, text = "Select", command = selectData)
        btn_selectData.grid(row = 0, column = 2, padx = 5, pady = 5)

        label2 = tk.Label(wrapper, text = "Column   :")
        label2.grid(row=0, column=0, padx = 10, pady = 10)
        
        def selectcolumn():
            global select_outlier_column
            select_outlier_column = mycombo.get()
            print(select_outlier_column)

        btn_selectcolumn = tk.Button(wrapper, text = "Select", command = selectcolumn)
        btn_selectcolumn.grid(row = 0, column = 2, padx = 5, pady = 5)



        def outlier_out():
            try:
                print(df['{}'.format(select_outlier_column)])
                oulier_idx  = outlier_remove(df, select_outlier_column)
                df.drop(oulier_idx, axis=0, inplace=True)                
                root.appendLog(self.processLog())
                root.pushStack(df)
                print(df)
                secces()
            except:
                warn()

        a1 = tk.Label(wrapper3, text = "")
        a1.pack()
        btnOK = tk.Button(wrapper3, text = "OK", command= outlier_out)
        btnOK.pack()

        window.title("OutlierBox")
        window.geometry("1000x350")
        window.resizable(True, True)
        window.mainloop()

    def processLog(self):
        log = []
        for i in self.options.keys():
            defaultOption = ['Default', 'Do Nothing', 'Do Nothing']
            if self.options[i] != defaultOption:
                log.append([dt.datetime.now(), i, self.options[i]])
        return log
