import tkinter as tk
import tkinter.ttk as ttk
from numpy import NaN
import pandas as pd
from function_Cleaning import * 
from class_mainFrame import *


class CleaningBox():
    def __init__(self, root):
        df = root.getData()
        window =  tk.Tk()
        self.options = {}
        amount_missing = tk.StringVar()
        cols = ["Column Not Selected "] + list(df.columns)
        for c in cols:
            self.options[c] = ['Default', 'Do Nothing', 1]


        wrapper = tk.LabelFrame(window, text="Select Column")
        wrapper.pack(padx = 10, pady = 5, fill = "both", expand= "yes")
        wrapper2 = tk.LabelFrame(window, text="Select Options")
        wrapper2.pack(padx = 10, pady = 10, fill = "both", expand= "yes")


        label1 = tk.Label(wrapper, text = "Column")
        label1.grid(row=0, column=0, padx = 10, pady = 10)
        
        mycombo = ttk.Combobox(wrapper, height = 15, values = cols, width=30)
        mycombo.current(0)
        mycombo.grid(row = 0, column = 1)
        
        def lookupColumn():
            colName = mycombo.get()
            amount_missing = df[colName].isnull().sum(axis=0)
            lblMissingValues.configure(text = amount_missing)
            combo1.current(0)
            combo2.current(0)
            combo3.current(0)

        def colOptions():
            colName = mycombo.get()
            self.options[colName] = [combo1.get(), combo2.get(), combo3.get()]
            print(self.options[colName])

        btnSelectCol = tk.Button(wrapper, text="Select", command=lookupColumn)
        btnSaveOptions = tk.Button(wrapper2, text="Save Column Options", command=colOptions)

        btnSelectCol.grid(row = 0, column=2, padx=10, pady=10)
        btnSaveOptions.grid(row = 3, column=4, padx=10, pady=10)


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

        handleMissingVals = ["Do Nothing", "Replacing With Mean", "Replacing With Median", "Others..."]
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
        btnOK.pack()

        window.title("CleaningBox")
        window.geometry("720x330")
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