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
import pandas as pd
import functions

#read file; extract contents of 'mill' key and unused flat dimension
#original format == dict, from MATLAB array
#Convert to numpy.ndarray
try:
    milldat = loadmat('mill.mat')
    milldat = milldat['mill'][0]
except:
    exit("Error: 'Mill.mat' either does not exist or could not be read.")


df_mill = prepData(milldat)
print(df_mill)

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
