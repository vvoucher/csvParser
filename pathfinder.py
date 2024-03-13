import os

pathFS = "D:\\project\\Report\\ReportDay"
pathRS = "D:\\Report"
pathFsExist = False
pathRsExist = False

def pathfinder():
    if os.path.exists(pathRS):
        # print("Istnieje scieżka RS")
        pathRsExist = True
    else:
        pathRsExist = False
    if os.path.exists(pathFS):
        # print("Istnieje scieżka FS")
        pathFsExist = True
        if (pathRsExist):# and pathFsExist):
            print("Istnieją dwie ścieżki",  pathFS, pathRS)
    else: 
        pathFsExist = False

    if ((pathFsExist) and (pathRsExist)):
        return -1
    if ((not pathFsExist) and (not pathRsExist)):
        return 0
    if ((pathFsExist) and (not pathRsExist)):
        return 1
    if ((not pathFsExist) and (pathRsExist)):
        return 2


