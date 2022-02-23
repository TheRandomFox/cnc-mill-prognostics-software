title: 		Milling machine prognostics program
author: 	Abdul Halim bin Slamat
std no.: 	9664005
cohort: 	FT/CS119

repo:		https://github.com/TheRandomFox/cnc-mill-prognostics-software
****************************************

Original dataset & report can be acquired at: https://ti.arc.nasa.gov/c/4/
Credit: A. Agogino and K. Goebel (2007). BEST lab, UC Berkeley.

****************************************
INTRODUCTION:
The purpose of this program is to use machine learning in an attempt to predict the state of wear for CNC milling machine tools by finding correlations between the degree of wear on the tool against sensor data collected from the spindle motor current, and the vibration and noise emission of the spindle and working table.

The original objective was to find to remaining useful lifespan of the tool, i.e. the remaining time until the predicted point of failure at the currect rate of use. However this would turn out to be unobtainable as I lacked several critical points of value necessary for the calculation. These values are intrinsic properties of the individual tool types and the worked material, and thus cannot be derived from the data that I have.
Therefore the objective was changed to instead attempt to predict the current state of wear on the tool based on sensor data input.

****************************************

REQUIREMENTS:
	NumPy
	Scipy
	Sklearn
	Pandas
	Matplotlib
	
****************************************

Reads mill.mat file
Original format == dict, read from MATLAB array
Convert into Pandas dataframe


##### milldat structure #####
milldat[x][y][z][0]:
x = experiment index, len==167 (each case measured multiple times as duration progresses)
y = field index, len==13
z = sensor data index for y=7:12, len==9000; for y=0:6, len==1
[0] = for some reason each individual value in each list is in a (1,) array; Must use a 4th dimension to extract the values.

field legend:
0 = case            type of experiment being run; defines DOC, feed & material
1 = run             iterative counter for experiment recording in each case
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

x==17, 94 & 105 contain corrupt or otherwise unsuitable data and will be removed from the dataframe.
##############################

