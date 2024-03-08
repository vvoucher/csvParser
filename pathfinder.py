import os

pathFS = "D:\\project\\Report\\ReportDay"
pathRS = "D:\\Report"
pathFsExist = 0 
pathRsExist = 0
def pathfinder():
    if os.path.exists(pathRS):
        print("Istnieje scieżka Rs")
        pathRsExist = True
    if os.path.exists(pathRS):
        print("Istnieje scieżka Fs")
        pathFsExist = True
        if (pathFsExist):# and pathFsExist):
            print("Istnieją dwie ścieżki")
    else:
        print("git")
        return 1
    # else:
    #     print("Brak folderu z danymi")

