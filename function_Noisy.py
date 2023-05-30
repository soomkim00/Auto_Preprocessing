import pandas as pd
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import RobustScaler
from matplotlib import *
import numpy as np

def outlier_remove(df_input, column):
  # target 값과 상관관계가 높은 열을 우선적으로 진행
  quantile_25 = np.percentile(df_input[column].values, 25)
  quantile_75 = np.percentile(df_input[column].values, 75)
  weight=1.5
  IQR = quantile_75 - quantile_25
  IQR_weight = IQR*weight
  
  lowest = quantile_25 - IQR_weight
  highest = quantile_75 + IQR_weight
  
  outlier_idx = df_input[column][ (df_input[column] < lowest) | (df_input[column] > highest) ].index
  return outlier_idx


def Isolation_Forest(df_input, column):
    clf = IsolationForest(max_samples=1000, random_state=1)
    df = df_input[['{}'.format(column)]]
    # fit 함수를 이용하여, 데이터셋을 학습시킨다. df는 dataframe의 이름이다.
    clf.fit(df)

    # predict 함수를 이용하여, outlier를 판별해 준다. 0과 1로 이루어진 Series형태의 데이터가 나온다.
    y_pred_outliers = clf.predict(df)

    # 원래의 dataframe에 붙이기. 데이터가 0인 것이 outlier이기 때문에, 0인 것을 제거하면 outlier가 제거된  dataframe을 얻을 수 있다.
    out = pd.DataFrame(y_pred_outliers)
    out = out.rename(columns={0: "out"})
    race_an1 = pd.concat([df, out], 1)
    result = race_an1.drop('out',axis=1)    
    print (result)
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