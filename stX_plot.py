from name_files import name_files
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# FS ST01(0 0.8),ST02(0 0.8),ST03(0 1.0),ST04(0 1.0),ST05(-1.0 1.0),ST06(-1.0 1.0),ST07(-1.0 0.5),ST08(-1.0 0.5),ST09(-1.0 1.0),ST10(-1.0 1.0),ST11(0 0.8),ST12(0 0.8),ST13(0 0.6)
from column_count import column_count

min = [0, 0, 0, 0, -1, -1, -1, -1, -1, -1, 0, 0, 0]
max = [0.8, 0.8, 1.0, 1.0, 1.0, 1.0, 0.5, 0.5, 1.0, 1.0, 0.8, 0.8, 0.6]

def stX_plot(db, line):
    if line == "A1":
        short = "7"
    if line == "A2":
        short = "8"
    if line == "A3":
        short = "9"   
    # plt.style.use("seaborn")
    plt.rc('ytick', labelsize=6) 

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
    fig.suptitle(myName)

    # plt.minorticks_on()
    max_yticks = 5
    
    for col in range(1,rows+1): #transponowane bo inaczej wychodzi 24
        name = "ST0" + str(col)
        ax[col-1].xaxis.set_minor_locator(plt.MultipleLocator(5))
        ax[col-1].grid(which= 'minor', linestyle= '-.', linewidth=0.25, axis='x')
        ax[col-1].grid(which= 'major', linestyle= '-', linewidth=1)
        ax[col-1].set_ylabel(name + ' [mm]', fontsize=5)#, rotation=0)
        yloc = plt.MaxNLocator(max_yticks)
        ax[col-1].yaxis.set_major_locator(yloc)
        legend.append(name)
        max = DbForLineNmber[name].max()
        min = DbForLineNmber[name].min()
        if max < 0.9:
            max = 0.9
        else: 
            max = max + 0.1
        if min > -0.1:
            min = -0.1
        else:
            min = min - 0.1
        ax[col-1].set_ylim(min,max)
        axisy[name] = DbForLineNmber[name].astype(float)
        if col != rows:
            ax[col-1].set_xticklabels([])
        upper = np.linspace(0.8, 0.8,axisx.size)
        lower = np.linspace(0, 0, axisx.size)
        
        ax[col-1].plot(axisx, lower,  '-.',axisx, upper,  '-.',linewidth=0.5, color = 'red')
        ax[col-1].plot(axisx,axisy[name])
    graphName = name_files("","Graphs","_" + myName + ".png")# + ".png"
    fig.savefig(graphName, dpi=300, format='png')
