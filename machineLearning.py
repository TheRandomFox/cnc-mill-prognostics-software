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
import sklearn.tree
import sklearn.naive_bayes as nb
from sklearn.metrics import accuracy_score
#from sklearn.pipeline import Pipeline

def prepData(milldat):
    '''
    Takes the raw data and prepares it for use.
    Find and get rid of corrupt or unusable indexes.
    df_x1 = feed, DOC, material : input 1
    df_x2 = signal data vals    : input 2
    df_y = VB labels            : output

    Parameters
    ----------
    milldat : ndarray

    Returns
    ----------
    milldat : ndarray
    df_x1, df_x2, df_y : DataFrame
    '''

    #remove corrupt/unusable indexes
    milldat = np.delete(milldat,[17,94,105],0)

    #new Pandas dataframes
    df_x1 = pd.DataFrame()
    df_x2 = pd.DataFrame()
    df_y = pd.DataFrame()

    def classify_wear_state(vb):
        '''
        Assigns labels to VB values based on degree of wear.
        Classification:
            VB				| Label
            VB < 0.2 		: 'Good'
            0.2 <= VB < 0.6	: 'Fair'
            0.6 <= VB < 0.8	: 'Degraded'
            VB >= 0.8		: 'Failed'
        Note: The thresholds chosen for VB are just dummy values for the purpose of this project.

        Parameters
        ----------
        vb : float

        Returns
        ----------
        vb_label : string
        '''
        if vb < 0.2:
            return 'Good'
        elif vb < 0.4:
            return 'Fair'
        elif vb < 0.6:
            return 'Degraded'
        elif vb < 0.8:
            return 'Critical'
        else:
            return 'Failed'

    #populate df_y, df_x1, df_x2
    dat = []
    for x in range(len(milldat)):   #y
        #in VB, replace any NaN values with zeros
        if np.isnan(milldat[x][2][0][0]) == True:
            milldat[x][2][0][0] = 0
        vb_label = classify_wear_state(milldat[x][2][0][0])
        dat.append(vb_label)
    df_y[0] = dat

    dx = 0  #index counter
    for y in range(4,7):    #x1
        dat = []    #reset dat
        for x in range(len(milldat)):
            dat.append(milldat[x][y][0][0])
        df_x1[dx] = dat
        dx = dx+1

    dx = 0
    for y in range(7,13):   #x2
        dat = []    #reset dat
        for x in range(len(milldat)):
            dat.append(milldat[x][y][0][0])
        df_x2[dx] = dat
        dx = dx+1

    #visualise dataframe table
    print('Visualise dataset labels:\n\n')
    print('X1:\n', df_x1,'\n')
    print('X2:\n', df_x2,'\n')
    print('Y:\n', df_y,'\n')

    return milldat, df_x1, df_x2, df_y


def sensorsArray(milldat):
    '''Extract sensor readings from milldat and put them in
    their own array.

    Parameters:
        milldat : ndarray

    Returns:
        sarray : ndarray
    '''
    datlen = len(milldat)
    sarray = []
    for mdx in range(datlen):
        for mdy in range(7,12):
            arr = []
            arr.append(milldat[mdx][mdy][0][1001::])
            #ignore the first 1000 readings as the milling machine had not started yet
        sarray.append(arr)
    #make sure it's the right shape
    print(sarray)
    sarray = np.array(sarray)

    #sarray = np.reshape(sarray, (datlen,6))
    return sarray


def train(df_x1, df_x2, df_y):
    '''
    Feature selection and training the algorithm.

    Parameters
    ----------
    df_x1 : DataFrame (164,3)
    df_x2 : DataFrame (164,6)
    df_y : Dataframe (164,1)

    Returns
    -------
    None.
    '''
    #remaining useful life => not obtainable. insufficient information.

    #divide data sets into training & testing groups
    feats1_train, feats1_test, labels_train, labels_test = train_test_split(df_x1, df_y, test_size=0.1)
    feats2_train, feats2_test, labels_train, labels_test = train_test_split(df_x2, df_y, test_size=0.1)

    #prediction x1
    clf1 =
    clf1.fit(feats1_train, labels_train)
    pred1 = clf1.predict(feats1_train)

    #determine accuracy rate x1
    acc = accuracy_score(pred1, labels_test)
    print(acc)
    #Root mean squared error




#print training result
#print('X-intercept: ', reg.intercept_)
#print('Coefficient: ', reg.coef_)