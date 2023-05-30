import pandas as pd
import tkinter as tk
import tkinter.ttk as ttk
import os

def get_datalist():
    path = os.getcwd() #현재 폴더의 경로
    data_path = path + "\data"
    print(data_path)
    os.chdir(data_path) #현재 폴더의 /data로 디렉토리 변경
    data_list = os.listdir() #/data에 들어있는 파일명 출력
    print(data_path)
    return data_path, data_list

def dataToCsv(data, path):
    data = pd.DataFrame(data)
    data.to_csv(path+".csv")


def addDataStack(stack, data):
    if len(stack) < 3:
        stack.append(data)
    
    else:
        stack.pop(0)
        stack.append(data)
    return stack

import tkinter.messagebox as msgbox

def secces():
    msgbox.showinfo("알림", "정상적으로 처리 되었습니다.")
def warn():
    msgbox.showwarning("경고", "오류가 발생했습니다.")