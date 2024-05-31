from datetime import datetime
import pandas as pd
def create_timestamp(df):
    newTable= []
    df['FullDate']= df['Date'] + ' ' + df['Time']
    for n in range(0,len(df['Time'])):
        sum = df['Date'].iloc[n] + " " + df['Time'].iloc[n]
        try:
            format_date = (datetime.strptime(sum, '%Y/%m/%d %H:%M:%S')).timestamp()
        except:
            format_date = (datetime.strptime(sum, '%d.%m.%Y %H:%M:%S')).timestamp()
        if format_date != 0:
            newTable.append(int(format_date))

    stamp=pd.DataFrame({'timestamp': newTable})
    stamp = stamp.set_index(df.index)
    df['timestamp'] = stamp.iloc[:,0].values
    df = df.set_index(df['timestamp'])
    df=df.sort_index()
    # print(df)
    return df