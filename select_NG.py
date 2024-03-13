import pandas
def select_NG(df, name, min, max):
    
    df = df.loc[~((df[name] <= max) & (df[name] >= min))]
    # print(df)
    df = df.loc[:,('Date','Time',name, 'ID', 'Hour', 'FullDate')]
    # df[name] = df[name].astype(float)
    return df