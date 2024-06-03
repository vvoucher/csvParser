
from filter_NG import filter_NG
from create_timestamp import create_timestamp
from set_hours import set_hours
from filter_NG import filter_NG
from tabulate import tabulate
from drop_rows import drop_rows
from name_files import name_files
from no_file import no_file
from whichLineID import whichLineID
from subframe import subframe
from station_from_col import station_from_col
which = 0
class NG_for_line:
    def __init__(self, db, stacja, linia, my_subframe) -> None:

        self.db = db
        self.linia = linia
        self.stacja = stacja
        if self.stacja == "155":
            which = "FS"
        if self.stacja == ("195") or ("215"):
            which = "RS"        
        my_subframe = subframe(which)

        which = my_subframe.which()

        self.db = create_timestamp(self.db)
        self.db = set_hours(self.db)
        self.name = self.stacja + " " + self.linia
        self.filtredlist, self.count, self.ngCount, self.selectNGlist = filter_NG(self.db, self.linia, which)
        if (self.count != 0):
            self.procent = round((self.ngCount/self.count)*1000)/10
        else:
            self.procent = 0

        pathToSave = my_subframe.nameFile(stacja,"Result", linia)

        try:
            self.filtredlist.to_csv(pathToSave)
            self.filtredlist = self.filtredlist.dropna(how='all', axis=1) 
            self.filtredlist = self.filtredlist.fillna("")
            print("\n   Stacja " + stacja + " " + linia)
            print(tabulate(drop_rows(self.filtredlist), headers=self.filtredlist.head()))
            print("Zapisano dane:       ", pathToSave)
        except:
            no_file(pathToSave)



        

        
    