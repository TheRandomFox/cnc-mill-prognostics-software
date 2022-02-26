"""
title: Milling machine prognostics program
author: Abdul Halim bin Slamat
std no.: 9664005
cohort: FT/CS119

Original dataset & attached report can be acquired at: https://ti.arc.nasa.gov/c/4/
Credit: K.Goebel & A.Agogino
"""

#import packages
import plotdata as pl
import machineLearning as ml
from sys import exit
from scipy.io import loadmat


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

#Prepare data : create dataframes, remove unusable indexes from milldat
milldat, df_x1, df_x2, df_y = ml.prepData(milldat)

predict = ml.train(df_x1,df_x2,df_y)
#Main program loop
'''
while isRunning == 1:
    #main menu
    print('========================================\n'
          'To view sample data from 1 cut, enter "1"\n'
          'To show prediction accuracy result, enter "2"\n'
          ''
          'To exit program, enter "exit"\n'
          '========================================\n')
    cmd = str.lower(input())
    if cmd == '1':
        cutNo = int(input('\nView which cut? (1-',len(milldat),'): '))-1
        pl.plotGraph(milldat,cutNo)
    elif cmd == '2':
        #prediction
        predict = ml.train(milldat,sarray)
    elif cmd == 'exit':
        ans = str.lower(input('Are you sure you want to close the program? (Y/N) '))
        if ans == 'n':
            break
        elif ans == 'y':
            isRunning = 0
            break
        else:
            print('Invalid input.\n\n')
    else:
        print('Invalid input.\n\n')
'''