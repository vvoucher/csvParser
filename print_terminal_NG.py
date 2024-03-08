from create_timestamp import create_timestamp
from set_hours import set_hours
from filter_NG import filter_NG
from tabulate import tabulate
from drop_rows import drop_rows
from name_files import name_files
from no_file import no_file
def print_terminal_NG(stacja, linia, db):
    
    db = create_timestamp(db)
    db = set_hours(db)
    df1, count, ngCount, selectNGlist = filter_NG(db, linia)
    pathToSave=name_files(stacja, "Result", "_" + linia + ".csv")
    try:
        df1.to_csv(pathToSave)
    except:
        no_file(pathToSave)
    df1 = df1.dropna(how='all', axis=1) 
    df1 = df1.fillna("")
    print("\n   Stacja " + stacja + " " + linia)

    print(tabulate(drop_rows(df1), headers=df1.head()))

    print("Zapisano dane:       ", pathToSave)
    return count, ngCount, selectNGlist

 