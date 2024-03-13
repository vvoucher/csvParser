from column_count import column_count

def station_from_col(db):

    first = column_count(db)[0]
    last = column_count(db)[1]
    rows = last-first
    if rows == 7:
        numStation = "215" 
    if rows == 4:
        numStation = "195" 
    if rows == 13:
        numStation = "155"

    return numStation, rows 