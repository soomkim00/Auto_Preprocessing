from sklearn.datasets import load_iris
import pandas as pd
from sklearn.preprocessing import MaxAbsScaler, MinMaxScaler, RobustScaler
from sklearn.preprocessing import StandardScaler
import tkinter.messagebox as msgbox

def def_StandardScaler(df_input, column):
    scaler = StandardScaler()
    result = scaler.fit_transform(df_input[['{}'.format(column)]])
    return result

def def_MinMaxScaler(df_input, column):
    scaler = MinMaxScaler()
    result = scaler.fit_transform(df_input[['{}'.format(column)]])
    return result

def def_MaxAbsScaler(df_input, column):
    scaler = MaxAbsScaler()
    result = scaler.fit_transform(df_input[['{}'.format(column)]])
    return result

def def_RobustScaler(df_input, column):
    scaler = RobustScaler()
    result = scaler.fit_transform(df_input[['{}'.format(column)]])
    return result

def filterNumeric(df_input):
    numerics = ['int16', 'int32', 'int64', 'float32', 'float64']
    result = df_input.select_dtypes(include=numerics)
    return result

def secces():
    msgbox.showinfo("알림", "정상적으로 처리 되었습니다.")
def warn():
    msgbox.showwarning("경고", "오류가 발생했습니다.")