from NG_for_line import NG_for_line
from station_from_col import station_from_col
from subframe import subframe
import pandas  as pd
from no_file import no_file

def station_runtime(db):
    my_subframe = subframe()
    station = station_from_col(db)[0]

    A1_195 = NG_for_line(db, station, "A1", my_subframe)
    A2_195 = NG_for_line(db, station, "A2", my_subframe)
    A3_195 = NG_for_line(db, station, "A3", my_subframe)

    indexes =   [A1_195.name, A2_195.name, A3_195.name         ]
    count =     [A1_195.count, A2_195.count, A3_195.count      ]
    ngTable =   [A1_195.ngCount, A2_195.ngCount, A3_195.ngCount]
    prcTable =  [A1_195.procent, A2_195.procent, A3_195.procent] 

    ngDF = pd.DataFrame({'Liczba': count,'NG': ngTable,'Procent NG': prcTable, "Name": indexes})
    ngDF = ngDF.set_index('Name')

    qcDF195=pd.concat([A1_195.selectNGlist,A2_195.selectNGlist, A3_195.selectNGlist])
    qcDF195 = qcDF195.dropna(how='all', axis=1) 
    qcDF195 = qcDF195.fillna("")
    qc195name = my_subframe.nameFile(station,"QC", "")

    try:
        qcDF195.to_csv(qc195name)
    except:
        no_file(qc195name)

    return ngDF

