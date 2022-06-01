from class_mainFrame import *
import pandas as pd


def recommend_cleaning(data):
    cols = data.columns
    for i in cols:
        i.count(isnumeric())