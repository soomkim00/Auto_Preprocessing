from tkinter import *
import tkinter.ttk as ttk
from unicodedata import category
from read_csv import *
import pandas as pd
root = Tk()
root.title("Auto Preprocessing")
root.geometry("600x720") #가로*세로 + (x좌표 + y 좌표)
root.resizable(False, False) #x(너비), y(높이) 값 변경 불가 (창 크기 변경불가)


wrapper = LabelFrame(root, text="데이터 확인")
wrapper.grid(row = 0, column = 0, padx = 5, pady = 5)

dataPath, file_list = get_datalist()
combobox = ttk.Combobox(wrapper, height = 5, width=60, values = file_list)
combobox.current(0)
combobox.grid(row = 0, column = 0, padx = 5, pady = 5)


def selectData():
    global data_name, data, df
    data_name = combobox.get()
    data = pd.read_csv(data_name)
    df = pd.DataFrame(data)
    cols = list(df.columns)
    btn_selectData = Button(wrapper, text = "Select", command = selectData)
    btn_selectData.grid(row = 0, column = 1, padx = 5, pady = 5)

    return df

def view():
    tableView = Tk()
    tableView.title("Data Head")
    tree = ttk.Treeview(tableView)
    tree.pack()
    cols = list(df.columns)
    tree["columns"] = cols
    for i in cols:
        tree.column(i, anchor="w")
        tree.heading(i, text=i, anchor='w')
    for index, row in df[:5].iterrows():
        tree.insert("",0,text=index,values=list(row))
        
btn_view = Button(wrapper, text = "View", command = view)
btn_view.grid(row = 0, column = 2, padx = 5, pady = 5)

def viewdetails():
    pass
btn_viewdetails = Button(wrapper, text = "Viewdetails", command = viewdetails)
btn_viewdetails.grid(row = 1, column = 1, padx = 5, pady = 5)

wrapper2 = LabelFrame(root, text="데이터 처리")
wrapper2.grid(row = 1, column = 0,padx = 5, pady = 5)

e = Entry(root, width=30)
e.grid(row = 3, column = 0, padx = 5, pady = 5)
e.insert(0, "파일명을 입력하세요")
def save():
    print(e.get())
btn = Button(root, text="Save", command=save)
btn.grid(row = 3, column = 1, padx = 5, pady = 5)

def btn_data_cleaning():
    pass

btn_select_cleaning = Button(wrapper2, text = "데이터 정제", command = btn_data_cleaning)
btn_select_cleaning.grid(row = 0, column = 0, padx = 5, pady = 5)


wrapper3 = LabelFrame(root, text="데이터 저장")
wrapper3.grid(row = 2, column = 0,padx = 5, pady = 5)

e = Entry(wrapper3, width=30)
e.grid(row = 0, column = 0, padx = 5, pady = 5)
e.insert(0, "파일명을 입력하세요")
def save():
    print(e.get())
btn = Button(wrapper3, text="Save", command=save)
btn.grid(row = 0, column = 1, padx = 5, pady = 5)
def btn_data_Transformation():
    pass

btn_select_transformation = Button(wrapper2, text = "데이터 변환", command = btn_data_Transformation)
btn_select_transformation.grid(row = 0, column = 1, padx = 5, pady = 5)



wrapper3 = LabelFrame(root, text="데이터 저장")
wrapper3.grid(row = 2, column = 0,padx = 5, pady = 5)

e = Entry(wrapper3, width=30)
e.grid(row = 0, column = 0, padx = 5, pady = 5)
e.insert(0, "파일명을 입력하세요")
def save():
    print(e.get())
btn = Button(wrapper3, text="Save", command=save)
btn.grid(row = 0, column = 1, padx = 5, pady = 5)
