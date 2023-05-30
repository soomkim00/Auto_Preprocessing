import tkinter as tk
import tkinter.ttk as ttk
import pandas as pd
from function_Reduction import *
from class_mainFrame import *
import tkinter.messagebox as msgbox
import numpy as np
import datetime as dt

class ReductionBox():
    def __init__(self, root):
        df = root.getData()
        window =  tk.Tk()
        self.options = {}
        self.log = []

        cols = ["Column Not Selected "] + list(filterNumeric(df).columns)
        for c in cols:
            self.options[c] = ['Default','column','num_divide','list_dividePoint','list_divideName']
        
        

        wrapper = tk.LabelFrame(window, text="Select Column")
        wrapper.grid(row=0, column = 0, rowspan=2, padx=10, pady=10, sticky="n", ipady = 30)
        wrapper2 = tk.LabelFrame(window, text="Select Options")
        wrapper2.grid(row=1, column = 0, rowspan=2, padx=10, pady=10, sticky="n", ipady = 30)
        wrapper3 = tk.LabelFrame(window, text= "Selected Options", relief="flat", bd=2, width=1000)
        wrapper3.grid(row=0, column = 1, rowspan=2, padx=10, pady=10, sticky="n", ipady = 30)
        self.treeview=ttk.Treeview(wrapper3, column = ["Time", "Column", "Num_divide","List_DividePoint","List_DivideName"])
        self.treeview["columns"] = ["Time", "Column", "Num_divide","List_DividePoint","List_DivideName"]
        self.treeview.column("#0", width=33)
        self.treeview.heading("#0", text="num")
        for i in range(len(self.treeview["columns"])):
            self.treeview.heading(self.treeview["columns"][i], text = self.treeview["columns"][i], anchor="w")
        self.treeview.column("#1", width = 109)
        self.treeview.column("#2", width = 100)
        self.treeview.column("#3", width = 200)
        self.treeview.column("#4", width = 200)
        self.treeview.pack()
        def insertLog(option):
            self.treeview.insert("", "end", text = len(self.log), values = option, iid=len(self.log))

        label1 = tk.Label(wrapper, text = "Column   :")
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


        lbl1 = tk.Label(wrapper2, text = "데이터 범주의 개수   :")
        lbl1.grid(row=0, column=0, padx = 10, pady=10)
        entry1 = tk.Entry(wrapper2, text="개수를 입력하세요.")
        entry1.grid(row=0, column=1, padx = 10, pady=10)
        def divide_num_get():
            global num_divide
            num_divide = entry1.get()
            #lbl2_1 = tk.Label(wrapper2, text ="기준값을 작은 순서대로"+("{}".format(str(num_divide+1)))+"개 입력하세요.")
            #lbl2_1.grid(row=1, column=3, padx =10, pady=10)
            #lbl3_1 = tk.Label(wrapper2, text ="범주의 이름을 작은 순서대로"+("{}".format(str(num_divide)))+"개 입력하세요.")
            #lbl3_1.grid(row=2, column=3, padx =10, pady=10)
            print(num_divide)
        btn_selectmethod1 = tk.Button(wrapper2, text = "Enter", command = divide_num_get)
        btn_selectmethod1.grid(row = 0, column = 2, padx = 5, pady = 5)     

        lbl2 = tk.Label(wrapper2, text = "데이터 범주의 기준값   :")
        lbl2.grid(row=1, column=0, padx = 10, pady=10)
        entry2 = tk.Entry(wrapper2)
        entry2.grid(row=1, column=1, padx = 10, pady=10)

        bins= []
        def divide_point_get():
            a = (entry2.get()).split()
            for i in range (len(a)):
                a[i] = float(a[i])
            for i in range (len(a)):
                bins.insert(i, a[i])
            print(a)
            print(bins)

        btn_selectmethod2 = tk.Button(wrapper2, text = "Enter", command = divide_point_get)
        btn_selectmethod2.grid(row = 1, column = 2, padx = 5, pady = 5)   

        lbl3 = tk.Label(wrapper2, text = "데이터 범주의 이름   :")
        lbl3.grid(row=2, column=0, padx = 10, pady=10)
        entry3 = tk.Entry(wrapper2)
        entry3.grid(row=2, column=1, padx = 10, pady=10)

        lbl3_2 = tk.Label(wrapper2, text ="공백(space)를 기준으로 값이 적용됩니다.")
        lbl3_2.grid(row=3, column=3, padx =10, pady=10)
        labels = []
        def divide_name_get():
            a = (entry3.get()).split()
            for i in range (len(a)):
                labels.insert(i, a[i])
            print(labels)

        btn_selectmethod3 = tk.Button(wrapper2, text = "Enter", command = divide_name_get)
        btn_selectmethod3.grid(row = 2, column = 2, padx = 5, pady = 5) 

        def reduction():
            try:
                df['{}'.format(select_reduct_column)] = def_data_divide(df, select_reduct_column,num_divide,bins,labels)
                print(df)
                root.appendLog(self.processLog())
                root.pushStack(df)
                secces()
            except:
                warn()
        
        btn_selectData = tk.Button(window, text = "OK", command = reduction)
        btn_selectData.grid(column = 1, row = 2, padx = 10, pady = 10)

        def colOptions():
            colName = mycombo.get()
            print(num_divide, bins, labels)
            self.options[colName] = [num_divide, bins, labels]
            insertLog((dt.datetime.now(), colName, num_divide, bins, labels))
            self.log.append((dt.datetime.now(), colName, num_divide, bins, labels))
            
        btnSaveOptions = tk.Button(wrapper2, text="Save Column Options", command=colOptions)
        btnSaveOptions.grid(row = 4, column=0, padx=10, pady=10)

        def reset_Options():
            num_divide = 0
            bins.clear()
            labels.clear()


        btnresetOptions = tk.Button(wrapper2, text="Reset Options", command=reset_Options)
        btnresetOptions.grid(row = 4, column=1, padx=10, pady=10)
        def info():
            msgbox.showinfo("알림", "정상적으로 처리 되었습니다.")
        def warn():
            msgbox.showwarning("경고", "오류가 발생했습니다.")

        window.title("ReductionBox")
        window.geometry("1500x400")
        window.resizable(False, False)
        window.mainloop()


    def processLog(self):
        log = []
        for i in self.options.keys():
            defaultOption = ['Default','column','num_divide','list_dividePoint','list_divideName']
            if self.options[i] != defaultOption:
                log.append([dt.datetime.now(), i, self.options[i]])
        return log

