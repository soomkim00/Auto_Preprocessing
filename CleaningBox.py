import tkinter as tk
import tkinter.ttk as ttk
from numpy import NaN
import pandas as pd
from function_Cleaning import * 
from class_mainFrame import *
import datetime as dt


class CleaningBox():
    def __init__(self, root):
        df = root.getData()
        window =  tk.Tk()
        self.options = {}
        self.log = []
        amount_missing = tk.StringVar()
        amount_DataRow = tk.StringVar()
        
        cols = ["Column Not Selected"] + list(df.columns)
        for c in cols:
            self.options[c] = ['Default', 'Do Nothing', 'Do Nothing']
        del self.options["Column Not Selected"]



        wrapper = tk.LabelFrame(window, text="Select Column")
        wrapper.grid(row=0, column = 0, ipadx= 18, padx = 10, pady = 10)
        wrapper2 = tk.LabelFrame(window, text="Select Options")
        wrapper2.grid(row=1, column = 0, padx=10, pady=10)
        wrapper3 = tk.LabelFrame(window, text= "Selected Options", relief="flat", bd=2, width=1000)
        wrapper3.grid(row=0, column = 1, rowspan=2, padx=10, pady=10, sticky="n", ipady = 30)
        self.treeview=ttk.Treeview(wrapper3, column = ["Time", "Column", "Data Type", "Missing Value","Drop Column"])
        self.treeview["columns"] = ["Time", "Column", "Data Type", "Missing Value","Drop Column"]
        self.treeview.column("#0", width=40)
        self.treeview.heading("#0", text="num")
        for i in range(len(self.treeview["columns"])):
            self.treeview.column(self.treeview["columns"][i], width = 120)
            self.treeview.heading(self.treeview["columns"][i], text = self.treeview["columns"][i], anchor="w")
        self.treeview.pack()

        def insertLog(option):
            self.treeview.insert("", "end", text = len(self.log), values = option, iid=len(self.log))


        label1 = tk.Label(wrapper, text = "Column")
        label1.grid(row=0, column=0, padx = 10, pady = 10)
        
        mycombo = ttk.Combobox(wrapper, height = 15, values = cols, width=30)
        mycombo.current(0)
        mycombo.grid(row = 0, column = 1)
        
        def lookupColumn():
            colName = mycombo.get()
            amount_missing = df[colName].isnull().sum(axis=0)
            amount_DataRow = len(df.index)
            missingRatio = round(amount_missing/amount_DataRow * 100, 2) 
            lblMissingValues.configure(text = str(amount_missing) + "/" + str(amount_DataRow) + " ("+str(missingRatio)+ "%)")

            combo1.current(0)
            combo2.current(0)
            combo3.current(0)

        def colOptions():
            colName = mycombo.get()
            self.options[colName] = [combo1.get(), combo2.get(), combo3.get()]
            insertLog((dt.datetime.now(), colName, combo1.get(), combo2.get(), combo3.get()))
            self.log.append((dt.datetime.now(), colName, combo1.get(), combo2.get(), combo3.get()))
            

        btnSelectCol = tk.Button(wrapper, text="Select", command=lookupColumn)
        btnSaveOptions = tk.Button(wrapper2, text="Save Column Options", command=colOptions)

        btnSelectCol.grid(row = 0, column=2, padx=10, pady=10)
        btnSaveOptions.grid(row = 4, column=0, padx=10, pady=10)


        lbl1 = tk.Label(wrapper2, text = "Data Type")
        lbl1.grid(row=0, column=0, padx = 10, pady=10)
        datatypes = ["Default","Numeric", "Categorical", "Datetime"]
        combo1 = ttk.Combobox(wrapper2, height = 15, values = datatypes, width = 30)
        combo1.current(0)
        combo1.grid(row=0, column=1, padx=10, pady=10)

        

        lbl2 = tk.Label(wrapper2, text = "# of Missing Values :")
        lblMissingValues = tk.Label(wrapper2, text = "Column Not Selected")
        lbl2.grid(row=1, column=0, padx = 10, pady=10)
        lblMissingValues.grid(row=1, column=1, padx = 10, pady=10)

        lbl3 = tk.Label(wrapper2, text = "Handle Missing Values")
        lbl3.grid(row=2, column=0, padx = 10, pady=10)

        handleMissingVals = ["Do Nothing", "Replacing With Mean", "Replacing With Median", "Forward Fill","Drop Null Row"]
        combo2 = ttk.Combobox(wrapper2, values = handleMissingVals, height = 15,  width = 30)
        combo2.current(0)
        combo2.grid(row=2, column=1, padx=10, pady = 10)

        lbl4 = tk.Label(wrapper2, text = "Drop Check")
        lbl4.grid(row=3, column=0, padx = 10, pady=10)

        dropVals = ["Do Nothing", "Drop This Column"]
        combo3 = ttk.Combobox(wrapper2, values=dropVals, height = 15, width = 30)    
        combo3.current(0)    
        combo3.grid(row=3, column=1, padx = 10, pady=10)

        def processOption():
            data = self.cleanData(df, self.options)
            root.modifyData(data)
            print(data)
            pass
        btnOK = tk.Button(window, text = "OK", command= processOption)
        #btnOK.grid(column= 4, row = 5, padx = 10, pady = 10)
        btnOK.grid(column = 1, row = 2, padx = 10, pady = 10)

        window.title("CleaningBox")
        window.geometry("1000x330")
        window.resizable(False, False)
        window.mainloop()

    def cleanData(self, df, options):
        columnList = []
        for c in df.columns:
            if options[c][2] == "Drop This Column":
                pass
            else:
                columnList.append(c)
                df[c] = modType(df[c], options[c][0])
                handleMissingVal(df[c], options[c][1])
        print(df)
        data = df[columnList]
        print(columnList)
        return data
        #root.modifyData(data)

#mainframe의 df를 변경하는 함수를 만들어서 OK버튼의 command 함수에 넣으면 될듯?