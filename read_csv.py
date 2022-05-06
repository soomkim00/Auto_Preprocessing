import pandas as pd
import os

#출력옵션
# pd.options.display.float_format = '{:,.2f}'.format #소숫점 자릿수
# pd.set_option('display.width', 85)
# pd.set_option('display.max_columns', 8)


def get_datalist():
    path = os.getcwd() #현재 폴더의 경로
    data_path = path + "\data"
    print(data_path)
    os.chdir(data_path) #현재 폴더의 /data로 디렉토리 변경
    data_list = os.listdir() #/data에 들어있는 파일명 출력
    print(data_path)
    return data_path, data_list


def read_csv(data_name):
    data = pd.read_csv('data/'+data_name)
    return data


def get_col_list(df):
    col_list = df.columns.values.tolist()
    return col_list


def select_col(df, col_list):
    return df[col_list]


