from create_timestamp import create_timestamp
from set_hours import set_hours
from filter_NG import filter_NG
from tabulate import tabulate
from drop_rows import drop_rows
from name_files import name_files

def print_terminal_NG(stacja, linia, db):
    
    db = create_timestamp(db)
    db = set_hours(db)
    df1, count, ngCount, selectNGlist = filter_NG(db, linia)
    pathToSave=name_files(stacja, "Result", "_" + linia + ".csv")
    df1.to_csv(pathToSave)
    df1 = df1.dropna(how='all', axis=1) 
    df1 = df1.fillna("")
    print("\n   Stacja " + stacja + " " + linia)

    print(tabulate(drop_rows(df1), headers=df1.head()))

    print("Zapisano dane:       ", pathToSave)
    return count, ngCount, selectNGlist

 