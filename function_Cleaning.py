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


def handleMissingVal(column, option):
    if option == "Do Notiong":
        return column
    elif option == "Replacing With Mean":
        column.fillna(int(column.mean()), inplace=True)
        return column
    elif option == "Replacing With Median":
        column.fillna(int(column.median()), inplace =True)
        return column