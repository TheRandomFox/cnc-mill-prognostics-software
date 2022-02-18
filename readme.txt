title: 		Milling machine prognostics program
author: 	Abdul Halim bin Slamat
std no.: 	9664005
cohort: 	FT/CS119
****************************************

Original dataset & report can be acquired at: https://ti.arc.nasa.gov/c/4/
Credit: A. Agogino and K. Goebel (2007). BEST lab, UC Berkeley.

# read mill.mat file; extract contents of 'mill' key and unused flat dimension
# original format == dict, read from MATLAB array
# new format == numpy array

# milldat structure
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