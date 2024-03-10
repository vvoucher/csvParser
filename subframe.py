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
        self.station = station
        if self.side == "RS":
            return self.nameBase + "Report\\" + self.side + self.station + "DAY\\" + self.side + self.station + "Report" + self.today + ".csv"
        if self.side == "FS":
            return self.nameBase + "ReportDay\\Report" + self.today + ".csv"

    def nameGraph(self, station):
        self.station = station
        if self.side == "RS":
            return self.nameBase + self.folder +"\\" + self.side + self.station +  "DAY" + "\\" + self.side + self.station + self.today + ".png"

        if self.side == "FS":
            return self.nameBase + "Graphs\\"  + self.side + "Report" + self.today + ".png"
        pass    
    def nameFile(self, station, folder):
        self.station = station
        self.folder = folder
        if self.side == "RS":
            return self.nameBase + self.folder +"\\" + self.side + self.station +  "DAY" + "\\" + self.side + self.station + "Report" + self.today + ".csv"

        if self.side == "FS":
            return self.nameBase + self.folder +"\\"  + self.side + "Report" + self.today + ".csv"
        