from open_csv_file import open_csv_file
from rename_header import rename_header
from no_file import no_file 
from subframe import subframe

def load_db(station, my_subframe):
    file = my_subframe.nameOpen(station)
    print(file)
    try:        
        db = open_csv_file(file)
    except:
        no_file(file)

    db = rename_header(db) 
    db['LineNumber']=db['ID'].astype(str).str[16:17]
    return db
