"""
title: Milling machine prognostics program
author: Abdul Halim bin Slamat
std no.: 9664005
cohort: FT/CS119

Original dataset & report can be acquired at: https://ti.arc.nasa.gov/c/4/
Credit: K.Goebel & A.Agogino
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def rootMeanSquare(sensorData):
    '''
    Input: array list [float]
    Calculates root mean square of all values in the given array
    '''
    rms = np.sum( np.square(sensorData) )
    rms = np.sqrt( rms/len(sensorData) )
    return rms

def prepData(ndarray):
    '''
    Takes the raw data and prepares it for use.
    Find and get rid of corrupt indexes.
    '''
    #identify fields and store label names
    fields = milldat.dtype.names
    print('List of field names:\n', fields, '\n')

    #new Pandas dataframe
    df_mill = pd.DataFrame()

    #extract label data into df_mill (not sensor data)
    #reshape table
    #x-axis: fields; y-axis: data values
    for y in range(7):
        #set/reset temp container
        dat = []
        for x in range(len(milldat)):
            dat.append(milldat[x][y][0][0])
        #make contents of dat a numpy array
        dat = np.array(dat)
        #insert into df_mill
        df_mill[y] = dat

    #set row & column labels
    df_mill.index = range(len(df_mill))     #X-axis labels
    df_mill.columns = fields[0:7]          #Y-axis labels

    #visualise dataframe table
    print(df_mill,'\n\n')

    return pd.Dataframe()