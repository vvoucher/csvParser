from column_count import column_count
def drop_rows(df):
    first = column_count(df)[0]
    # last = column_count(df)[1]
    last = len(df.columns)
    dropRows = []
    for row2 in range(0,24):
        i=0
        for col2 in range(first, last):
            if df.iloc[row2,col2] == "":
                i+=1

        if i == last-first:
            dropRows.append(row2)

    finish=df.drop(dropRows)
    return finish