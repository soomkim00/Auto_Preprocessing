from class_mainFrame import *
import pandas as pd

def count_numeric(col):
    res = 0
    for i in col:
        if str(i).isnumeric():
            res += 1
    return res
def recommend_cleaning(_data):
    data = _data
    cols = data.columns
    for i in cols:
        n_numeric = count_numeric(data[i])
        n_null = data[i].isnull().sum(axis=0)/len(data[i])
        if n_numeric / len(data[i]) > 0.9:
            pd.to_numeric(data[i])
        if  n_null/len(data[i]) < 0.1:
            data[i].dropna()
        elif n_null/len(data[i]) > 0.1:
            data[i].fillna(data[i].mean(), inplace=True)
    return data

import tkinter.messagebox as msgbox

def secces():
    msgbox.showinfo("알림", "정상적으로 처리 되었습니다.")
def warn():
    msgbox.showwarning("경고", "오류가 발생했습니다.")