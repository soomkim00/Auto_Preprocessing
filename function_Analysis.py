import pandas as pd
import missingno as msno
import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

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

def getDataTypes(df):
    types = {}
    for i in df.columns:
        types[i] = df[i].dtype
    return types
    