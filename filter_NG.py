from column_count import column_count
import pandas as pd
from select_NG import select_NG
from tabulate import tabulate
def filter_NG(df, line):
    if line == "A1":
        line = "7"
    if line == "A2":
        line = "8"
    if line == "A3":
        line = "9"    

    # print(df['Result'].str.count('NG'))
    # print(df['Result'].groupby('Result'))
    
    df['ID']=df['ID'].astype(str).str[16:17]
    df = df.loc[(df['ID'] == line)] 
    table = []
    first = column_count(df)[0]
    last = column_count(df)[1]
    hours = []
    for hour in range(0,24):
        hours.append(hour)
  
    result = pd.DataFrame({'Hour': hours})
    # tfTable = pd.DataFrame({'Hour': hours})
    for col in range(first ,last):
        name = "ST0" + str(col - first +1 )
        table = select_NG(df,name).groupby('Hour').size()  
        table = table.to_frame()
        result[name]=table
        result=result.fillna("")

    return result # 0,1