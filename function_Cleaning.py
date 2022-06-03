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
    if option == "Do Nothing":
        return df
    elif option == "Replacing With Mean":
        df[column].fillna(column.mean(), inplace=True)
        return df
    elif option == "Replacing With Median":
        df[column].fillna(column.median(), inplace =True)
        return df
    elif option == "Forward Fill":
        df[column].ffill(axis = 0)
        return df
    elif option == "Drop Null Row":
        df[column].dropna()
        return df
    else:
        return df