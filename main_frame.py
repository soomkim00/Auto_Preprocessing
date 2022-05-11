from tkinter import *
import tkinter.ttk as ttk
from unicodedata import category
from read_csv import *

import tkinter as tk
from tkinter import ttk

LARGEFONT =("Verdana", 35)


class tkinterApp(tk.Tk):
     
    # __init__ function for class tkinterApp
    def __init__(self, *args, **kwargs):
        
         
        # __init__ function for class Tk
        tk.Tk.__init__(self, *args, **kwargs)
         
        # creating a container
        container = tk.Frame(self) 
        container.pack(side = "top", fill = "both", expand = True)
  
        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)
  
        # initializing frames to an empty array
        self.frames = {} 
  
        # iterating through a tuple consisting
        # of the different page layouts
        for F in (StartPage, Page1, Page2, Page3, Page4, Page5, Page6):
  
            frame = F(container, self)
  
            # initializing frame of that object from
            # startpage, page1, page2 respectively with
            # for loop
            self.frames[F] = frame
  
            frame.grid(row = 0, column = 0, sticky ="nsew")
  
        self.show_frame(StartPage)
  
    # to display the current frame passed as
    # parameter
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()
  
# first window frame startpage
  
class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # label of frame Layout 2
        label = ttk.Label(self, text ="Auto Preprocessing", font = LARGEFONT)

        # putting the grid in its place by using
        # grid
        label.grid(row = 0, column = 4, padx = 10, pady = 10)
  
        button1 = ttk.Button(self, text ="Prev",
        command = lambda : controller.show_frame(Page1))
     
        # putting the button in its place by
        # using grid
        button1.grid(row = 7, column = 1, padx = 10, pady = 10)
  
        ## button to show frame 2 with text layout2
        button2 = ttk.Button(self, text ="Next",
        command = lambda : controller.show_frame(Page1))
     
        # putting the button in its place by
        # using grid
        button2.grid(row = 7, column = 7, padx = 10, pady = 10)

        dataPath, file_list = get_datalist()
        combobox = ttk.Combobox(self, height = 5, values = file_list)
        combobox.current(0)
        combobox.grid(row = 2, column = 2)
        def getDataname():
            global data_name, data, df
            data_name = combobox.get()
            data = pd.read_csv(data_name)
            df = pd.DataFrame(data)
            cols = list(df.columns)
            tableView = Tk()
            tree = ttk.Treeview(tableView)
            tree.pack()
            tree["columns"] = cols
            for i in cols:
                tree.column(i, anchor="w")
                tree.heading(i, text=i, anchor='w')

            for index, row in df.iterrows():
                tree.insert("",0,text=index,values=list(row))


        selectData = Button(self, text = "Select", command = getDataname)
        selectData.grid(row = 3, column = 2)




 
# second window frame page1
class Page1(tk.Frame):
     
    def __init__(self, parent, controller):
         
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text ="Data cleaning", font = LARGEFONT)
        label.grid(row = 0, column = 4, padx = 10, pady = 10)
  
        # button to show frame 2 with text
        # layout2
        button1 = ttk.Button(self, text ="Prev",
                            command = lambda : controller.show_frame(StartPage))
     
        # putting the button in its place
        # by using grid
        button1.grid(row = 7, column = 1, padx = 10, pady = 10)
  
        # button to show frame 2 with text
        # layout2
        button2 = ttk.Button(self, text ="Next",
                            command = lambda : controller.show_frame(Page2))
        button2.grid(row = 7, column = 7, padx = 10, pady = 10)
       
        global category_1
        global method_1
        
        category_1 = ["결측치 처리", "이상치 처리"] 
        method_1 = ["해당 데이터 삭제", "평균값 적용"]


        combobox_category = ttk.Combobox(self, height=5, values=category_1)
        combobox_category.grid(row = 2, column = 2, padx = 10, pady = 10)

        def combobox_get() :
            my_catagory = combobox_category.get()    
        
        button3 = ttk.Button(self, text ="Select", command = combobox_get)
        button3.grid(row = 7, column = 4, padx = 10, pady = 10)





        
        
  
  
  
  
# third window frame page2
class Page2(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text ="Page 2", font = LARGEFONT)
        label.grid(row = 0, column = 4, padx = 10, pady = 10)
  
        button1 = ttk.Button(self, text ="Prev",
                            command = lambda : controller.show_frame(Page1))
        button1.grid(row = 7, column = 1, padx = 10, pady = 10)
        button2 = ttk.Button(self, text ="Next",
                            command = lambda : controller.show_frame(Page3))
        button2.grid(row = 7, column = 4, padx = 10, pady = 10)

        button3 = ttk.Button(self, text ="Select",
                            command = lambda : controller.show_frame(Page3))
        button3.grid(row = 7, column = 4, padx = 10, pady = 10)
        

  
class Page3(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text ="Page 3", font = LARGEFONT)
        label.grid(row = 0, column = 4, padx = 10, pady = 10)
  
        # button to show frame 2 with text
        # layout2
        button1 = ttk.Button(self, text ="Prev",
                            command = lambda : controller.show_frame(Page2))
     
        # putting the button in its place by
        # using grid
        button1.grid(row = 7, column = 1, padx = 10, pady = 10)
  
        # button to show frame 3 with text
        # layout3
        button2 = ttk.Button(self, text ="Next",
                            command = lambda : controller.show_frame(Page4))
     
        # putting the button in its place by
        # using grid
        button2.grid(row = 7, column = 7, padx = 10, pady = 10)

class Page4(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text ="Page 4", font = LARGEFONT)
        label.grid(row = 0, column = 4, padx = 10, pady = 10)
  
        # button to show frame 2 with text
        # layout2
        button1 = ttk.Button(self, text ="Prev",
                            command = lambda : controller.show_frame(Page3))
     
        # putting the button in its place by
        # using grid
        button1.grid(row = 7, column = 1, padx = 10, pady = 10)
  
        # button to show frame 3 with text
        # layout3
        button2 = ttk.Button(self, text ="Next",
                            command = lambda : controller.show_frame(Page5))
     
        # putting the button in its place by
        # using grid
        button2.grid(row = 7, column = 7, padx = 10, pady = 10)

class Page5(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text ="Page 5", font = LARGEFONT)
        label.grid(row = 0, column = 4, padx = 10, pady = 10)
  
        # button to show frame 2 with text
        # layout2
        button1 = ttk.Button(self, text ="Prev",
                            command = lambda : controller.show_frame(Page4))
     
        # putting the button in its place by
        # using grid
        button1.grid(row = 7, column = 1, padx = 10, pady = 10)
  
        # button to show frame 3 with text
        # layout3
        button2 = ttk.Button(self, text ="Next",
                            command = lambda : controller.show_frame(Page6))
     
        # putting the button in its place by
        # using grid
        button2.grid(row = 7, column = 7, padx = 10, pady = 10)

class Page6(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text ="Page 6", font = LARGEFONT)
        label.grid(row = 0, column = 4, padx = 10, pady = 10)
  
        # button to show frame 2 with text
        # layout2
        button1 = ttk.Button(self, text ="Prev",
                            command = lambda : controller.show_frame(Page5))
     
        # putting the button in its place by
        # using grid
        button1.grid(row = 7, column = 1, padx = 10, pady = 10)
  
        # button to show frame 3 with text
        # layout3
        button2 = ttk.Button(self, text ="Next",
                            command = lambda : controller.show_frame(StartPage))
     
        # putting the button in its place by
        # using grid
        button2.grid(row = 7, column = 7, padx = 10, pady = 10)
# Driver Code


app = tkinterApp()

app.mainloop()



"""
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
    tableView = Tk()
    tree = ttk.Treeview(tableView)
    tree.pack()
    tree["columns"] = cols
    for i in cols:
        tree.column(i, anchor="w")
        tree.heading(i, text=i, anchor='w')

    for index, row in df.iterrows():
        tree.insert("",0,text=index,values=list(row))


selectData = Button(root, text = "Select", command = getDataname)
selectData.pack()


def ToDataclean():
    

    nextbtn.destroy()
    selectData.destroy()
    combobox.destroy()
    
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

nextbtn = Button(root, text = "Next", command = ToDataclean)
nextbtn.pack()




def show_table(data):
        global df
        print(data_name)
        
#show_table(data)
#page1


root.mainloop()
"""
