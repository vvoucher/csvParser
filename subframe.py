from today_to_file import today_to_file
from delay_terminal import delay_terminal
from pathfinder import pathfinder
class subframe:
    def __init__(self):
        self.today = today_to_file() 
        match pathfinder():
            case -1:
                delay_terminal(10)
                exit("EXIT")
            case 0:
                delay_terminal(10)
                exit("EXIT")
            case 1:
                self.side = "FS"
                self.nameBase = "D:\\project\\Report\\"
            case 2:
                self.side = "RS"
                self.nameBase = "D:\\"
    
    def which(self):
        
        return self.side
    
    def nameOpen(self, station):
        # self.side = side
        self.station = station
        if ((self.station == "215") or (self.station == "195")):
            return self.nameBase + "Report\\" + self.side + self.station + "DAY\\" + self.side + self.station + "Report" + self.today + ".csv"
        if self.station == "155":
            return self.nameBase + "ReportDay\\Report" + self.today + ".csv"

    def nameGraph(self, station, line):
        # RSReport2024_1_13_195_A2
        self.station = station
        self.line = line
        if (self.station == "215") or (self.station == "195"):
            return self.nameBase + "Graphs\\" + self.side + self.station +  "DAY" + "\\" + self.side + "Report" + self.today +"_" + self.station + "_" + self.line + ".png"

        if self.station == "155":
            return self.nameBase + "Graphs\\"  + self.side + "Report" + self.today + "_" + self.station + "_" + self.line + ".png"
        pass    
    def nameFile(self, station, folder, line):
        self.station = station
        self.folder = folder
        self.line = line
        if (self.station == "215") or (self.station == "195"):
            return self.nameBase + self.folder +"\\" + self.side + self.station +  "DAY" + "\\" + self.side + self.station + "Report" + self.today + "_" + self.line + ".csv"

        if (self.station == "155"):
            return self.nameBase + self.folder +"\\"  + self.side + "Report" + self.today + "_" + self.line + ".csv"
        
        if (self.station == "FS"):
            return self.nameBase + self.folder +"\\" + self.side + "DAY" + "\\" + self.side + "Report" + self.today + "_" + self.line + ".csv"
        if (self.station == "RS"):
            return self.nameBase + self.folder +"\\" + self.side +  "DAY" + "\\" + self.side + "Report" + self.today + "_" + self.line + ".csv"
