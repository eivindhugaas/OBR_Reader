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
path=r'C:\Users\eivinhug\OneDrive - NTNU\PhD_Backup\NTNU\PhD\Testing\Laminate_E\OBR_Files\E01_FatigueTest_2_28082018'
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

    filename="Output_Summed_"+str(prefix)+str(start)+"_"+str(stop)+".txt"
    
    print(path+filename)
    
    thefile = open(os.path.join(path,filename), 'w')
    thefile.write("Length (m) \t") 
    for i in range(start,stop+1,1):
        thefile.write("Measurement %s (microstrain)\t"%int(i))  
    thefile.write("\n")
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

    print(AllStrain)
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
    
