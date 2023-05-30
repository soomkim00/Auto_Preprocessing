import pandas as pd
import missingno as msno
import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
from matplotlib.figure import Figure
import tkinter.ttk as ttk

def getfirstlook(df, nrows=5, uniqueids=None):
    out = {}
    #out['head'] = df.head(nrows)
    out['dtypes\n'] = df.dtypes
    out['nrows'] = df.shape[0]
    out['ncols'] = df.shape[1]
    out['index'] = df.index
    if (uniqueids is not None):
        out['uniqueids'] = df['uniqueids'].nunique()
    return out

def displaydict(dicttodisplay):
    s = ""
    for x in dicttodisplay.items():
        s += ': '.join(map(str, x))
        s += '\n'
    return s

def gettots(df):
    out = {}
    out['mins'] = df.min()
    out['per15'] = df.quantile(0.15)
    out['qr1'] = df.quantile(0.25)
    out['med'] = df.median()
    out['qr3'] = df.quantile(0.75)
    out['per85'] = df.quantile(0.85)
    out['max'] = df.max()
    out['count'] = df.count()
    out['mean'] = df.mean()
    out['iqr'] = out['qr3'] - out['qr1']
    return pd.DataFrame(out)


def filterNumeric(df):
    numerics = ['int16', 'int32', 'int64', 'float32', 'float64']
    df = df.select_dtypes(include=numerics)
    return df


def show_msno_matrix(df):
    window = tk.Tk()  #Tk 객체 생성. 기본 윈도우 객체
    fig = msno.matrix(df).get_figure()
    chart_type = FigureCanvasTkAgg(fig, master=window)
    
    
    chart_type.draw()
    chart_type.get_tk_widget().pack()
    window.mainloop()

def show_plotbox(df):
    window = tk.Tk()  #Tk 객체 생성. 기본 윈도우 객체
    col_numeric = list(filterNumeric(df).columns)
    mycombo = ttk.Combobox(window, height = 15, values = col_numeric, width=30)
    mycombo.current(0)
    mycombo.pack()
    myFrame = tk.Frame(window)
    myFrame.pack()
    def lookupColumn():
        colName = mycombo.get()
        draw = drawBoxPlot(colName)

    btnSelectCol = tk.Button(window, text="Select", command=lookupColumn)
    btnSelectCol.pack()


    def drawBoxPlot(i):
        
        fig = Figure(figsize=(3, 3), dpi=200)
        plt = fig.add_subplot()
        box_plot_data = (df[i])

        plt.boxplot(box_plot_data)
        plt.set_title(i)

        canvas = FigureCanvasTkAgg(fig, master=myFrame)
        canvas.draw()
        bplot = canvas.get_tk_widget()
        bplot.delete('all')
        bplot.grid(column=0, row=0)
    
    window.mainloop()

def filterNumeric(df_input):
    numerics = ['int16', 'int32', 'int64', 'float32', 'float64']
    result = df_input.select_dtypes(include=numerics)
    return result

def getDataTypes(df):
    types = {}
    for i in df.columns:
        types[i] = df[i].dtype
    return types
    

import tkinter.messagebox as msgbox

def secces():
    msgbox.showinfo("알림", "정상적으로 처리 되었습니다.")
def warn():
    msgbox.showwarning("경고", "오류가 발생했습니다.")