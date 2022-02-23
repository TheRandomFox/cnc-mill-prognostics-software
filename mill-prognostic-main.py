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
import matplotlib.pyplot as plt
import pandas as pd

#read file; extract contents of 'mill' key and unused flat dimension
#original format == dict, from MATLAB array
#Convert to numpy.ndarray
try:
    milldat = loadmat('mill.mat')
    milldat = milldat['mill'][0]
except:
    exit("Error: 'Mill.mat' either does not exist or could not be read.")

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
df_mill.index = range(len(milldat))     #X-axis labels
df_mill.columns = fields[0:7]          #Y-axis labels

#visualise dataframe table
print(df_mill,'\n\n')

print('Visualise data for a given cut number.\n')
cutNo = 166
plt.plot(milldat[cutNo][7], label='smcAC')
plt.plot(milldat[cutNo][8], label='smcDC')
plt.plot(milldat[cutNo][9], label='vib_table')
plt.plot(milldat[cutNo][10], label='vib_spindle')
plt.plot(milldat[cutNo][11], label='AE_table')
plt.plot(milldat[cutNo][12], label='AE_spindle')

#input features

#output features
#remaining useful life => not obtainable. insufficient information.
'''
Table A:
    X-axis: rate of wear = dVB/dt
    Y-axis: rate of traversal = DOC/t

Table B:
    X-axis: rate of wear = dVB/dt
    Y-axis: motor current = smcAC, smcDC

Table C:
    X-axis: rate of wear = dVB/dt
    Y-axis: equipment vibration = vib_table, vib_spindle

Table D:
    X-axis: rate of wear = dVB/dt
    Y-axis: noise emission = ae_table, ae_spindle
'''


#divide data sets into training & testing groups


#visualise data


#train algorithm
#alg used:


#print training result
#print('X-intercept: ', reg.intercept_)
#print('Coefficient: ', reg.coef_)


#Root mean squared error
