import time
from delay_terminal import delay_terminal
from stX_plot import stX_plot
from print_terminal_NG import print_terminal_NG
from load_db import load_db

startTime = time.time()

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

print_terminal_NG("195", "A1", db195)
print_terminal_NG("195", "A2", db195)
print_terminal_NG("215", "A1", db215)
print_terminal_NG("215", "A2", db215)

endTime=time.time()
print("Czas kalkulacji: ", round((endTime-startTime)*100)/100, 's')

delay_terminal(15)

