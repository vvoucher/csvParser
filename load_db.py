from open_csv_file import open_csv_file
from rename_header import rename_header
from no_file import no_file 
from subframe import subframe
import pandas as pd
from tabulate import tabulate

def load_db(station, my_subframe):
    file = my_subframe.nameOpen(station)
    backup = my_subframe.nameBackup(station)
    print("Ścieżka backup: ", backup)
    print("Ścieżka pliku: ", file)
    try:        
        db = open_csv_file(file)
        db = rename_header(db) 
    except:
        no_file(file)

    try:
        db_backup = open_csv_file(backup)
        # print(len(db_backup))
        
    except:
        try:
            print("Tworzę nowy backup")
            db.to_csv(backup, index = False)
            print(backup)
        except:
            no_file(backup)

    # if len(db_backup) >= len(db):
    #     print("backup is longer")
    #     # print()
    # if len(db_backup) > len(db):
    #     print("backup is shorter")
    
    # db_backup = rename_header(db_backup) 
    # db_diff = pd.concat([db,db_backup])
    # db_diff = db_diff.drop_duplicates() # DROP DUPLICATES
    # for i in range(0,len(db.columns)):
    #     db_diff.columns.values[i]=db.columns.values[i]
    # db_backup = pd.concat([db_backup, db_diff])
    
    db['LineNumber']=db['ID'].astype(str).str[16:17]
    return db
