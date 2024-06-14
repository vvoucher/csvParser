from column_count import column_count
def rename_header(df):    

    table=column_count(df)

    first = table[0]
    last = table[1]
    # print(df)
    columnNames = ['No','Date','Time','ID','Result']
    for col in range(first,last):
        if (col-first) < 9:
            columnNames.append("ST0" + str(col-first+1))
        if (col-first) >= 9:
            columnNames.append("ST" + str(col-first+1))

    for pos in range(last, len(df.T)):
        max = len(df.columns[pos])
        if max > 6:
            max = 4
        columnNames.append(df.columns[pos][0:max])

    df.columns = columnNames#+ [*df.columns[(last+1):]]
    return df