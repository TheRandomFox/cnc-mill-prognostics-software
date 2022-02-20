"""
title: Milling machine prognostics program
author: Abdul Halim bin Slamat
std no.: 9664005
cohort: FT/CS119

Original dataset & report can be acquired at: https://ti.arc.nasa.gov/c/4/
"""

#import packages
from sys import exit
from scipy.io import loadmat
#import matplotlib

#read file; extract contents of 'mill' key and unused flat dimension
#original format == dict, read from MATLAB array
#new format == numpy array
try:
    milldat = loadmat('mill.mat')
    milldat = milldat['mill'][0]
except:
    exit('Error: No file detected.')

#exploring data
""" milldat structure

milldat[x][y][z]:
x = experiment index, len==167 (each case done multiple times, varying by duration)
y = field index, len==13
z = experiment data index for y=7:12, len==9000; for y=0:6, len==1

field legend:
0 = case            type of experiment being run; defines DOC, feed & material
1 = run             no. of experiment runs in each case
2 = VB              flank wear, mm (dist from cutting edge to abrasive wear on flank of tool)
3 = time            duration, s
4 = DOC             depth of cut, mm
5 = feed            rate of traversal thru material, mm/min
6 = material        material being cut (1=cast iron, 2=steel)
7 = smcAC           spindle motor current AC, Amp
8 = smcDC           spindle motor current DC, Amp
9 = vib_table       Table vibration, kHz
10 = vib_spindle    Spindle vibration, kHz
11 = AE_table       Acoustic emission at table, kHz
12 = AE_spindle     Acoustic emission at spindle, kHz

Note:
    According to the dataset readme, for some of the experiments t or VB are empty because they were not measured.
    The program will ignore these cases.
"""

#select features to use
#current:    feats_curr = DOC, feed, material, vb, time, smcac, smcdc
#vibration:  feats_vib = DOC, feed, material, vb, time, vib_table, vib_spindle
#acoustic:   feats_ae = DOC, feed, material, vb, time,  ae_table, ae_spindle

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
        feats.append(milldat[x][4][0])      #DOC
        feats.append(milldat[x][5][0])      #feed
        feats.append(milldat[x][2][0])      #vb
        feats.append(milldat[x][3][0])      #time

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
'''
Y-axis: rate of wear = dVB/dt
X-axis: feed,
remaining useful life => not obtainable. insufficient information.
'''

#divide data sets into training & testing groups


#visualise data

#train algorithm
#alg used:


#print training result
#print('X-intercept: ', reg.intercept_)
#print('Coefficient: ', reg.coef_)


#Root mean squared error
