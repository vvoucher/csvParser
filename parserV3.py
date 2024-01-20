import pandas as pd
from datetime import datetime
import time
import numpy as numpy
import matplotlib.pyplot as plt
from time import strftime
import math
def today_to_file():
    today = (datetime.today()).strftime("%Y_%#m_%#d")
    return today

def name_files(number, folder, extension):
    today = today_to_file() 
    # lapPath = "C:\\Users\\UR100\\Documents\\csvParser\\"
    # path = lapPath + folder + "\\" + "RS" + number + "DAY" + "\\" + "RS" + number + "Report" + today + extension #".csv"
    path = folder + "\\" + "RS" + number + "DAY" + "\\" + "RS" + number + "Report" + today + extension #".csv"
    # path = "D:\\" + folder + "\\" + "RS" + number + "DAY" + "\\" + "RS" + number + "Report" + today + extension #".csv"
    print("Sciezka:         ", path)
    return path

def open_csv_file(file_name):

    df=pd.read_csv(file_name, encoding = 'unicode_escape', engine ='python')
    print("Plik:        ", file_name, "\n")
   
    return df

def column_count(df):
    o=0
    first = 0
    last = 0
    for n in range(0,len(df.columns)):
        if ("ST0" in df.columns[n]):
            o += 1
            if ("ST01" in df.columns[n]):
                first = n
    last = first + o   

    table = [first, last]
    return table

def rename_header(df):    

    table=column_count(df)

    first = table[0]
    last = table[1]

    columnNames = ['No','Date','Time','ID','Result']
    for col in range(first,last):
        columnNames.append("ST0" + str(col-first+1))
    df.columns = columnNames + [*df.columns[last:]]
    return df

def select(df, name):
    
    df = df.loc[~((df[name] <= 0.8) & (df[name] >= 0))]
    df = df.loc[:,('Date','Time',name, 'ID', 'Hour', 'FullDate')]
    return df

def create_timestamp(df):
    newTable= []
    df['FullDate']= df['Date'] + ' ' + df['Time']
    for n in range(0,len(df['Time'])):
        sum = df['Date'].iloc[n] + " " + df['Time'].iloc[n]
        format_date = (datetime.strptime(sum, '%Y/%m/%d %H:%M:%S')).timestamp()
        if format_date != 0:
            newTable.append(int(format_date))

    stamp=pd.DataFrame({'timestamp': newTable})
    stamp = stamp.set_index(df.index)
    df['timestamp'] = stamp.iloc[:,0].values
    df = df.set_index(df['timestamp'])
    df=df.sort_index()
    # print(df)
    return df

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

def filter_NG(df, line):
    if line == "A1":
        line = "7"
    if line == "A2":
        line = "8"
    if line == "A3":
        line = "9"    
        
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
        table = select(df,name).groupby('Hour').size()  
        # print(table)
        table = table.to_frame()
        result[name]=table
        result=result.fillna("")

    return result # 0,1

def drop_rows(df):
    table = []
    first = column_count(df)[0]
    last = column_count(df)[1]
    print(first, last)
    dropRows = []
    for row2 in range(0,24):
        i=0
        for col2 in range(first, last):
            if df.iloc[row2,col2] == "":
                i+=1
                # print(i)

        if i == last-first:
            dropRows.append(row2)
            # print(i)
    # print(dropRows)
    finish=df.drop(dropRows)
    return finish

def main_autogague(station, line):
    print("Stacja:      ", station)
    file=name_files(station,"Report", ".csv")
    # print("TEST")
    dataBase = open_csv_file(file)
    dataBase = rename_header(dataBase)
    dataBase = create_timestamp(dataBase)
    dataBase = set_hours(dataBase)
    result = filter_NG(dataBase, line)
    simpleResult = drop_rows(result)
    # print("Obliczone \n")
    # print(result)
    print(simpleResult)
    pathToSave=name_files(station, "Result" + line, ".csv")
    result.to_csv(pathToSave)

    # print(result, "\n")
    print("Zapisano dane:       ", pathToSave)
    # print("\n")
    return result

def subplot_setup(ax,data1, isname,islegend):
    axisy = pd.DataFrame()
    # ax = ax.flatten()
    axisx = data1['Hour']
    legend=[]
    for col in range(1,len(data1.T)): #transponowane bo inaczej wychodzi 24
        name = "ST0" + str(col)
        legend.append(name)
        axisy[name] = data1[name].astype(str)
        ax.plot(axisx,axisy[name])
    
    # if len(data1.T)==5:
    ax.set_ylabel("Liczba wystąpień")
    
    ax.grid(True)
    if isname:
        if len(data1.T)==5:
            ax.set_title("Stacja 195")
        if len(data1.T)==8:
            ax.set_title("Stacja 215")
            
    box = ax.get_position()
    ax.set_position([box.x0, box.y0, box.width * 0.8, box.height])

    if islegend:    
        ax.legend(legend)
        ax.legend(legend,loc='center left', bbox_to_anchor=(1, 0.5))


data195A1 = main_autogague("195","A1")
data215A1 = main_autogague("215","A1") 
data195A2 = main_autogague("195","A2")
data215A2 = main_autogague("215","A2") 
# data195A3 = main_autogague("195","A3")
# data215A3 = main_autogague("215","A3") 

fig, (ax1) = plt.subplots(nrows=2,ncols=2, sharex='all')
n=0
subplot_setup(ax1[0,0],data195A1,1,0)
subplot_setup(ax1[1,0],data215A1,1,0)
subplot_setup(ax1[0,1],data195A2,1,1)
subplot_setup(ax1[1,1],data215A2,1,1)
graphName = name_files("","Graphs",".png")# + ".png"
fig.savefig(graphName, dpi=300, format='png')
print("Wykres zapisano:     ", graphName)
print("\n")
# sleepTime = 15
# now = strftime("%H:%M:%S")
# print(now,"To okno zamknie się za ", sleepTime,"sekund")
# time.sleep(sleepTime)



