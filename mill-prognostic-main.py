"""
title: Milling machine prognostics program
author: Abdul Halim bin Slamat
std no.: 9664005
cohort: FT/CS119

Original dataset & report can be acquired at: https://ti.arc.nasa.gov/c/4/
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
#reformat to numpy array
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
df_mill.index = range(len(milldat))
df_mill.columns = fields[0:7]

#visualise dataframe table
print(df_mill)

#plot graph of VB/t for case 1
cs1_vb = []; cs1_t = []
for cn in range(0,12):
    dat = []
    cs1_vb.append(df_mill.at[cn,'VB'])
    cs1_t.append(df_mill.at[cn,'time'])
plt.plot(cs1_t, cs1_vb, '-')
plt.xlabel('Time (s)')
plt.ylabel('Tool wear (mm)')

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
