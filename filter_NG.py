from column_count import column_count
import pandas as pd
from select_NG import select_NG
import numpy as np
from whichLineID import whichLineID
def filter_NG(df, line):

    line = str(whichLineID(line))
    df = df.loc[(df['LineNumber'] == line)]
    
    ngCount = sum(df['Result'] == "NG")
    count = len(df['Result'] )
    
    newNGlist = df.loc[df['Result'] == "NG"]

    selectNGlist = pd.DataFrame()
    selectNGlist['FrameID'] = newNGlist['ID']

    table = []
    first = column_count(df)[0]
    last = column_count(df)[1]
    hours = []
    for hour in range(0,25):
        hours.append(hour)

    result = pd.DataFrame({'Hour': hours})
    result2 = pd.DataFrame({'Hour': hours})
    
    for col in range(first ,last):
        name = "ST0" + str(col - first +1 )
        table = select_NG(df,name).groupby('Hour').size()  
        selectNGlist[name] = newNGlist.iloc[:,col]
        toReplace=selectNGlist[name].loc[(selectNGlist[name] <= 0.8) & (selectNGlist[name] >= 0)].values
        selectNGlist[name] = selectNGlist[name].replace(toReplace, np.nan)
        table = table.to_frame()
        result[name]=table
        # result=result.fillna("")

    pointsTable = []
 
    for col in range(last, len(df.columns)):
        if df.columns[col][0] == "P":
            pointsTable.append(df.columns[col])
            selectNGlist[df.columns[col]] = newNGlist.iloc[:,col]
            selectNGlist[df.columns[col]] = selectNGlist[df.columns[col]].replace("OK",np.nan)
            selectNGlist[df.columns[col]] = selectNGlist[df.columns[col]].replace("NG",df.columns[col])
    # selectNGlist = selectNGlist.dropna(how='all', axis=1) 
    # selectNGlist = selectNGlist.fillna("")
    pointsTable.append('Hour')
    selectNGlist = selectNGlist.set_index(selectNGlist['FrameID'])
    selectNGlist = selectNGlist.drop('FrameID', axis=1)
    # print(selectNGlist)

    table3 = []
    result2 = df.loc[:,pointsTable]
    result3 = pd.DataFrame({'Hour': hours})
    for col in range(0, len(pointsTable)):
            temp = result2.loc[result2[pointsTable[col]] == "NG"]
            table3=temp.groupby('Hour').size()
            # print(table3)
            result3[pointsTable[col]] = table3
            # result3=result3.fillna("")
    combined = pd.concat([result, result3], axis=1, join='inner')
    combined = combined.drop('Hour', axis=1)

    return combined, count, ngCount, selectNGlist # 0,1