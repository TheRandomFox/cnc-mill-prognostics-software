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

#read file; extract contents of 'mill' key and unused flat dimension
#original format == dict, from MATLAB array
#reformat to numpy array
try:
    milldat = loadmat('mill.mat')
    milldat = milldat['mill'][0]
except:
    exit("Error: 'Mill.mat' either does not exist or could not be read.")

#extract data to be used into individual cases.

case1 = []; case2 = []; case3 = []; case4 = []; case5 = []; case6 = []; case7 = []; case8 = []
case9 = []; case10 = []; case11 = []; case12 = []; case13 = []; case14 = []; case15 = []; case16 = []

for x in range(len(milldat)):
    if milldat[x][2][0] > 0:    #if contains valid values for VB; else skip.
        for y in range(12):
            if milldat[x][0] == 1:
                case1.append(milldat[x][y+1])
            elif milldat[x][0] == 2:
                case2.append(milldat[x][y+1])
            elif milldat[x][0] == 3:
                case3.append(milldat[x][y+1])
            elif milldat[x][0] == 4:
                case4.append(milldat[x][y+1])
            elif milldat[x][0] == 5:
                case5.append(milldat[x][y+1])
            elif milldat[x][0] == 6:
                case6.append(milldat[x][y+1])
            elif milldat[x][0] == 7:
                case7.append(milldat[x][y+1])
            elif milldat[x][0] == 8:
                case8.append(milldat[x][y+1])
            elif milldat[x][0] == 9:
                case9.append(milldat[x][y+1])
            elif milldat[x][0] == 10:
                case10.append(milldat[x][y+1])
            elif milldat[x][0] == 11:
                case11.append(milldat[x][y+1])
            elif milldat[x][0] == 12:
                case12.append(milldat[x][y+1])
            elif milldat[x][0] == 13:
                case13.append(milldat[x][y+1])
            elif milldat[x][0] == 14:
                case14.append(milldat[x][y+1])
            elif milldat[x][0] == 15:
                case15.append(milldat[x][y+1])
            else:
                case16.append(milldat[x][y+1])

#get mean and standard deviation for sensor data for each run


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
