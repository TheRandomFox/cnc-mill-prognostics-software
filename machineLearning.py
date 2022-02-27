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

from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.ensemble import AdaBoostClassifier
import sklearn.decomposition as dcomp
from sklearn.metrics import accuracy_score
#import sklearn.pipeline.Pipeline as pipe

def prepData(milldat):
    '''
    Takes the raw data and prepares it for use.
    Find and get rid of corrupt or unusable indexes.
    Apply StandardScaler to each dataframe
    df_x1 = feed, DOC, material : input 1
    df_x2 = signal data vals    : input 2
    df_y = VB labels            : output

    Parameters
    ----------
    milldat : ndarray

    Returns
    ----------
    milldat : ndarray
    dfs_x1, dfs_x2, dfs_y : DataFrame
    '''

    #remove corrupt/unusable indexes
    milldat = np.delete(milldat,[17,94,105],0)
    lenmill = len(milldat)
    #replace NaN indexes with mean values
    xnan = [] #store indexes with nan values
    vbmean = []
    for x in range(lenmill):
        if np.isnan(milldat[x][2][0][0]) == True:
            xnan.append(x)
        else:
            vbmean.append(milldat[x][2][0][0])
    vbmean = np.mean(vbmean)
    for i in range(len(xnan)):
        milldat[xnan[i]][2][0][0] = vbmean

    #populate df_y, df_x1, df_x2
    #y (164,1)
    dat = []
    for x in range(lenmill):
        yclass = classifyWearState(milldat[x][2][0][0])
        dat.append(yclass)
    df_y = pd.DataFrame(data=dat)

    #x1 (164,3)
    df_x1 = []
    for x in range(lenmill):
        dat = []
        for y in range(4,7):
            dat.append(milldat[x][y][0][0])
        df_x1.append(dat)
    df_x1 = pd.DataFrame(data=df_x1)

    #x2 (164,6)
    #divide into chunks of 250, pertaining to roughly 1s of readings each
    #T(total) = (9000-1000)/250Hz = 32s
    df_x2 = []
    for x in range(lenmill):
        dat = []
        for y in range(7,13):
            #ignore the first 1000 readings as the milling machine had not started yet
            dat.append(milldat[x][y][1001::][0])
        df_x2.append(dat)
    df_x2 = pd.DataFrame(data=df_x2)


    #Perform scaling by Standardization on X feats
    scaler = StandardScaler()
    df_x1 = scaler.fit_transform(df_x1)
    df_x2 = scaler.fit_transform(df_x2)
    #ensure Y is 1-D
    df_y = np.ravel(df_y)

    #visualise dataframe table
    #print('Visualise dataset labels:\n\n')
    #print('X1:\n', df_x1,'\n')
    #print('X2:\n', df_x2,'\n')
    #print('Y:\n', df_y,'\n')

    return milldat, df_x1, df_x2, df_y

def classifyWearState(vb):
    '''
    Assigns labels to VB values based on degree of wear.
    The thresholds chosen for VB are just dummy values for the purpose of this project.
    Classification:
        VB value		| Label
        VB < 0.2 		: 'Good'
        0.2 <= VB < 0.4	: 'Fair'
        0.4 <= VB < 0.6 : 'Degraded'
        0.6 <= VB < 0.8	: 'Critical'
        VB >= 0.8		: 'Failed'

    Parameters
    ----------
    vb : float

    Returns
    ----------
    yclass : string
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

def train(df_x1, df_x2, df_y):
    '''
    Feature selection and training the algorithm.

    Parameters
    ----------
    df_x1 : DataFrame (164,3)
    df_x2 : DataFrame (164,6)
    df_y : Dataframe (164,)
    xpredict : ndarray (1,9)

    Returns
    -------
    None.
    '''

    #divide data sets into training & testing groups
    X1_train, X1_test, y_train, y_test = train_test_split(df_x1, df_y, test_size=0.1)
    X2_train, X2_test, y_train, y_test = train_test_split(df_x2, df_y, test_size=0.1)

    #prediction x1
    cls1 = AdaBoostClassifier(n_estimators=100)
    cls1.fit(X1_train, y_train)
    pred1 = cls1.predict(X1_test)
    #prediction x2
    #clf2 = dcomp.FastICA(max_iter=200, tol=1e-3)
    #clf2.

    #determine accuracy rate
    acc1 = accuracy_score(pred1, y_test)
    print('X1 accuracy: ', round(acc1, 4))

    #Root mean squared error

