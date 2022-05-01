import pandas as pd
import matplotlib.pyplot as plt
import os

#출력옵션
pd.options.display.float_format = '{:,.2f}'.format #소숫점 자릿수
pd.set_option('display.width', 85)
pd.set_option('display.max_columns', 8)

def show_datalist():
    path = os.getcwd() #현재 폴더의 경로
    data_path = path + "\data"
    os.chdir(data_path) #현재 폴더의 /data로 디렉토리 변경
    print(os.listdir()) #/data에 들어있는 파일명 출력
    os.chdir(path)

def read_csv():
    path = os.getcwd() #현재 폴더의 경로
    data_path = path + "\data"
    data_name = "\landtempssample.csv"
    data = pd.read_csv(data_path + data_name)
    return data



data = read_csv()
df = pd.DataFrame(data)
print(df.head())
col_list = df.columns.values.tolist()
print(col_list)