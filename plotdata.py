"""
title: Milling machine prognostics program
author: Abdul Halim bin Slamat
std no.: 9664005
cohort: FT/CS119

Original dataset & report can be acquired at: https://ti.arc.nasa.gov/c/4/
Credit: K.Goebel & A.Agogino
"""

import mill-prognostic-main
import matplotlib.pyplot as plt
import matplotlib.axes as ax
import numpy as np

def plotGraph(ndarray, int):
    '''
    Visualise data for a given cut number
    '''
    global milldat, cutNo