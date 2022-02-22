"""
title: Milling machine prognostics program
author: Abdul Halim bin Slamat
std no.: 9664005
cohort: FT/CS119

Original dataset & report can be acquired at: https://ti.arc.nasa.gov/c/4/
Credit: K.Goebel & A.Agogino
"""

import numpy as np

def rootMeanSquare(sensorData):
    '''
    Input: array list [float]
    Calculates root mean square of all values in the given array
    '''
    rms = 0
    for i in sensorData:
        rms = rms + (sensorData[i] * sensorData[i])
    rms = np.sqrt( rms/len(sensorData) )

    return rms
