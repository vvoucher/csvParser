import pandas
def select_NG(df, name):
    
    df = df.loc[~((df[name] <= 0.8) & (df[name] >= 0))]
    df = df.loc[:,('Date','Time',name, 'ID', 'Hour', 'FullDate')]
    return df