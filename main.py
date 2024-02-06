import time
from delay_terminal import delay_terminal
from stX_plot import stX_plot
from print_terminal_NG import print_terminal_NG
from load_db import load_db
import pandas as pd
from tabulate import tabulate
from name_files import name_files
import os

startTime = time.time()
ngTable = pd.DataFrame()

db215 = load_db("215")
db195 = load_db("195")

db215['LineNumber']=db215['ID'].astype(str).str[16:17]
db195['LineNumber']=db195['ID'].astype(str).str[16:17]

if(db195.size > 10):
    stX_plot(db195,"A1")
    stX_plot(db195,"A2")
    stX_plot(db215,"A1")
    stX_plot(db215,"A2")
else:
    print("Za mało pomiarów by wygenerować wykres")

c195a1, n195a1, ngList1 = print_terminal_NG("195", "A1", db195)
c195a2, n195a2, ngList2 = print_terminal_NG("195", "A2", db195)
c215a1, n215a1, ngList3 = print_terminal_NG("215", "A1", db215)
c215a2, n215a2, ngList4 = print_terminal_NG("215", "A2", db215)

def prc(ngCount, Count):
    n = round((ngCount/Count)*1000)/10
    return n

indexes = ["195 A1", "195 A2", "215 A1", "215 A2"]
count = [c195a1,c195a2, c215a1, c215a2]
ngTable = [n195a1, n195a2, n215a1, n215a2]
prcTable = [prc(n195a1,c195a1), prc(n195a2,c195a2), prc(n215a1,c215a1), prc(n215a2,c215a2)]

ngDF = pd.DataFrame({'Liczba': count,'NG': ngTable,'Procent NG': prcTable, "Name": indexes})
ngDF = ngDF.set_index('Name')

print("\n", tabulate(ngDF, headers=ngDF.head()),"\n")

dayResultFileName  = name_files("","Result", ".csv")
ngDF.to_csv(dayResultFileName)
print("Zapisano do pliku: ", dayResultFileName)
qcDF195=pd.concat([ngList1,ngList2])
qcDF195 = qcDF195.dropna(how='all', axis=1) 
qcDF195 = qcDF195.fillna("")

qcDF215=pd.concat([ngList3,ngList4])
qcDF215 = qcDF215.dropna(how='all', axis=1) 
qcDF215 = qcDF215.fillna("")

qc195name= name_files("195","QC",".csv")

qcDF195.to_csv(qc195name)

qc215name= name_files("215","QC",".csv")

qcDF215.to_csv(qc215name)


endTime=time.time()
print("Czas kalkulacji: ", round((endTime-startTime)*100)/100, 's')
delay_terminal(20)

