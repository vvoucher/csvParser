import pandas as pd

def set_hours(df):
    df['Hour'] = pd.to_datetime(df['FullDate'], format='%Y/%m/%d %H:%M:%S', exact=False)
    df['Hour'] = df['Hour'].astype(str).str[11:13] 
    table = []
    
    for row in range(0,len(df['Hour'])):
        table.append(int(df['Hour'].iloc[row]) + 1)
    
    hours = pd.DataFrame({'Hour': table})
    hours = hours.set_index(df.index)
    df['Hour'] = hours.iloc[:,0].values
    return df