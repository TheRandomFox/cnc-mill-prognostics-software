"""
title: Milling machine prognostics program
author: Abdul Halim bin Slamat
std no.: 9664005
cohort: FT/CS119

Original dataset & report can be acquired at: https://ti.arc.nasa.gov/c/4/
Credit: K.Goebel & A.Agogino
"""

import matplotlib.pyplot as plt
import matplotlib.axes as ax
import matplotlib.spines
import numpy as np

def plotGraph(ndarray, int):
    '''
    Visualise data for a given cut number
    '''
    global milldat, cutNo
    datlabels = ['AC motor current',
                 'DC motor current',
                 'Vibration at table',
                 'Vibration at spindle',
                 'AE at table',
                 'AE at spindle']

    #generate 6 graphs in a column
    fig, axs = plt.subplots(6, 1, sharey=True, figsize=[4,6], dpi=130,
                            frameon=False)
    axs.set_title('Cut #'+ cutNo)

    #define axes for each graph
    for i in 6:
        #x divisions: seconds == no. of readings/Hertz
        axs[i].plot(np.arange(0,9000)/250, milldat[cutNo][i+7])

        #set Y label name
        axs[i].set_ylabel(datlabels[i])

        #set X label name at the bottom
        if i < 5:
            #if not at bottom, don't show borders
            axs.spines[:].set_visible(False)
            axs.set_xticks(labels=None)
            axs.set_yticks(labels=None)
        else:
            #if at bottom, show bottom border
            axs.spines[['top','left','right']].set_visible(False)
            axs.spines['bottom'].set_visible(True)
            axs[i].set_xlabel('Time (s)')

    plt.show()

