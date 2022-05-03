from tkinter import *
import tkinter.ttk as ttk
from read_csv import *

root = Tk()
root.title("Auto Preprocessing")
root.geometry("600x720") #가로*세로 + (x좌표 + y 좌표)
root.resizable(False, False) #x(너비), y(높이) 값 변경 불가 (창 크기 변경불가)


dataPath, file_list = get_datalist()
combobox = ttk.Combobox(root, height = 5, values = file_list)
combobox.current(0)
combobox.pack()
def getDataname():
    global data_name, data, df
    data_name = combobox.get()
    data = pd.read_csv(data_name)
    df = pd.DataFrame(data)
    cols = list(df.columns)
    tree = ttk.Treeview(root)
    tree.pack()
    tree["columns"] = cols
    for i in cols:
        tree.column(i, anchor="w")
        tree.heading(i, text=i, anchor='w')

    for index, row in df.iterrows():
        tree.insert("",0,text=index,values=list(row))


selectData = Button(root, text = "select", command = getDataname)
selectData.pack()





def show_table(data):
        global df
        print(data_name)
        
#show_table(data)
root.mainloop()

