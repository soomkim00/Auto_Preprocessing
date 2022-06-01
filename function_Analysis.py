import pandas as pd
def getfirstlook(df, nrows=5, uniqueids=None):
    out = {}
    #out['head'] = df.head(nrows)
    out['dtypes\n'] = df.dtypes
    out['nrows'] = df.shape[0]
    out['ncols'] = df.shape[1]
    out['index'] = df.index
    if (uniqueids is not None):
        out['uniqueids'] = df['uniqueids'].nunique()
    return out

def displaydict(dicttodisplay):
    s = ""
    for x in dicttodisplay.items():
        s += ': '.join(map(str, x))
        s += '\n'
    return s

def gettots(df):
    out = {}
    out['mins'] = df.min()
    out['per15'] = df.quantile(0.15)
    out['qr1'] = df.quantile(0.25)
    out['med'] = df.median()
    out['qr3'] = df.quantile(0.75)
    out['per85'] = df.quantile(0.85)
    out['max'] = df.max()
    out['count'] = df.count()
    out['mean'] = df.mean()
    out['iqr'] = out['qr3'] - out['qr1']
    return pd.DataFrame(out)


def filterNumeric(df):
    numerics = ['int16', 'int32', 'int64', 'float32', 'float64']
    df = df.select_dtypes(include=numerics)
    return df