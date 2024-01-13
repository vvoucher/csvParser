from column_count import column_count
def rename_header(df):    

    table=column_count(df)

    first = table[0]
    last = table[1]

    columnNames = ['No','Date','Time','ID','Result']
    for col in range(first,last):
        columnNames.append("ST0" + str(col-first+1))
    df.columns = columnNames + [*df.columns[last:]]
    return df