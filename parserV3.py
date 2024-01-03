import pandas as pd
from datetime import datetime
import time
import numpy as numpy
import matplotlib.pyplot as plt
from time import strftime

def today_to_file():
    today = (datetime.today()).strftime("%Y_%m_%d")
    return today

def name_files(number, folder, extension):
    today = today_to_file() 
    # print("Today: ", today)
    # path = folder + "/RS" + number + "Day/" + "RS" + number + "Report" + today + ".csv"
    path = folder + "\\" + "RS" + number + "Day" + "\\" + "RS" + number + "Report" + today + extension #".csv"
    
    # print("Sciezka:         ", path)
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

def filter_NG(df):
    table = []
    first = column_count(df)[0]
    last = column_count(df)[1]
    hours = []
    for hour in range(0,24):
        hours.append(hour)

    result = pd.DataFrame({'Hour': hours})
    tfTable = pd.DataFrame({'Hour': hours})
    for col in range(first ,last):
        name = "ST0" + str(col - first +1 )
        table = select(df,name).groupby('Hour').size()  
        table = table.to_frame()
        result[name]=table
        result=result.fillna("")

    dropRows = []
    for row2 in range(0,24):
        i=0
        for col2 in range(first, last):
            if result.iloc[row2,col2-4] == "":
                i+=1

        if i == last-5:
            dropRows.append(row2)

    finish=result.drop(dropRows)
    # print("CSV:        \n", result)
    # print("Terminal:        \n", finish)
    return result, finish # 0,1

def main_autogague(station):
    print("Stacja:      ", station)
    file=name_files(station,"Report", ".csv")
    dataBase = open_csv_file(file)
    dataBase = rename_header(dataBase)
    dataBase = create_timestamp(dataBase)
    dataBase = set_hours(dataBase)
    result = filter_NG(dataBase)[0]
    simpleResult = (filter_NG(dataBase)[1])
    # print("Obliczone \n")
    print(simpleResult)

    pathToSave=name_files(station, "Result", ".csv")
    result.to_csv(pathToSave)

    # print(result, "\n")
    print("Zapisano dane:       ", pathToSave)
    # print("\n")
    return result

def subplot_setup(ax1,data1):
    axisy = pd.DataFrame()
    axisx = data1['Hour']
    legend=[]
    for col in range(1,len(data1.T)): #transponowane bo inaczej wychodzi 24
        name = "ST0" + str(col)
        legend.append(name)
        axisy[name] = data1[name].astype(str)
        ax1.plot(axisx,axisy[name])

    ax1.set_ylabel("Liczba wystąpień")
    ax1.grid(True)
    ax1.set_title("Stacja 195")
    ax1.legend(legend)
    box = ax1.get_position()
    ax1.set_position([box.x0, box.y0, box.width * 0.8, box.height])
    ax1.legend(legend,loc='center left', bbox_to_anchor=(1, 0.5))
  
data195 = main_autogague("195")
data215 = main_autogague("215") 

fig, (ax1,ax2) = plt.subplots(2,1, sharex='col')

subplot_setup(ax1,data195)
subplot_setup(ax2,data215)
graphName = name_files("","Graphs",".png")# + ".png"
fig.savefig(graphName, dpi=300, format='png')
print("Wykres zapisano:     ", graphName)
print("\n")
sleepTime = 15
now = strftime("%H:%M:%S")
print(now,"To okno zamknie się za ", sleepTime,"sekund")
time.sleep(sleepTime)



