import numpy as np
import math
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from itertools import product, combinations
import csv
import sys
from ReaderFunctions.ReaderFunctions import readers as rdr
import os
import pandas

loadlevel="1-0mm"
startdistance=0.0 #mm
length=120.0 #mm
key='E01_fibre 1_'
prefix=key
path=r'C:\Users\eivinhug\OneDrive - NTNU\PhD_Backup\NTNU\PhD\Testing\Laminate_E\OBR_Files\E01_FatigueTest_2_28082018'
rdr=rdr()

highest_numbers=np.arange(13,174,10)
start_heres=np.arange(5,166,10)
Measurements=np.arange(5+8,166+8,10)
zeroreading=4

load_file_number = str(zeroreading).zfill(4)
file=prefix+load_file_number+'_Lower.txt'
doods=rdr.Lower_Reader(location='%s\%s' %(path, file))
PastStrain=doods[1]


for i in range(0,len(Measurements)):
    
    StrainSummed=doods[1]
    start=start_heres[i]
    stop=highest_numbers[i]
    filename="Output_Summed_"+str(prefix)+str(start)+"_"+str(stop)+".txt"
        
    res=rdr.Output_Reader_pick_Measurement(location=os.path.join(path,filename),Measurement=Measurements[i])

    if i==0:
        Strain=[res[0]]
        
    
    Strain.append(res[1])

Newfilename="Output_"+str(prefix)+"at_LoadLevel_"+str(loadlevel)+".txt"
thefile = open(os.path.join(path,Newfilename), 'w')


thefile.writelines('\t'.join(str(elem) for elem in row) + '\n' for row in list(map(list, zip(*Strain))))
