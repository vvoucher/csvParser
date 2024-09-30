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
    colNames =  ['Liczba', 'NG', 'Procent NG', 'Name']
    colSquad =  [count, ngTable, prcTable, indexes] 
    # summedNg =  []#A1.summedNg.values, A2.summedNg.values, A3.summedNg.values] 
    # print(pd.concat([A1.summedNg, A2.summedNg, A3.summedNg]))
    SUMMED_DF = pd.DataFrame(pd.concat([A1.summedNg, A2.summedNg, A3.summedNg]))
    for l in range(0,len(A1.summedNg.columns.values)):
        colNames.append(A1.summedNg.columns.values[l])
    NG_DF = pd.DataFrame( columns = colNames, data = SUMMED_DF)
    for i in range(0, len(colSquad)):
        NG_DF[colNames[i]] = colSquad[i]
    # NG_DF.columns = colNames
    # print(NG_DF)
    # test_NG_DF = pd.DataFrame(columns= colNames, A1.summedNg.columns)
    # print(type(A1.summedNg.columns))
    NG_DF = pd.DataFrame({'Liczba': count,'NG': ngTable,'Procent NG': prcTable, "Name": indexes})
    # NG_DF.columns = []
    SUMMED_DF = SUMMED_DF.set_index(NG_DF.index)
    # print(SUMMED_DF.columns)
    NG_DF = pd.concat([NG_DF, SUMMED_DF], axis = 1)
    NG_DF = NG_DF.set_index('Name')

    QC_DF=pd.concat([A1.selectNGlist,A2.selectNGlist, A3.selectNGlist])
    QC_DF = QC_DF.dropna(how='all', axis=1) 
    QC_DF = QC_DF.fillna("")
    qc_name = my_subframe.nameFile(station,"QC", "")
    # print(qc_name)
    try:
        QC_DF.to_csv(qc_name)
    except:
        no_file(qc_name)

    return NG_DF

