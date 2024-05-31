from NG_for_line import NG_for_line
from station_from_col import station_from_col
from subframe import subframe
import pandas  as pd
from no_file import no_file

def station_runtime(db):
    
    station = station_from_col(db)[0]
    if station == "155":
        side = "FS"
    if station == ("195") or ("215"):
        side = "RS"
    print(station)
    my_subframe = subframe(side)
    A1 = NG_for_line(db, station, "A1", my_subframe)
    A2 = NG_for_line(db, station, "A2", my_subframe)
    A3 = NG_for_line(db, station, "A3", my_subframe)
    
    indexes =   [A1.name, A2.name, A3.name         ]
    count =     [A1.count, A2.count, A3.count      ]
    ngTable =   [A1.ngCount, A2.ngCount, A3.ngCount]
    prcTable =  [A1.procent, A2.procent, A3.procent] 

    NG_DF = pd.DataFrame({'Liczba': count,'NG': ngTable,'Procent NG': prcTable, "Name": indexes})
    NG_DF = NG_DF.set_index('Name')

    QC_DF=pd.concat([A1.selectNGlist,A2.selectNGlist, A3.selectNGlist])
    QC_DF = QC_DF.dropna(how='all', axis=1) 
    QC_DF = QC_DF.fillna("")
    qc_name = my_subframe.nameFile(station,"QC", "")

    try:
        QC_DF.to_csv(qc_name)
    except:
        no_file(qc_name)

    return NG_DF

