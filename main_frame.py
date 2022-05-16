from tkinter import *
import tkinter.ttk as ttk
from unicodedata import category
from read_csv import *
import pandas as pd
root = Tk()
root.title("Auto Preprocessing")
root.geometry("600x720") #가로*세로 + (x좌표 + y 좌표)
root.resizable(False, False) #x(너비), y(높이) 값 변경 불가 (창 크기 변경불가)

dataPath, file_list = get_datalist()
combobox = ttk.Combobox(root, height = 5, width=60, values = file_list)
combobox.current(0)
combobox.grid(row = 0, column = 0, padx = 10, pady = 10)

global data_name, data, df

def selectData():
    data_name = combobox.get()
    data = pd.read_csv(data_name)
    df = pd.DataFrame(data)
    cols = list(df.columns)
    return df
btn_selectData = Button(root, text = "Select", command = selectData)
btn_selectData.grid(row = 0, column = 1, padx = 5, pady = 5)

def printData():
    print(df)

btn_print = Button(root, text = "TEST", command = printData)
btn_print.grid(row = 2, column = 2, padx = 5, pady = 5)


def view():
    tableView = Tk()
    tree = ttk.Treeview(tableView)
    tree.pack()
    cols = list(df.columns)
    tree["columns"] = cols
    for i in cols:
        tree.column(i, anchor="w")
        tree.heading(i, text=i, anchor='w')

    for index, row in df.iterrows():
        tree.insert("",0,text=index,values=list(row))
btn_view = Button(root, text = "View", command = view)
btn_view.grid(row = 0, column = 2, padx = 5, pady = 5)

def viewdetails():
    pass
btn_viewdetails = Button(root, text = "Viewdetails", command = viewdetails)
btn_viewdetails.grid(row = 2, column = 1, padx = 5, pady = 5)


e = Entry(root, width=30)
e.grid(row = 3, column = 0, padx = 5, pady = 5)
e.insert(0, "파일명을 입력하세요")
def save():
    print(e.get())
btn = Button(root, text="Save", command=save)
btn.grid(row = 3, column = 1, padx = 5, pady = 5)

'''
def ToDataclean():    
    category_1 = ["결측치 처리", "이상치 처리"] 
    method_1 = ["해당 데이터 삭제", "평균값 적용"]
    method_2 = ["구간화 적용", "군집화 적용"]
    global my_category
    global my_method
    combobox_clean_category = ttk.Combobox(root, height=5, values=category_1)
    combobox_clean_category.pack()
    def category_clean_select() :
        my_category = combobox_clean_category.get()
        print(my_category)
        
        if(my_category == "결측치 처리") :
            method_missing_value_select()  
        if(my_category == "이상치 처리") :
            method_noisy_value_select()
        else :
            pass
    def method_missing_value_select():
        combobox_clean_method = ttk.Combobox(root, height=5, values=method_1)
        combobox_clean_category.destroy()
        category_btn.destroy()
        combobox_clean_method.pack()
        method_btn_1 = Button(root, text = "Select" )#, command = 결측치 처리 함수 연결)
        method_btn_1.pack()
    def method_noisy_value_select():
        combobox_clean_method = ttk.Combobox(root, height=5, values=method_2)
        combobox_clean_category.destroy()
        category_btn.destroy()
        combobox_clean_method.pack()
        method_btn_2 = Button(root, text = "Select") #, command = 이상치 처리 함수 연결)
        method_btn_2.pack()
    
    category_btn = Button(root, text = "Select", command = category_clean_select)
    category_btn.pack()
    
def ToDataintergration() :
    nextbtn = Button(root, text = "Next", command = ToDataReduction)
    print("ToDataintergration")
    
def ToDataReduction():
    nextbtn = Button(root, text = "Next", command = ToDatatransformation)
    print("ToDataReduction")
def ToDatatransformation():
    nextbtn = Button(root, text = "Next", command = ToDataintergration)
    print("ToDatatransformation")
def show_table(data):
        global df
        print(data_name)
        
#show_table(data)
#page1
'''

root.mainloop()
