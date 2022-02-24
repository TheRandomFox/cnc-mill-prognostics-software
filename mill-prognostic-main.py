"""
title: Milling machine prognostics program
author: Abdul Halim bin Slamat
std no.: 9664005
cohort: FT/CS119

Original dataset & attached report can be acquired at: https://ti.arc.nasa.gov/c/4/
Credit: K.Goebel & A.Agogino
"""

#import packages
from sys import exit
from scipy.io import loadmat
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


#read file; extract contents of 'mill' key and unused flat dimension
#original format == dict, from MATLAB array
#Converts to numpy.ndarray
try:
    milldat = loadmat('mill.mat')
    milldat = milldat['mill'][0]
except:
    exit("Error: 'Mill.mat' either does not exist or could not be read.")

def prepData(ndarray):
    '''
    Takes the raw data and prepares it for use.
    Find and get rid of corrupt indexes.
    '''
    global milldat
    #identify fields and store label names
    fields = milldat.dtype.names
    print('List of field names:\n', fields, '\n')

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
    print(dfmill,'\n\n')

    return dfmill

dfmill = prepData(milldat)

'''#Visualise data for a given cut number.
cutNo = 166
print('Cut: ', cutNo)
plt.plot(milldat[cutNo][7], label='smcAC')
plt.plot(milldat[cutNo][8], label='smcDC')
plt.plot(milldat[cutNo][9], label='vib_table')
plt.plot(milldat[cutNo][10], label='vib_spindle')
plt.plot(milldat[cutNo][11], label='AE_table')
plt.plot(milldat[cutNo][12], label='AE_spindle')
plt.title(cutNo)
plt.legend()'''


#input features

#output features
#remaining useful life => not obtainable. insufficient information.



#divide data sets into training & testing groups


#visualise data


#train algorithm
#alg used:


#print training result
#print('X-intercept: ', reg.intercept_)
#print('Coefficient: ', reg.coef_)


#Root mean squared error
