from tkinter import *
import tkinter.ttk as ttk
from read_csv import *

root = Tk()
root.title("Auto Preprocessing")
root.geometry("1080x720") #가로*세로 + (x좌표 + y 좌표)
root.resizable(False, False) #x(너비), y(높이) 값 변경 불가 (창 크기 변경불가)

btn = Button(root, text = "hello")
btn.pack()

print('path : ', os.getcwd())
file_list = get_datalist()
print(file_list)
combobox = ttk.Combobox(root, height = 5, values = file_list)
combobox.pack()
def btncmd():
    data_name = combobox.get()
    print(combobox.get()) #선택된 값 표시
    return data_name
btn = Button(root, text = "select", command = btncmd)
btn.pack()
root.mainloop()

