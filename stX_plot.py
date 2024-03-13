from name_files import name_files
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# FS ST01(0 0.8),ST02(0 0.8),ST03(0 1.0),ST04(0 1.0),ST05(-1.0 1.0),ST06(-1.0 1.0),ST07(-1.0 0.5),ST08(-1.0 0.5),ST09(-1.0 1.0),ST10(-1.0 1.0),ST11(0 0.8),ST12(0 0.8),ST13(0 0.6)
from column_count import column_count
from no_file import no_file
from whichLineID import whichLineID
from subframe import subframe
from station_from_col import station_from_col
# mins = [0, 0, 0, 0, -1, -1, -1, -1, -1, -1, 0, 0, 0]
# maxes = [0.8, 0.8, 1.0, 1.0, 1.0, 1.0, 0.5, 0.5, 1.0, 1.0, 0.8, 0.8, 0.6]

def stX_plot(db, line, my_subframe):

    my_subframe = subframe()
    short = whichLineID(line)
    plt.rc('ytick', labelsize=3) 
    DbForLineNmber = pd.DataFrame()
    DbForLineNmber = db[db['LineNumber'] == str(short)]
    
    # first = column_count(DbForLineNmber)[0]
    # last = column_count(DbForLineNmber)[1]
    # rows = last-first
    # if rows == 7:
    #     numStation = "215" 
    # if rows == 4:
    #     numStation = "195" 
    # if rows == 13:
    #     numStation = "155" 

    numStation, rows = station_from_col(DbForLineNmber)

    if numStation == "155":
        mins = [0, 0, 0, 0, -1, -1, -1, -1, -1, -1, 0, 0, 0]
        maxes = [0.8, 0.8, 1.0, 1.0, 1.0, 1.0, 0.5, 0.5, 1.0, 1.0, 0.8, 0.8, 0.6]
    if numStation == "195" or numStation=="215":
        mins = [0,0,0,0,0,0,0,0]
        maxes = [0.8,0.8,0.8,0.8,0.8,0.8,0.8,0.8]
    myName = numStation + "_" + line
    
    fig, ax = plt.subplots(rows, 1, figsize=(6,6))#, sharex= True)#, sharex='all')
    axisy = pd.DataFrame()
    axisx = DbForLineNmber['No']
    legend=[]
    fig.suptitle(myName)

    max_yticks = 5
    # print(range(1,rows+1))
    for col in range(1,rows+1): #transponowane bo inaczej wychodzi 24
        if col < 10:
            name = "ST0" + str(col)
        if col >= 10:
            name = "ST" + str(col)
            # print(DbForLineNmber.head())
        # plt.subplots()

        ax[col-1].xaxis.set_minor_locator(plt.MultipleLocator(5))
        ax[col-1].grid(which= 'minor', linestyle= '-.', linewidth=0.25, axis='x')
        ax[col-1].grid(which= 'major', linestyle= '-', linewidth=0.5)
        ax[col-1].set_ylabel(name + ' [mm]', fontsize=4)#, rotation=0)
        yloc = plt.MaxNLocator(max_yticks)
        ax[col-1].yaxis.set_major_locator(yloc)
        legend.append(name)
        # print(DbForLineNmber["ST01"])
        max = DbForLineNmber[name].max()
        min = DbForLineNmber[name].min()
        if np.isnan(max):
            max=1
            min=-1

        if max < maxes[col-1]+0.1:
            max = maxes[col-1]+0.1
        else: 
            max = max + 0.1
        if min > mins[col-1]-0.1:
            min = mins[col-1]-0.1
        else:
            min = min - 0.1
        
        ax[col-1].set_ylim(min,max)
        axisy[name] = DbForLineNmber[name].astype(float)
        if col != rows:
            ax[col-1].set_xticklabels([])
        upper = np.linspace(maxes[col-1],maxes[col-1],axisx.size)
        lower = np.linspace(mins[col-1], mins[col-1], axisx.size)
        
        ax[col-1].plot(axisx, lower,  '-.',axisx, upper,  '-.',linewidth=0.5, color = 'red')
        ax[col-1].plot(axisx,axisy[name], linewidth = 0.8 )
   
    # graphName = subframe.nameGraph(sta)
    graphName = my_subframe.nameGraph(numStation, line)  
    # print(my_subframe.nameGraph(numStation, line))
    # graphName = name_files("","Graphs","_" + myName + ".png")# + ".png"
    
    try:
        fig.savefig(graphName, dpi=300, format='png')
    except:
        no_file(graphName)