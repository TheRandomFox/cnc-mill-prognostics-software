"""
title: Milling machine prognostics program
author: Abdul Halim bin Slamat
std no.: 9664005
cohort: FT/CS119

Original dataset & report can be acquired at: https://ti.arc.nasa.gov/c/4/
Credit: K.Goebel & A.Agogino
"""

import matplotlib.pyplot as plt
import seaborn as sb
import numpy as np

def plotGraph(milldat, cutNo):
    '''
    Visualise data for a given cut number

    Parameters:
        milldat : ndarray
        cutNo : int

    Returns:
        void
    '''

    datlabels = ['AC motor current',
                 'DC motor current',
                 'Vibration at table',
                 'Vibration at spindle',
                 'AE at table',
                 'AE at spindle']

    #generate 6 graphs in a column
    fig, axs = plt.subplots(6, 1, sharey=True, linewidth=0.5, figsize=[4,5], dpi=150)
    sb.set_theme(context='notebook', font_scale=0.5)

    axs[0].set_title('Cut #'+ str(cutNo+1), fontsize='medium')

    #define axes for each graph
    for i in range(6):
        #x divisions: seconds == no. of readings/Hertz
        axs[i].plot(np.arange(0,len(milldat[cutNo][i+7]))/250, milldat[cutNo][i+7])

        #set Y label name
        axs[i].set_ylabel(datlabels[i], fontsize='small')

        #set X label name at the bottom
        if i < 5:
            #if not at bottom, don't show borders
            axs[i].spines[:].set_visible(False)
            axs[i].set_xticks([])
        else:
            #if at bottom, show bottom border
            axs[i].spines[['top','left','right']].set_visible(False)
            axs[i].spines['bottom'].set_visible(True)
            axs[i].set_xlabel('Time (s)', size=5)


    plt.show()

