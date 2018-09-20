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
prefix='E01_fibre 1_'
path=r'C:\Users\eivinhug\OneDrive - NTNU\PhD_Backup\NTNU\PhD\Testing\Laminate_E\OBR_Files\E01_FatigueTest_2_28082018\RAW'
rdr=rdr()

highest_numbers=np.arange(13,174,10)
start_heres=np.arange(5,166,10)
zeroreading=4

load_file_number = str(zeroreading).zfill(4)
file=prefix+load_file_number+'_Lower.txt'
doods=rdr.Lower_Reader(location='%s\%s' %(path, file))
print(doods)
PastStrain=doods[1]
#Result=rdr.SeriesReader(location=r'C:\Users\eivinhug\NTNU\PhD\Testing\Laminate_D\OBR_Files\D01_Temsion_07062018',key=key,startdistance=startdistance,length=length)

for i in range(0,len(highest_numbers)):
    
    StrainSummed=doods[1]
    start=start_heres[i]
    stop=highest_numbers[i]
    AllStrain=[]
    Strain=[]
    
    for i in range(start,stop+1,1):
        load_file_number = str(i).zfill(4)
        file=prefix+load_file_number+'_Lower.txt'
        dood=rdr.Lower_Reader(location='%s\%s' %(path, file))
        if i==start:
            Length=dood[0]
            AllStrain.append(Length)
        Strain=dood[1]
        StrainSummed=[StrainSummed[a]+Strain[a] for a in range(len(Strain))]#[x + y for x, y in zip(Strain,PastStrain)]

        AllStrain.append(StrainSummed)
    
    for d in range(1,len(AllStrain)):
        theotherfile=open(os.path.join(path,prefix+str(d+start-1).zfill(4)+'_Lower_summed.txt'), 'w') #extra
        print(prefix+str(d+start-1).zfill(4)+'_Lower_summed.txt')
        theotherfile.write("Length (m)	Strain (microstrain)	")            
        theotherfile.write("\n")            
        for t in range(len(Length)-1):
            theotherfile.write("%.6f"%AllStrain[0][t])
            theotherfile.write("\t")    
            theotherfile.write("%.6f"%(AllStrain[d][t]))
            theotherfile.write("\n")
        theotherfile.close()
    
