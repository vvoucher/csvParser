from column_count import column_count
import pandas as pd
from select_NG import select_NG
def filter_NG(df, line):
    if line == "A1":
        line = "7"
    if line == "A2":
        line = "8"
    if line == "A3":
        line = "9"    

    table = []
    first = column_count(df)[0]
    last = column_count(df)[1]
    hours = []
    for hour in range(0,24):
        hours.append(hour)
    result2 = pd.DataFrame({'Hour': hours})

    result = pd.DataFrame({'Hour': hours})

    for col in range(first ,last):
        name = "ST0" + str(col - first +1 )
        table = select_NG(df,name).groupby('Hour').size()  
        table = table.to_frame()
        result[name]=table
        # result=result.fillna("")

    pointsTable = []
    table2 = []
    for col in range(last, len(df.columns)):
        if df.columns[col][0] == "P":
            pointsTable.append(df.columns[col])
    pointsTable.append('Hour')

    table3 = []
    result2 = df.loc[:,pointsTable]
    result3 = pd.DataFrame({'Hour': hours})
    for col in range(0, len(pointsTable)):
            temp = result2.loc[result2[pointsTable[col]] == "NG"]
            table3=temp.groupby('Hour').size()
            result3[pointsTable[col]] = table3
            # result3=result3.fillna("")
    combined = pd.concat([result, result3], axis=1, join='inner')
    combined = combined.drop('Hour', axis=1)
    # print(combined)
    # combined = combined.dropna(how='all', axis=1) 
    # combined = combined.fillna("")
    # print(combined)
    return combined # 0,1