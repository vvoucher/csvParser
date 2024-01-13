import pandas as pd

def open_csv_file(file_name):
    df=pd.read_csv(file_name, encoding = 'unicode_escape', engine ='python')
    # print("Plik:        ", file_name, "\n")
    return df