from CleaningBox import CleaningBox
from function_mainFrame import *
from read_csv import get_datalist
import tkinter as tk
import tkinter.ttk as ttk
import pandas as pd



class mainFrame():
    def __init__(self):
        self.dataPath, self.dataList = get_datalist()
        self.data = None


        root = tk.Tk()
        root.title("Auto Preprocessing")
        root.geometry("600x280") #가로*세로 + (x좌표 + y 좌표)
        root.resizable(False, False) #x(너비), y(높이) 값 변경 불가 (창 크기 변경불가)
        wrapper = tk.LabelFrame(root, text="데이터 확인")
        wrapper.pack(padx = 10, pady = 5, fill = "both", expand= "yes")

        
        combobox = ttk.Combobox(wrapper, height = 5, width=60, values = self.dataList)
        combobox.current(0)
        combobox.grid(row = 0, column = 0, padx = 5, pady = 5)

        def selectData():
            data_name = combobox.get()
            data = pd.read_csv(data_name)
            df = pd.DataFrame(data)
            self.data = df

        btn_selectData = tk.Button(wrapper, text = "Select", command = selectData)
        btn_selectData.grid(row = 0, column = 1, padx = 5, pady = 5)

        btn_view = tk.Button(wrapper, text = "View", command = self.view) 
        btn_view.grid(row = 0, column = 2, padx = 5, pady = 5)

        def viewdetails():
            pass
        btn_viewdetails = tk.Button(wrapper, text = "Viewdetails", command = viewdetails)
        btn_viewdetails.grid(row = 1, column = 1, padx = 5, pady = 5)

        wrapper2 = tk.LabelFrame(root, text="데이터 처리")
        wrapper2.pack(padx = 10, pady = 5, fill = "both", expand= "yes")


        def btn_data_cleaning():
            #CleaningBox(self.data)
            pass
        btn_select_cleaning = tk.Button(wrapper2, text = "데이터 정제", command = btn_data_cleaning)
        btn_select_cleaning.grid(row = 0, column = 0, padx = 5, pady = 5)

        def btn_data_Transformation():
            pass
        btn_select_cleaning = tk.Button(wrapper2, text = "데이터 변환", command = btn_data_Transformation)
        btn_select_cleaning.grid(row = 0, column = 1, padx = 5, pady = 5)

        wrapper3 = tk.LabelFrame(root, text="데이터 저장")
        wrapper3.pack(padx = 10, pady = 5, fill = "both", expand= "yes")

        e = tk.Entry(wrapper3, width=30)
        e.grid(row = 0, column = 0, padx = 5, pady = 5)
        e.insert(0, "파일명을 입력하세요")
        def save():
            print(e.get())
        btn = tk.Button(wrapper3, text="Save", command=save)
        btn.grid(row = 0, column = 1, padx = 5, pady = 5)

        root.mainloop()
        pass

    def modifyData(self, data):
        self.data = data
    def view(self):
        tableView = tk.Tk()
        tableView.title("Data Head")
        tree = ttk.Treeview(tableView)
        tree.pack()
        cols = list(self.data.columns)
        tree["columns"] = cols
        for i in cols:
            tree.column(i, anchor="w")
            tree.heading(i, text=i, anchor='w')
        for index, row in self.data[:5].iterrows():
            tree.insert("",0,text=index,values=list(row))

mainFrame()