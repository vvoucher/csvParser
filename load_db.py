from name_files import name_files
from open_csv_file import open_csv_file
from rename_header import rename_header

def load_db(station):
    file=name_files(station,"Report", ".csv")
    db = open_csv_file(file)
    db = rename_header(db)  
    return db
