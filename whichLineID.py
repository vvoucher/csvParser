
def whichLineID(line):
    for l in range(1,4): #1 2 3 
        lineName = "A" + str(l)
        if line == lineName:
            return l + 6 # 7 8 9 
