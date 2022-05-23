import pandas as pd

def cleanData(df, options):
    columnList = []
    for c in df.columns:
        if options[c][2] == 0:
            pass
        else:
            columnList.append(c)
            modType(df[c], options[0])
            handleMissingVal(df[c], options[1])

    data = df[columnList]



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