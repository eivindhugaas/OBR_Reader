import numpy as np
import math
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from itertools import product, combinations
import csv
import sys
from ReaderFunctions.ReaderFunctions import readers as rdr

startdistance=100.0 #mm
length=100.0 #mm
rdr=rdr()
Result=rdr.SeriesReader(location=r'C:\Users\eivinhug\Documents\GitHub\OBR_Reader\TestFiles',key='Fibre_4000kN',startdistance=startdistance,length=length)

ResultSmooth=rdr.Smoother(Result=Result[0],FiberNumbers=Result[1],Fibersforsmoothing=[4],algorithm='threshold')
#rdr.Plotter(Result=Result[0],FiberNumbers=Result[1])
#rdr.Plotter(Result=ResultSmooth,FiberNumbers=Result[1])
rdr.ContourPlotter(Result=ResultSmooth,FiberNumbers=Result[1],FiberPositions=Result[2])
#rdr.SurfacePlotter(Result=Result[0],FiberNumbers=Result[1],FiberPositions=Result[2])
#rdr.SurfacePlotter(Result=ResultSmooth,FiberNumbers=Result[1],FiberPositions=Result[2])

#rdr.Writer(Result=Result[0],FiberNumbers=Result[1])

