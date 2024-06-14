from open_csv_file import open_csv_file
from rename_header import rename_header
from no_file import no_file 
from subframe import subframe
import pandas as pd
from tabulate import tabulate
from delay_terminal import delay_terminal
from create_timestamp import create_timestamp
from column_count import column_count

def load_db(station, my_subframe):
    file = my_subframe.nameOpen(station)
    backup = my_subframe.nameBackup(station)
    db_backup = pd.DataFrame()
    db = pd.DataFrame()
    db_diff = pd.DataFrame()
    
    org_len=0
    print("\nŚcieżka backup: ", backup)
    print("Ścieżka pliku: ", file)
    try:        
        db = open_csv_file(file)

        db = rename_header(db) 
        org_len=len(db.T)
    except:
        no_file(file)

    try:
        db_backup = open_csv_file(backup)
    except:
        try:
            db.to_csv(backup, index = False)
            print("Zapisano nowy backup: ", backup)
        except:
            no_file(backup)

    if abs(len(db_backup)-len(db)) > 0:
        
        print("\nLiczba nowych wpisów: ", abs(len(db_backup)-len(db)))
        db_backup = rename_header(db_backup)
        db_diff = pd.concat([db,db_backup])
        db_diff = db_diff.drop_duplicates(subset=['ID', 'Time'], keep= "last") # DROP DUPLICATES
        db_diff=create_timestamp(db_diff)
        db_diff["Date"] = pd.to_datetime(db_diff['Date'],dayfirst= True, format = 'mixed' )
        db_diff['Date'] = db_diff['Date'].dt.strftime("%d.%m.%Y")
        db_index=pd.DataFrame()
        db_index['No']=db_diff.index
        db_diff['No'] = range(0,len(db_diff))
        db_out = pd.DataFrame()
        new_len=len(db_diff.T)

        for col in range(1,org_len):
            db_out.index = db_diff.index     
            db_out[db.columns[col]]=db_diff[db.columns[col]]

        db=db_diff
        db_backup=db_diff
        try:
            db_out.to_csv(backup, index = False)
            print("Zapisano nowy backup: ", backup)
        except:
            no_file(backup)        
    else:
        print("\nBackup: ",len(db_backup)," jest tej samej długości co dane: ", len(db))
    
    db['LineNumber']=db['ID'].astype(str).str[16:17]
    return db
