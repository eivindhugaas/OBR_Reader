import numpy as np
import math
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from itertools import product, combinations
import csv
import sys
from ReaderFunctions.ReaderFunctions import readers as rdr
import os

key='E07_fibre 2_'
prefix=key
path=r'C:\Users\eivinhug\OneDrive - NTNU\PhD\Testing\Laminate_E\OBR_Files\E07_Fatigue_14092018\Processesed'
rdr=rdr()

start_heres=np.arange(17,318,12)
highest_numbers=np.arange(27,328,12)
zeroreading=17

load_file_number = str(zeroreading).zfill(4)
file=prefix+load_file_number+'_Lower_Smooth.txt'
doods=rdr.Lower_Reader(location='%s\%s' %(path, file))
print(doods)
PastStrain=doods[1]
#Result=rdr.SeriesReader(location=r'C:\Users\eivinhug\NTNU\PhD\Testing\Laminate_D\OBR_Files\D01_Temsion_07062018',key=key,startdistance=startdistance,length=length)



for i in range(0,len(highest_numbers)):
    
    StrainSummed=doods[1]
    start=start_heres[i]
    stop=highest_numbers[i]

    filename="Output_Summed_"+str(prefix)+str(start)+"_"+str(stop)+".txt"
    
   
    
    thefile = open(os.path.join(path,filename), 'w')
    thefile.write("Length (m) \t") 
    for i in range(start,stop+1,1):
        thefile.write("Measurement %s (microstrain)\t"%int(i))  
    thefile.write("\n")
    AllStrain=[]
    Strain=[]
    for i in range(start,stop+1,1):
        load_file_number = str(i).zfill(4)
        file=prefix+load_file_number+'_Lower_Smooth.txt'
        print(file)
        dood=rdr.Lower_Reader(location='%s\%s' %(path, file))
        print(dood)
        if i==start:
            Length=dood[0]
            AllStrain.append(Length)
        Strain=dood[1]
        StrainSummed=[StrainSummed[a]+Strain[a] for a in range(len(Strain))]#[x + y for x, y in zip(Strain,PastStrain)]
        AllStrain.append(StrainSummed)

    for t in range(len(Length)-1): #-1 to avoid number of datpoints issues.
        for d in range(len(AllStrain)):
            if AllStrain[d]==[]:
                thefile.write("0.000000")
                thefile.write("\t")
            else:
                thefile.write("%.6f"%AllStrain[d][t])
                thefile.write("\t")
        thefile.write("\n")    
    
    
    #ResultSmooth=rdr.Smoother(Result=Result[0],FiberNumbers=Result[1],Fibersforsmoothing=[9],algorithm='threshold')
    #rdr.Plotter(Result=Result[0],FiberNumbers=Result[1])
    #rdr.Plotter(Result=ResultSmooth,FiberNumbers=Result[1])
    #rdr.ContourPlotter(Result=ResultSmooth,FiberNumbers=Result[1],FiberPositions=Result[2])
    #rdr.SurfacePlotter(Result=Result[0],FiberNumbers=Result[1],FiberPositions=Result[2])
    #rdr.SurfacePlotter(Result=ResultSmooth,FiberNumbers=Result[1],FiberPositions=Result[2])
    #rdr.Writer(Result=Result[0],FiberNumbers=Result[1],Filename=key)
    #rdr.ContourPlotter(Result=ResultSmooth,FiberNumbers=Result[1],FiberPositions=Result[2])
    
