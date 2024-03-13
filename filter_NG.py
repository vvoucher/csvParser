from column_count import column_count
import pandas as pd
from select_NG import select_NG
import numpy as np
from whichLineID import whichLineID
def filter_NG(df, line, which):

    mins = []
    maxes = []
    # min = [0, 0, 0, 0, -1, -1, -1, -1, -1, -1, 0, 0, 0]
    # max = [0.8, 0.8, 1.0, 1.0, 1.0, 1.0, 0.5, 0.5, 1.0, 1.0, 0.8, 0.8, 0.6]
    if which == "FS":
        mins = [0, 0, 0, 0, -1, -1, -1, -1, -1, -1, 0, 0, 0]
        maxes = [0.8, 0.8, 1.0, 1.0, 1.0, 1.0, 0.5, 0.5, 1.0, 1.0, 0.8, 0.8, 0.6]
    if which == "RS":
        mins = [0,0,0,0,0,0,0,0]
        maxes = [0.8,0.8,0.8,0.8,0.8,0.8,0.8,0.8]
    
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
        l = (col - first +1 )
        # print(l, maxes[l-1], mins[l-1])
        if l < 10:
            name = "ST0" + str(l)
        if l >= 10:
            name = "ST" + str(l)

        table = select_NG(df,name, mins[l-1], maxes[l-1]).groupby('Hour').size() 
        # print(name, l, first, last, line)

        selectNGlist[name] = newNGlist.iloc[:,col]

        try:
            selectNGlist[name] = selectNGlist[name].astype(float)
        except:
            # print(name, l)
            exit("EXIT")
        toReplace=selectNGlist[name].loc[~(selectNGlist[name] >= mins[l-1]) & (selectNGlist[name] <= maxes[l-1])].values
        selectNGlist[name] = selectNGlist[name].replace(toReplace, np.nan)
        table = table.to_frame()
        result[name]=table


    pointsTable = []
 
    for col in range(last, len(df.columns)):
        if df.columns[col][0] == "P":
            pointsTable.append(df.columns[col])
            selectNGlist[df.columns[col]] = newNGlist.iloc[:,col]
            selectNGlist[df.columns[col]] = selectNGlist[df.columns[col]].replace("OK",np.nan)
            selectNGlist[df.columns[col]] = selectNGlist[df.columns[col]].replace("NG",df.columns[col])

    pointsTable.append('Hour')
    selectNGlist = selectNGlist.set_index(selectNGlist['FrameID'])
    selectNGlist = selectNGlist.drop('FrameID', axis=1)

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
    # print(combined)
    return combined, count, ngCount, selectNGlist # 0,1