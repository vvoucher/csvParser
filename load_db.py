from name_files import name_files
from open_csv_file import open_csv_file
from rename_header import rename_header
import os
from no_file import no_file 

def load_db(station):
    file=name_files(station,"Report", ".csv")
    # if ~os.path.exists(file):
    #     print("brak: ", file)
    try:        
        db = open_csv_file(file)
    except:
        no_file(file)

    db = rename_header(db) 
    db['LineNumber']=db['ID'].astype(str).str[16:17]
    return db
