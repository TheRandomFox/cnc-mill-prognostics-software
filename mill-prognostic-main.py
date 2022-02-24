"""
title: Milling machine prognostics program
author: Abdul Halim bin Slamat
std no.: 9664005
cohort: FT/CS119

Original dataset & attached report can be acquired at: https://ti.arc.nasa.gov/c/4/
Credit: K.Goebel & A.Agogino
"""

#import packages
import plotdata
from sys import exit
from scipy.io import loadmat
import numpy as np
import pandas as pd

#read file; extract contents of 'mill' key and unused flat dimension
#original format == dict, from MATLAB array
#Converts to numpy.ndarray
try:
    milldat = loadmat('mill.mat')
    milldat = milldat['mill'][0]
except:
    exit("Error: 'Mill.mat' either does not exist or could not be read.")

print('Data file loaded successfully.\n\n')
isRunning = 1

def prepData(ndarray):
    '''
    Takes the raw data and prepares it for use.
    Find and get rid of corrupt indexes.
    '''
    global milldat
    #identify fields and store label names
    fields = milldat.dtype.names

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

#Main program loop
while isRunning == 1:
    #main menu
    print('========================================\n'
          'To view sample data from 1 cut, enter "1"\n'
          'To show prediction result, enter "2"\n'
          'To exit program, enter "exit"\n'
          '========================================\n')
    cmd = lower(input())
    if cmd == '1':
        cutNo = int(input('\nView which cut? (1-164):'))-1
        plotGraph(milldat,cutNo)
    elif cmd == '2':
        print('Not implemented yet...\n')
        #call prediction algorithm here
    elif cmd == 'exit':
        ask = lower(input('Are you sure you want to close the program? (Y/N) '))
        if ask == 'n':
            break
        elif ask == 'y':
            isRunning = 0
            break
        else print('Invalid input.\n\n')
    else print('Invalid input.\n\n')




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
