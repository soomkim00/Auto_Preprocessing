from class_mainFrame import *
import pandas as pd

def count_numeric(col):
    res = 0
    for i in col:
        if i.isnumeric():
            res += 1
    return res
def recommend_cleaning(data):
    cols = data.columns
    for i in cols:
        n_numeric = count_numeric(data[i])
        n_null = data[i].isnull().sum(axis=0)/len(data[i])
        if n_numeric / len(data[i]) > 0.9:
            data[i].to_numeric()
        if  n_null/len(data[i]) < 0.1:
            data[i].dropna()
        elif n_null/len(data[i]) > 0.3:
            data[i].fillna(data[i].mean(), inplace=True)
