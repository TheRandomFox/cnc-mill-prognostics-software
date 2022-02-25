"""
title: Milling machine prognostics program
author: Abdul Halim bin Slamat
std no.: 9664005
cohort: FT/CS119

Original dataset & report can be acquired at: https://ti.arc.nasa.gov/c/4/
Credit: K.Goebel & A.Agogino
"""

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import feature_selection as fs
from sklearn.pipeline import Pipeline

def prepData(milldat):
    '''
    Takes the raw data and prepares it for use.
    Find and get rid of corrupt or unusable indexes.

    Parameters:
        milldat : ndarray

    Returns:
        dfmill : pandas.DataFrame() object
        milldat : ndarray
    '''
    #identify fields and store label names
    fields = milldat.dtype.names

    #new Pandas dataframe
    dfmill = pd.DataFrame()

    #remove corrupt/unusable indexes
    milldat = np.delete(milldat,[17,94,105],0)

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
        dfmill[y] = dat

    #set row & column labels
    dfmill.index = range(len(dfmill))     #X-axis labels
    dfmill.columns = fields[0:7]          #Y-axis labels

    #visualise dataframe table
    print('Visualise dataset labels:\n', dfmill,'\n\n')

    return dfmill, milldat

def sensorsArray(milldat):
    '''Extract sensor readings from milldat and put them in
    their own array.

    Params:
        milldat : ndarray

    Returns:
        sarray : list
    '''
    sarray = [['Motor current AC',
               'Motor current DC',
               'Vibration table',
               'Vibration spindle',
               'AE table',
               'AE spindle']]
    for mdx in range(len(milldat)):
        for mdy in range(7,12):
            arr = []
            arr.append(milldat[mdx][mdy][0][1000::])
            #ignore the first 1000 readings as the milling machine had not started yet
        sarray.append(arr)
    #make sure it's the right shape
    sarray = np.reshape(sarray, (len(milldat),6))
    return sarray


def train(milldat):
    #train algorithm
    #alg used:
    #divide data sets into training & testing groups
    #split training/testing data by index
    #mill_index = range(len(milldat))

    x_train, x_test = train_test_split(() )


    #feats = Pipeline( )



#print training result
#print('X-intercept: ', reg.intercept_)
#print('Coefficient: ', reg.coef_)