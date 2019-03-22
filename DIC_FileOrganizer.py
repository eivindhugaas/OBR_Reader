from copy import deepcopy
import matplotlib.pyplot as plt
import os
# shutil is here for using the correct operative specific move commands.
import shutil
from math import log
import numpy as np

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.axes3d import Axes3D, get_test_data
from matplotlib import cm
import numpy as np

from Smoothening_Functions.SmootheningFunctions import smoothening as smth
smth=smth()

Linenames=['L0','L3','L2','L4','L5','L6','L1','L8','L7']
Lineindexes=[10,22,34,46,58,70,82,94,106]
Lengthindexes=[1,14,26,38,50,62,74,86,98]
Strain=['e1 [1] - Lagrange','e1 [1] - Lagrange','e1 [1] - Lagrange','e1 [1] - Lagrange','e1 [1] - Lagrange','e1 [1] - Lagrange','e1 [1] - Lagrange','e1 [1] - Lagrange','e1 [1] - Lagrange']

Location=r'C:\Users\eivinhug\OneDrive - NTNU\PhD\Testing\Laminate_F\DIC\F13_Fatigue'
metafile='F13_MeasurementMetadata.txt'
datafile='LineSlice_F13_2.txt'
Metalines=[]

with open(Location+'\\'+metafile) as metadata:
	metalines=metadata.readlines()
	metalines=[x.strip() for x in metalines] 
	for line in metalines:
		splitline=line.split('\t')
		Number=splitline[0]
		Force=splitline[1]
		Cycle=splitline[2]
		Dataline=[Number,Cycle,Force]
		print(Dataline)
		Metalines.append(Dataline)
dataint=0
Datalines=[]
#Datadict=defaultdict(dict)
Datalineindex=[]
Numbers=[]
lineint=0
with open(Location+'\\'+datafile) as data:
	lines=data.readlines()
	for line in lines:
		splitline=line.split('\t')
		Datalines.append(splitline)
		
print('Done loading data')

WriteData=[]
for b in range(len(Lineindexes)):
	Lineindex=Lineindexes[b]				
	Linename=Linenames[b]
	Lengthindex=Lengthindexes[b]
	Start=False
	for i in range(len(Datalines)):
		data=Datalines[i]
		if 'Index [1]' in data[0]:
			
			Start=True
			firstline=True
			Number=int((((Datalines[i-2][0]).split('-'))[-1].split('_'))[0])
			
			WriteData.append([Linename,Number,Lineindex,Lengthindex,i+1,i+201])

print(WriteData)		
		
for entry in WriteData:
	Linename=entry[0]
	Number=entry[1]
	Lineindex=entry[2]
	Lengthindex=entry[3]
	start=entry[4]
	stop=entry[5]
	Write_file=Location+'\\RAW\\F_13_Line_'+str(Linename)+'_'+str(Number).zfill(5)+'.txt'
	if not os.path.exists(os.path.dirname(Write_file)):
		os.makedirs(os.path.dirname(Write_file))
	with open(Write_file,"w+") as datafile:
		datafile.write('Length (m)\tStrain (microstrain)\n')
		for i in range(start,stop):	
			if Datalines[i][Lengthindex]!='':
				try:
					firstentry=str(round((float(Datalines[i][Lengthindex])),4))
				except:
					firstentry=Datalines[i][Lengthindex]
					sys.exit()
				
				try:
					secentry=str(round((float(Datalines[i][Lineindex])*1000000),4))
				except:
					#secentry=Datalines[i][Lineindex]
					secentry=str(0.0)
					
				if i==stop-1:
					datafile.write(firstentry+'\t'+secentry)
				else:
					datafile.write(firstentry+'\t'+secentry+'\n')