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
#import matplotlib

#read file; extract contents of 'mill' key and unused flat dimension
#original format == dict, from MATLAB array
#reformat to numpy array
try:
    milldat = loadmat('mill.mat')
    milldat = milldat['mill'][0]
except:
    exit("Error: 'Mill.mat' either does not exist or could not be read.")

#select features to use
#current:    feats_curr = feed, material, vb, time, smcac, smcdc
#vibration:  feats_vib = feed, material, vb, time, vib_table, vib_spindle
#acoustic:   feats_ae = feed, material, vb, time,  ae_table, ae_spindle

#for each experiment run, separate by material and append to relevant feats array
feats_curr_iron = []
feats_curr_steel = []
feats_vib_iron = []
feats_vib_steel = []
feats_ae_iron = []
feats_ae_steel = []

feats = []
for i in range(3):
    for x in range(len(milldat)):
        if milldat[x][2][0] > 0 and milldat[x][3][0] > 0:    #if contains valid values for time and VB; else skip.
            feats.append(milldat[x][2][0])      #vb
            feats.append(milldat[x][3][0])      #time
            feats.append(milldat[x][5][0])      #feed

            if i == 0:      #current feats
                feats.append(milldat[x][7].flatten())   #smcAC
                feats.append(milldat[x][8].flatten())   #smcDC
                if milldat[x][6][0] == 1:               #material == castiron
                    feats_curr_iron.append(feats)
                else:                                   #material == steel
                    feats_curr_steel.append(feats)

            elif i == 1:    #vib feats
                feats.append(milldat[x][9].flatten())   #vib_table
                feats.append(milldat[x][10].flatten())  #vib_spindle
                if milldat[x][6][0] == 1:
                    feats_vib_iron.append(feats)
                else:
                    feats_vib_steel.append(feats)

            else:           #ae feats
                feats.append(milldat[x][11].flatten() )   #ae_table
                feats.append(milldat[x][12].flatten() )   #ae_spindle
                if milldat[x][6][0] == 1:
                    feats_ae_iron.append(feats)
                else:
                    feats_ae_steel.append(feats)

            feats = []   #reset feats

#input features


#output features
#remaining useful life => not obtainable. insufficient information.
'''
Table A:
    X-axis: rate of wear = dVB/dt
    Y-axis: rate of traversal = DOC/t
'''

'''
Table B:
    X-axis: rate of wear = dVB/dt
    Y-axis: motor current = smcAC, smcDC
'''

'''
Table C:
    X-axis: rate of wear = dVB/dt
    Y-axis: equipment vibration = vib_table, vib_spindle
'''

'''
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
