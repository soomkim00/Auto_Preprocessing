import tkinter as tk
import tkinter.ttk as ttk
import pandas as pd
from function_Reduction import *
from class_mainFrame import *

class ReductionBox():
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
  
        def selectcolumn_reduct():
            global select_reduct_column
            select_reduct_column = mycombo.get()
            print(select_reduct_column)
        btn_selectData = tk.Button(wrapper, text = "Select", command = selectcolumn_reduct)
        btn_selectData.grid(row = 0, column = 2, padx = 5, pady = 5)

        redction_method = ["데이터 범주화"]

        label2 = tk.Label(wrapper2, text = "축소 방법 :")
        label2.grid(row=0, column=0, padx = 10, pady = 10)
        
        mycombo2 = ttk.Combobox(wrapper2, height = 15, values = redction_method, width=30)
        mycombo2.current(0)
        mycombo2.grid(row = 0, column = 1)     


        lbl1 = tk.Label(wrapper2, text = "데이터 범주의 개수")
        lbl1.grid(row=0, column=0, padx = 10, pady=10)
        entry_reduction1 = tk.Entry()
        datatypes = ["Default","Numeric", "Categorical", "Datetime"]
        combo1 = ttk.Combobox(wrapper2, height = 15, values = datatypes, width = 30)
        combo1.current(0)
        combo1.grid(row=0, column=1, padx=10, pady=10)

        def select_method_reduction():
            global select_reduction_method
            select_reduction_method = mycombo2.get()
            if(select_reduction_method=="데이터 범주화"):
                pass
                #~~~.gird
            print(select_reduction_method)

        btn_selectData = tk.Button(wrapper2, text = "Select", command = select_method_reduction)
        btn_selectData.grid(row = 0, column = 2, padx = 5, pady = 5)

        def reduction():
            if(select_reduction_method=="데이터 범주화"):

                df['{}'.format(select_reduct_column)] = def_StandardScaler(df, select_reduct_column)
                print(df)
            else: pass
        btn_selectData = tk.Button(wrapper2, text = "축소", command = reduction)
        btn_selectData.grid(row = 1, column = 6, padx = 5, pady = 5)
        
        window.title("ReductionBox")
        window.geometry("720x720")
        window.resizable(False, False)
        window.mainloop()
