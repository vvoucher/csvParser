import time
import pandas as pd

from delay_terminal import delay_terminal
from stX_plot import stX_plot
from print_terminal_NG import print_terminal_NG
from load_db import load_db
from tabulate import tabulate
from name_files import name_files
from pathfinder import pathfinder
from no_file import no_file
from whichLineID import whichLineID
from prc import prc
from NG_for_line import NG_for_line
from subframe import subframe

startTime = time.time()
ngTable = pd.DataFrame()
# pathfinder()
my_subframe = subframe()
# print(my_subframe.which())
# print(my_subframe.nameFile("215", "Result"))
# print(my_subframe.nameGraph("215"))

# print(my_subframe.nameOpen("215"))

db215 = load_db("215", my_subframe)
db195 = load_db("195", my_subframe)

for l in range(1,4):
    lineName= "A" + str(l)
    if(db195.size > 10):
        stX_plot(db195,lineName, subframe)
        stX_plot(db215,lineName, subframe)
        # print(lineName)
    else:
        print("Za mało pomiarów by wygenerować wykres")

A1_195 = NG_for_line(db195, "195", "A1")
A2_195 = NG_for_line(db195, "195", "A2")
A3_195 = NG_for_line(db195, "195", "A3")
A1_215 = NG_for_line(db215, "215", "A1")
A2_215 = NG_for_line(db215, "215", "A2")
A3_215 = NG_for_line(db215, "215", "A3")

indexes =   [A1_195.name, A2_195.name, A3_195.name,             A1_215.name, A2_215.name, A3_215.name ]
count =     [A1_195.count, A2_195.count, A3_195.count,          A1_215.count, A2_215.count, A3_215.count]
ngTable =   [A1_195.ngCount, A2_195.ngCount, A3_195.ngCount,    A1_215.ngCount, A2_215.ngCount, A3_215.ngCount]
prcTable =  [A1_195.procent, A2_195.procent, A3_195.procent,    A1_215.procent, A2_215.procent, A3_215.procent] 

ngDF = pd.DataFrame({'Liczba': count,'NG': ngTable,'Procent NG': prcTable, "Name": indexes})
ngDF = ngDF.set_index('Name')

print("\n", tabulate(ngDF, headers=ngDF.head()),"\n")

dayResultFileName  = name_files("","Result", ".csv")
try:
    ngDF.to_csv(dayResultFileName)
except:
    no_file(dayResultFileName)


print("Zapisano do pliku: ", dayResultFileName)

qcDF195=pd.concat([A1_195.selectNGlist,A2_195.selectNGlist, A3_195.selectNGlist])
qcDF195 = qcDF195.dropna(how='all', axis=1) 
qcDF195 = qcDF195.fillna("")

qcDF215=pd.concat([A1_215.selectNGlist, A2_215.selectNGlist, A3_215.selectNGlist])
qcDF215 = qcDF215.dropna(how='all', axis=1) 
qcDF215 = qcDF215.fillna("")

qc195name= name_files("195","QC",".csv")
try:
    qcDF195.to_csv(qc195name)
except:
    no_file(qcDF195)

qc215name= name_files("215","QC",".csv")
try:
    qcDF215.to_csv(qc215name)
except:
    no_file(qcDF215)

endTime=time.time()
print("Czas kalkulacji: ", round((endTime-startTime)*100)/100, 's')
delay_terminal(20)

