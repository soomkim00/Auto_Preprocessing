import tkinter as tk
import tkinter.ttk as ttk
import pandas as pd
from function_Trans import *
from class_mainFrame import *
import datetime as dt

class TransBox():
    def __init__(self, root):
        df = root.getData()
        window =  tk.Tk()
        self.options = {}
        self.log = []

        cols = list(df.columns)
        for c in cols:
            self.options[c] = ['Default','column','method']

        wrapper = tk.LabelFrame(window, text="Select Column")
        wrapper.grid(row=0, column = 0, ipadx= 18, padx = 10, pady = 10)
        wrapper2 = tk.LabelFrame(window, text="Select Options")
        wrapper2.grid(row=1, column = 0, padx=10, pady=10)
        wrapper3 = tk.LabelFrame(window, text= "Selected Options", relief="flat", bd=2, width=1000)
        wrapper3.grid(row=0, column = 1, rowspan=2, padx=10, pady=10, sticky="n", ipady = 30)
        self.treeview=ttk.Treeview(wrapper3, column = ["Time", "Column", "Method"])
        self.treeview["columns"] = ["Time", "Column", "method"]
        self.treeview.column("#0", width=33)
        self.treeview.heading("#0", text="num")
        for i in range(len(self.treeview["columns"])):
            self.treeview.heading(self.treeview["columns"][i], text = self.treeview["columns"][i], anchor="w")
        self.treeview.column("#1", width = 109)
        self.treeview.column("#2", width = 100)
        self.treeview.pack()
        def insertLog(option):
            self.treeview.insert("", "end", text = len(self.log), values = option, iid=len(self.log))
        scl_method = ["StandardScaler", "MinMaxScaler", "MaxAbsScaler", "RobustScaler"]  #"RobustScaler", "MaxAbsScaler" 추가 ?

        label1 = tk.Label(wrapper2, text = "변환 방법   :")
        label1.grid(row=0, column=0)
        
        mycombo1 = ttk.Combobox(wrapper2, height = 15, values = scl_method, width=30)
        mycombo1.current(0)
        mycombo1.grid(row = 0, column = 1)

        def selectData():
            global transformation_method
            transformation_method = mycombo1.get()
            print(transformation_method)

        btn_selectData = tk.Button(wrapper2, text = "Select", command = selectData)
        btn_selectData.grid(row = 0, column = 2, padx = 5, pady = 5)

        cols_trans = ["Column Not Selected "] + list(filterNumeric(df).columns)
        label2 = tk.Label(wrapper, text = "Column   :")
        label2.grid(row=0, column=0, padx = 10, pady = 10)
        
        mycombo = ttk.Combobox(wrapper, height = 15, values = cols_trans, width=30)
        mycombo.current(0)
        mycombo.grid(row = 0, column = 1)

        def selectcolumn():
            global select_trans_column
            select_trans_column = mycombo.get()
            print(select_trans_column)

        btn_selectcolumn = tk.Button(wrapper, text = "Select", command = selectcolumn)
        btn_selectcolumn.grid(row = 0, column = 2, padx = 5, pady = 5)

        def colOptions():
            colName = mycombo.get()
            self.options[colName] = [mycombo1.get()]
            insertLog((dt.datetime.now(), colName, mycombo1.get()))
            self.log.append((dt.datetime.now(), colName, mycombo1.get()))
            
        btnSaveOptions = tk.Button(wrapper2, text="Save Column Options", command=colOptions)
        btnSaveOptions.grid(row = 4, column=0, padx=10, pady=10)





        def trans():
            try:    
                if(transformation_method=="StandardScaler"):
                    df['{}'.format(select_trans_column)] = def_StandardScaler(df, select_trans_column)
                    root.appendLog(self.processLog())
                    root.pushStack(df)
                    print(df)
                    secces()
                elif(transformation_method=="MinMaxScaler"):
                    df['{}'.format(select_trans_column)] = def_MinMaxScaler(df, select_trans_column)
                    root.appendLog(self.processLog())
                    root.pushStack(df)
                    print(df)
                    secces()
                elif(transformation_method=="MaxAbsScaler"):
                    df['{}'.format(select_trans_column)] = def_MaxAbsScaler(df, select_trans_column)
                    root.appendLog(self.processLog())
                    root.pushStack(df)
                    print(df)
                    secces()
                elif(transformation_method=="RobustScaler"):
                    df['{}'.format(select_trans_column)] = def_RobustScaler(df, select_trans_column)
                    root.appendLog(self.processLog())
                    root.pushStack(df)
                    print(df)
                    secces()
                else:
                    pass
            except:
                warn()

        btnOK = tk.Button(wrapper3, text = "OK", command= trans)
        btnOK.pack()


        window.title("TransformationBox")
        window.geometry("900x350")
        window.resizable(False, False)
        window.mainloop()
    def processLog(self):
        log = []
        for i in self.options.keys():
            defaultOption = ['Default','column','method']
            if self.options[i] != defaultOption:
                log.append([dt.datetime.now(), i, self.options[i]])
        return log