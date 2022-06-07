
import pandas as pd


def def_data_divide(df_input, column, num_divide, bins, labels):
    result = pd.cut(df_input['{}'.format(column)], bins, right=True, labels=labels)
    return result

def filterNumeric(df_input):
    numerics = ['int16', 'int32', 'int64', 'float32', 'float64']
    result = df_input.select_dtypes(include=numerics)
    return result

import tkinter.messagebox as msgbox

def secces():
    msgbox.showinfo("알림", "정상적으로 처리 되었습니다.")
def warn():
    msgbox.showwarning("경고", "오류가 발생했습니다.")