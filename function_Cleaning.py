import pandas as pd




def modType(column, option):
    if option == "Default":
        return column

    elif option == "Numeric":
        return pd.to_numeric(column)

    elif option == "Categorical":
        return column.astype('category')

    elif option  == "Datetime":
        return pd.to_datetime(column)
    


def handleMissingVal(df, column, option):
    print(column)
    if option == "Do Nothing":
        return df
    elif option == "Replacing With Mean":
        df[column].fillna(df[column].mean(), inplace=True)
        return df
    elif option == "Replacing With Median":
        df[column].fillna(df[column].median(), inplace =True)
        return df
    elif option == "Forward Fill":
        df[column].ffill(axis = 0)
        return df
    elif option == "Drop Null Row":
        df.dropna(axis= 0, how='any',subset = [column] ,inplace = True)        
        return df
    else:
        return df

import tkinter.messagebox as msgbox

def secces():
    msgbox.showinfo("알림", "정상적으로 처리 되었습니다.")
def warn():
    msgbox.showwarning("경고", "오류가 발생했습니다.")