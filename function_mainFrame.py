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


