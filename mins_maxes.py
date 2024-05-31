def mins_maxes(which):
    if which == "FS":
        mins = [0, 0, 0, 0, -1, -1, -1, -1, -1, -1, 0, 0, 0]
        maxes = [0.8, 0.8, 1.0, 1.0, 1.0, 1.0, 0.5, 0.5, 1.0, 1.0, 0.8, 0.8, 0.6]
    if which == "RS":
        mins = [0, 0 ,0 ,0 ,0 ,0 ,0 ,0]
        maxes = [0.8 ,0.8 ,0.8 ,0.8 ,0.8 ,0.8 ,0.8 ,0.8]
    return mins, maxes