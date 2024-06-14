def column_count(df):
    o=0
    first = 0
    last = 0
    # print(df.head())
    # print(len(df.columns))
    for n in range(0,len(df.columns)):
        if ("ST" in df.columns[n][0:2]):
            o += 1
            # print(df.columns[n])
            if ("ST01" in df.columns[n]):
                first = n
    last = first + o   
    # print(last)
    table = [first, last]
    return table