def column_count(df):
    o=0
    first = 0
    last = 0
    for n in range(0,len(df.columns)):
        if ("ST" in df.columns[n]):
            o += 1
            if ("ST01" in df.columns[n]):
                first = n
    last = first + o   

    table = [first, last]
    return table