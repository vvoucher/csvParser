import time
import pandas as pd
import numpy as np
from delay_terminal import delay_terminal
from stX_plot import stX_plot
from load_db import load_db
from no_file import no_file
from subframe import subframe
from station_runtime import station_runtime
from tabulate import tabulate
startTime = time.time()
where = 0
my_subframe = subframe(where)
where = my_subframe.which()
def calculate_station(stations, my_subframe):
    table = np.array(stations)
    ngDF = pd.DataFrame({})

    for n in range(0,len(stations)):
        print(n, stations[n])
        db = load_db(str(stations[n]), my_subframe)
        if ngDF.empty: 
            print("pusty")   
            ngDF = station_runtime(db)
        if ~ngDF.empty:
            ngDF = pd.concat([ngDF,station_runtime(db)])
    return ngDF

# print(calculate_station([155], my_subframe))

if (where == "FS"):
    db = load_db("155", my_subframe)
    ngDF = pd.DataFrame({})
    ngDF = station_runtime(db)


if(where == "RS"):
    db195 = load_db("195", my_subframe)
    db215 = load_db("215", my_subframe)
    ngDF195 = station_runtime(db195)
    ngDF215 = station_runtime(db215)
    ngDF = pd.concat([ngDF195,ngDF215])

dayResultFileName = my_subframe.nameFile(where,"Result","")
try:
    ngDF.to_csv(dayResultFileName)
    print(tabulate(ngDF, headers=ngDF.head()))
    print("Zapisano do pliku: ", dayResultFileName, "\n")
except:
    no_file(dayResultFileName)

if (where == "FS"):
    for l in range(1,4):
        lineName= "A" + str(l)
        if(db.size > 10):
            stX_plot(db,lineName, my_subframe)
            # print(lineName)
        else:
            print("Za mało pomiarów by wygenerować wykres")


if(where == "RS"):
    for l in range(1,4):
        lineName= "A" + str(l)
        if(db195.size > 10):
            stX_plot(db195,lineName, my_subframe)
            stX_plot(db215,lineName, my_subframe)
            # print(lineName)
        else:
            print("Za mało pomiarów by wygenerować wykres")


endTime=time.time()
print("Czas kalkulacji: ", round((endTime-startTime)*100)/100, 's')
delay_terminal(20)

