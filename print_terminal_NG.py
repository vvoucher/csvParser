from create_timestamp import create_timestamp
from set_hours import set_hours
from filter_NG import filter_NG
from tabulate import tabulate
from drop_rows import drop_rows
from name_files import name_files

def print_terminal_NG(stacja, linia, db):

    db = create_timestamp(db)
    db = set_hours(db)
    df1 = filter_NG(db, linia)
    # df1=autogague(stacja, linia, db)
    
    print("\n   Stacja " + stacja + " " + linia)
    print(tabulate(drop_rows(df1.drop('Hour', axis=1)), headers=df1.head()))
    pathToSave=name_files(stacja, "Result", "_" + linia + ".csv")
    df1.to_csv(pathToSave)
    print("Zapisano dane:       ", pathToSave)
    # axisy = pd.DataFrame()

    # axisx = df1['Hour']
    # legend=[]
    # for col in range(1,len(df1.T)): #transponowane bo inaczej wychodzi 24
    #     name = "ST0" + str(col)
    #     nameOld = "ST0" + str(col-1)
    #     legend.append(name)
    #     axisy[name] = df1[name].astype(str)
    #     # ax[l,s].bar(axisx,axisy[name])
 