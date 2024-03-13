import time
import pandas as pd

from delay_terminal import delay_terminal
from stX_plot import stX_plot
from load_db import load_db
from no_file import no_file
from subframe import subframe
from station_runtime import station_runtime
from tabulate import tabulate
startTime = time.time()

my_subframe = subframe()
where = my_subframe.which()

if (where == "FS"):
    db = load_db("155", my_subframe)
    ngDF = pd.DataFrame({})
    ngDF = station_runtime(db)

    for l in range(1,4):
        lineName= "A" + str(l)
        if(db.size > 10):
            stX_plot(db,lineName, my_subframe)
            # print(lineName)
        else:
            print("Za mało pomiarów by wygenerować wykres")

if(where == "RS"):
    db195 = load_db("195", my_subframe)
    db215 = load_db("215", my_subframe)
    ngDF195 = station_runtime(db195)
    ngDF215 = station_runtime(db215)
    ngDF = pd.concat([ngDF195,ngDF215])

    for l in range(1,4):
        lineName= "A" + str(l)
        if(db195.size > 10):
            stX_plot(db195,lineName, my_subframe)
            stX_plot(db215,lineName, my_subframe)
            # print(lineName)
        else:
            print("Za mało pomiarów by wygenerować wykres")

dayResultFileName = my_subframe.nameFile(where,"Result","")
try:
    ngDF.to_csv(dayResultFileName)
    print(tabulate(ngDF, headers=ngDF.head()))
    print("Zapisano do pliku: ", dayResultFileName)
except:
    no_file(dayResultFileName)



endTime=time.time()
print("Czas kalkulacji: ", round((endTime-startTime)*100)/100, 's')
delay_terminal(20)

