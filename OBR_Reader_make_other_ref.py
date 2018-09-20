import numpy as np
import math
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from itertools import product, combinations
import csv
import sys
from ReaderFunctions.ReaderFunctions import readers as rdr
import os

startdistance=0.0 #mm
length=120.0 #mm
key='E01_fibre 1_'
prefix=key
path=r'C:\Users\eivinhug\OneDrive - NTNU\PhD_Backup\NTNU\PhD\Testing\Laminate_E\OBR_Files\E01_FatigueTest_2_28082018\RAW'
rdr=rdr()

highest_numbers=np.arange(13,174,10)
start_heres=np.arange(5,166,10)
zeroreading=4

load_file_number = str(zeroreading).zfill(4)
file=prefix+load_file_number+'_Lower.txt'
Zerodoods=rdr.Lower_Reader(location='%s\%s' %(path, file))
ZeroStrain=Zerodoods[1]
ZeroLength=Zerodoods[0]

for i in range(0,len(highest_numbers)):
    
    start=start_heres[i]
    stop=highest_numbers[i]


    Strain=[]
    for i in range(start,stop+1,1):
      
        OldStrain=ZeroStrain
        
        if i>start:
            Old_load_file_number = str(i-1).zfill(4)
            Oldfile=prefix+Old_load_file_number+'_Lower.txt'
            Old_dood=rdr.Lower_Reader(location='%s\%s' %(path, Oldfile))
            OldStrain=Old_dood[1]
            
        load_file_number = str(i).zfill(4)
        file=prefix+load_file_number+'_Lower.txt'
        dood=rdr.Lower_Reader(location='%s\%s' %(path, file))
        
        Length=dood[0]
        Strain=dood[1]
        
        theotherfile=open(os.path.join(path,prefix+str(i).zfill(4)+'_older_reference_Lower.txt'), 'w') #extra
        theotherfile.write("Length (m)	Strain (microstrain)	") 
        theotherfile.write("\n")   
        
        for t in range(len(ZeroLength)-1):
            theotherfile.write("%.6f"%ZeroLength[t])
            theotherfile.write("\t")    
            theotherfile.write("%.6f"%(Strain[t]+OldStrain[t]))
            theotherfile.write("\n")                    
