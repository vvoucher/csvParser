from autogague import autogague
from tabulate import tabulate
from drop_rows import drop_rows
from name_files import name_files
import matplotlib.pyplot as plt
import numpy as numpy
import pandas as pd
from open_csv_file import open_csv_file
from rename_header import rename_header
from column_count import column_count
from delay_terminal import delay_terminal

def bulk(stacja, linia, db):

    df1=autogague(stacja, linia, db)
    print("\n   Stacja " + stacja + " " + linia)
    print(tabulate(drop_rows(df1.drop('Hour', axis=1)), headers=df1.head()))
    pathToSave=name_files(stacja, "Result", "_" + linia + ".csv")
    df1.to_csv(pathToSave)
    print("Zapisano dane:       ", pathToSave)
    axisy = pd.DataFrame()

    axisx = df1['Hour']
    legend=[]
    for col in range(1,len(df1.T)): #transponowane bo inaczej wychodzi 24
        name = "ST0" + str(col)
        nameOld = "ST0" + str(col-1)
        legend.append(name)
        axisy[name] = df1[name].astype(str)
        # ax[l,s].bar(axisx,axisy[name])
    
def load_db(station):
    file=name_files(station,"Report", ".csv")
    db = open_csv_file(file)
    db = rename_header(db)  
    return db

externaldb=pd.DataFrame()
def draw_bulk_plot(db, line):
    if line == "A1":
        short = "7"
        place = 0
    if line == "A2":
        short = "8"
        place = 1
    if line == "A3":
        short = "9"   
    DbForLineNmber = pd.DataFrame()
    DbForLineNmber = db[db['LineNumber'] == short]
    first = column_count(DbForLineNmber)[0]
    last = column_count(DbForLineNmber)[1]
    rows = last-first
    if rows == 7:
        myName = "215_" + line
    if rows == 4:
        myName = "195_" + line
    fig, ax = plt.subplots(rows, 1)#, sharex='all')
    axisy = pd.DataFrame()
    axisx = DbForLineNmber['No']
    legend=[]
    plt.rc('ytick', labelsize=6) 

    for col in range(1,last-first+1): #transponowane bo inaczej wychodzi 24
        name = "ST0" + str(col)
        ax[col-1].grid(True)
        legend.append(name)
        max = DbForLineNmber[name].max()
        min = DbForLineNmber[name].min()
        if max < 0.9:
            max = 0.9
        if min > -0.1:
            min = -0.1

        ax[col-1].set_ylim(min,max)
        axisy[name] = DbForLineNmber[name].astype(float)
        max_yticks = 5
        yloc = plt.MaxNLocator(max_yticks)
        ax[col-1].yaxis.set_major_locator(yloc)
        ax[col-1].set_ylabel(name + ' [mm]', fontsize=5)#, rotation=0)
        # if col != last:
            # ax[col-1].set_axis_off()
        # else:
        #     ax[col-1].xaxis.set_visible(False)
        ax[col-1].plot(axisx,axisy[name])
    graphName = name_files("","Graphs","_" + myName + ".png")# + ".png"
    fig.savefig(graphName, dpi=300, format='png')


db215 = load_db("215")
db195 = load_db("195")

db215['LineNumber']=db215['ID'].astype(str).str[16:17]
db195['LineNumber']=db195['ID'].astype(str).str[16:17]

draw_bulk_plot(db195,"A1")
draw_bulk_plot(db195,"A2")
draw_bulk_plot(db215,"A1")
draw_bulk_plot(db215,"A2")

bulk("195", "A1", db195)
bulk("195", "A2", db195)
bulk("215", "A1", db215)
bulk("215", "A2", db215)

delay_terminal(15)

