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
import sklearn.kernel_ridge as krr
import sklearn.tree
from sklearn.metrics import accuracy_score
#from sklearn.pipeline import Pipeline

def prepData(milldat):
    '''
    Takes the raw data and prepares it for use.
    Find and get rid of corrupt or unusable indexes.
    df_x1 = feed, DOC, material; shape (164,:) : input 1
    df_x2 = signal data vals;    shape (164,:) : input 2
    df_y = VB;                   shape (:,164) : output

    Parameters:
        milldat : ndarray

    Returns:
        milldat : ndarray
        df_x1, df_x2, df_y : DataFrame object
    '''

    #remove corrupt/unusable indexes
    milldat = np.delete(milldat,[17,94,105],0)

    #new Pandas dataframes
    df_x1 = pd.DataFrame()
    df_x2 = pd.DataFrame()
    df_y = pd.DataFrame()

    #populate df_y, df_x1, df_x2
    for x in range(len(milldat)):   #y
        dat = []
        #in VB, replace any NaN values with zeros
        if np.isnan(milldat[x][2][0][0]) == True:
            milldat[x][2][0][0] = 0
        dat.append(milldat[x][2][0][0])
        df_y[0,x] = dat

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


def train(milldat, sarray):
    '''
    Feature selection and training the algorithm.
    feats in (x): sensor data ; feats out (y): VB

    Parameters
    ----------
    milldat : ndarray
    sarray : list

    Returns
    -------
    None.
    '''
    #output features
    #remaining useful life => not obtainable. insufficient information.
    X = sarray #shape=(164,6)
    y = [0, milldat[:][2][0][0]] #VB shape=(0,164)

    #divide data sets into training & testing groups
    features_train, features_test, labels_train, labels_test = train_test_split(X, y, test_size=0.1, stratify=y)

    #prediction
    clf = krr()
    clf.fit(features_train, labels_train)
    pred = clf.predict(features_test)

    #determine accuracy rate
    acc = accuracy_score(pred, labels_test)
    print(acc)
    #Root mean squared error




#print training result
#print('X-intercept: ', reg.intercept_)
#print('Coefficient: ', reg.coef_)