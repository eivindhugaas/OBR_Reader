import numpy as np
import pandas as pd
import math
from numpy import *
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from itertools import product, combinations
import csv
import sys
from os import listdir
from os.path import isfile, join
from scipy.signal import savgol_filter
import pickle
plt.rcParams.update({'font.size': 30})
class readers:
    def __init__(self):
        Check="OK"

    def Lower_Reader(self,location='C:\file\you\wish\to\open.txt'):
        '''
        Takes one _lower.txt file, reads it and returns the length and strain as two arrays in one array.
        '''
        if isfile(location):
            f  = open(location, 'r') 
            lines=f.readlines()
            length=[]
            strain=[]
            startappending=False
            for i in range(len(lines)):
                if startappending:                                       #skips all text at start of file
                    length.append(float(lines[i].split('\t')[0]))        
                    strain.append(float(lines[i].split('\t')[1]))    
                if lines[i]=='Length (m)\tStrain (microstrain)\t\n':
                    startappending=True             
            f.close()        
            result=[length,strain]
        
        else:
            print('file %s not found, return empty result array' % location)
            result=[[],[]]

        return result
    
    def Output_Reader(self,location='C:\file\you\wish\to\open.txt'):
        '''
        Takes one Output txt file, reads it and returns the length and strain as arrays in one array.
        '''
        if isfile(location):
            f  = open(location, 'r') 
            lines=f.readlines()
            lengthandstrain=[]
            lengthandstrains=[]
            print(lines)
            for t in range(len(lines[1].split('\t'))-1):
                startappending=False
                for i in range(len(lines)):
                    if startappending:    #skips all text at start of file
                        print(lines[i].split('\t')[t])
                        lengthandstrain.append(float(lines[i].split('\t')[t]))           
                    if 'Length' in lines[i]:
                        startappending=True  
                lengthandstrains.append(lengthandstrain)
                lengthandstrain=[]
            f.close()        
            result=lengthandstrains
        
        else:
            print('file %s not found, return empty result array' % location)
            result=[[],[]]

        return result    
    
    def Output_Reader_pick_Measurement(self,location='C:\file\you\wish\to\open.txt',Measurement=10000001):
        '''
        Takes one Output txt file, reads it and returns the length and strain as arrays in one array.
        '''
        
        if isfile(location):
            f  = open(location, 'r') 
            lines=f.readlines()
            lengthandstrain=[]
            lengthandstrains=[]
            
            TopString=lines[0].split('\t')
            for n in range(len(TopString)):
                if TopString[n]=='Measurement %s (microstrain)'%Measurement:
                    measureindex=n
                    break
            
            for t in range(len(lines[1].split('\t'))-1):
                startappending=False
                for i in range(len(lines)):
                    if startappending:    #skips all text at start of file
                        lengthandstrain.append(float(lines[i].split('\t')[t]))           
                    if 'Length' in lines[i]:
                        startappending=True  
                lengthandstrain=lengthandstrain        
                lengthandstrains.append(lengthandstrain)
                lengthandstrain=[]
            f.close()        
            result=[lengthandstrains[0],lengthandstrains[n]]

        
        else:
            print('file %s not found, return empty result array' % location)
            result=[[],[]]
            
        

        return result      
    
    def Plotter(self,Result=[[0.0,1.1,2.2],[1000.3,1500.0,2000.1]],FiberNumbers=[]):
        '''
        Plots one series.
        '''

        fig = plt.figure()
        fig.suptitle('Strain along sample', fontsize=14, fontweight='bold')
        if len(Result[1])>1:
            for i in range(len(Result[1])):
                plt.plot(Result[0][0], Result[1][i],label='Fiber %s'%FiberNumbers[i])
            plt.legend() 
               
        else:
            plt.plot(Result[0][0], Result[1][0])            
        ax = fig.add_subplot(111)
        fig.subplots_adjust(top=0.85)
       
        ax.set_xlabel('Length')
        ax.set_ylabel('Strain')

        
        plt.show()
        
    def SurfacePlotter(self,Result=[[0.0,1.1,2.2],[1000.3,1500.0,2000.1]],FiberNumbers=[],FiberPositions=[]):
        '''
        Plots one series.
        '''
        plt.style.use('seaborn-white')
        y=sort(FiberPositions) # Fiber position
        z = [x for _,x in sorted(zip(FiberPositions,Result[1]))]
        x=Result[0][0]# Length
        #z=Result[1] #Strain
        X,Y=np.meshgrid(x,y)
        Z=(np.array(z))

        plt.contourf(X, Y, Z)
        plt.colorbar() 
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        ax.plot_wireframe(X, Y, Z)
        plt.show()
        

         
    def ContourPlotter(self,Result=[[0.0,1.1,2.2],[1000.3,1500.0,2000.1]],FiberNumbers=[],FiberPositions=[]):
        plt.style.use('classic')
        y=sort(FiberPositions) # Fiber position
        z = [x for _,x in sorted(zip(FiberPositions,Result[1]))]
        x=Result[0][0]# Length
        #z=Result[1] #Strain
        X,Y=np.meshgrid(x,y)
        Z=(np.array(z))

        #plt.contour(X, Y, Z, colors='black')
        #fig = plt.figure()
        #ax = fig.add_subplot(111, projection='3d')
        #ax.plot_wireframe(X, Y, Z)
        plt.contourf(X, Y, Z, 1000)#, cmap='RdGy')
        plt.colorbar();        
        plt.show()
        
    def Smoother(self,Result=[],FiberNumbers=[1,2,3,4,5,6,89],Fibersforsmoothing=[1,3,4],algorithm='bithces'):
        ResultSmooth=[]
        for i in range(len(FiberNumbers)):
            for t in range(len(Fibersforsmoothing)):
                smoothed=Result[1][i]
                if FiberNumbers[i]==Fibersforsmoothing[t]:
                    y=Result[1][i]
                    if algorithm=='ysg':
                        ysg = savgol_filter(y, 21, 3)
                        smoothed=ysg
                    elif algorithm=='threshold':
                        Threshold=smooth.thresholding_algo(np.array(y), lag=3, threshold=40000000, influence=0.)
                        smoothed=Threshold["avgFilter"]                                                             
                    break
            ResultSmooth.append(smoothed)
            ysg=[]  
        
        return Result[0], ResultSmooth
    
    def SeriesReader(self,location='C:\location\of\your\series',key='Fibre_4000kN',startdistance=12.0,length=145.0):
        '''
        Takes one series of measurements, called by a key which must be uniqe to that series. 
        This means that if one series is named Fiber and another Fiber_4000kN, then it will crash upon key='Fiber'.
        
        Returns length of longest series vs strain normalized toward Reference.txt.
        '''
        f=open(join(location,'Reference.txt'))
        lines=f.readlines()
        FiberNumber=[]
        Length=[]
        Position=[]
        startappending=False
        for i in range(len(lines)):
            if lines[i].find("Fiber"):
                startappending=True    
            if startappending:
                FiberNumber.append(int(lines[i].split('\t')[0]))
                Length.append(float(lines[i].split('\t')[1]))
                Position.append(float(lines[i].split('\t')[2]))
        Reference=[FiberNumber,Length]
        f.close()
        
        wantedfiles=[]
        Reference=[FiberNumber,Length]
        Shortest=min(Length)
        wantedfiles = [f for f in listdir(location) if isfile(join(location, f)) and f.find(key)!=-1 and f.find('Reference')==-1]           
        sorted_files = sorted(wantedfiles)
        OldFiberNumber=0
        Strain=[]
        Length=[]
        StrainArrays=[]
        LengthArrays=[]
        Fibernumbers=[]
        Positionswithmeasurement=[]
        for f in sorted_files: #Checks for one series of measurements.
            Fibernumber=int(f.split('_')[-2]) #Takes out fibernumber
            Fibernumbers.append(Fibernumber) # Appends f
            Positionswithmeasurement.append(Position[Fibernumber-1])
            if Fibernumber<OldFiberNumber:
                OldFiberNumber=0
                break
            Resultonefiber=readers.Lower_Reader(self,location=join(location,f))
            for i in range(len(Reference[0])):
                if Fibernumber==Reference[0][i]:
                    Strain=[]
                    Length=[]
                    for l in range(len(Resultonefiber[0])):
                        if Resultonefiber[0][l]>Reference[1][i]:
                            Strain.append(Resultonefiber[1][l])
                            Length.append(Resultonefiber[0][l])
                    ##### End result loop one fibre ####
                    StrainArrays.append(Strain)
                    LengthArrays.append(Length)
        LengthsofLengths=[]
        for l in LengthArrays:
            LengthofLength=len(l)
            LengthsofLengths.append(LengthofLength)
        longest=max(LengthsofLengths)
        for i in range(len(LengthsofLengths)):
            if LengthsofLengths[i]==longest:
                num=i
        Len=LengthArrays[num]

        Length=Len-np.full((1,int(len(Len))), float(Len[0]))          

        strainequal=[]
        for s in StrainArrays:
            missing=longest-len(s)
            lastentry=s[-1]
            strain=s
            for i in range(missing):
                strain.append(lastentry)
            strainequal.append(strain)
        LengthAdjusted=[]
        StrainAdjusted=[]
        idel=[]
        for i in range(len(Length[0])):
            if startdistance+length>Length[0][i]>startdistance:
                LengthAdjusted.append(Length[0][i])
                
            else:
                idel.append(i)
            
        strainequal=np.delete(strainequal,idel,1)
       
        Length=[LengthAdjusted]
        
        print(len(LengthAdjusted))
        print(len(strainequal[0]))
        #print(StrainAdjusted)
        return [Length,strainequal],Fibernumbers,Positionswithmeasurement

    def Writer(self,Result=[],FiberNumbers=[],Filename='Jahman'):
        y=1
        filename="Output_"+Filename+".txt"
        thefile = open(filename, 'w')
        
        thefile.write("Length (mm) \t" %FiberNumbers) 
        for fiber in FiberNumbers:
            thefile.write("Fiber %s (microstrain)\t"%int(fiber))  
        thefile.write("\n")
        for i in range(len(Result[1][0])):
            Lengthtowrite=Result[0][0][i]
            thefile.write("%.4f"%Lengthtowrite)
            thefile.write("\t")
            for column in Result[1]:
                thefile.write("%.6f"%column[i])
                thefile.write("\t")
            thefile.write("\n")
            
class smooth:
    def thresholding_algo(y, lag, threshold, influence):
        signals = np.zeros(len(y))
        filteredY = np.array(y)
        avgFilter = [0]*len(y)
        stdFilter = [0]*len(y)
        avgFilter[lag - 1] = np.mean(y[0:lag])
        stdFilter[lag - 1] = np.std(y[0:lag])
        for i in range(lag, len(y)):
            if abs(y[i] - avgFilter[i-1]) > threshold * stdFilter [i-1]:
                if y[i] > avgFilter[i-1]:
                    signals[i] = 1
                else:
                    signals[i] = -1
    
                filteredY[i] = influence * y[i] + (1 - influence) * filteredY[i-1]
                avgFilter[i] = np.mean(filteredY[(i-lag):i])
                stdFilter[i] = np.std(filteredY[(i-lag):i])
            else:
                signals[i] = 0
                filteredY[i] = y[i]
                avgFilter[i] = np.mean(filteredY[(i-lag):i])
                stdFilter[i] = np.std(filteredY[(i-lag):i])
    
        return dict(signals = np.asarray(signals),
                    avgFilter = np.asarray(avgFilter),
                    stdFilter = np.asarray(stdFilter))

