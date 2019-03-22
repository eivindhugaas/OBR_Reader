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
from os import listdir
from os.path import isfile, join
from Smoothening_Functions.SmootheningFunctions import smoothening as smth
smth=smth()
import pandas as pd

writedist=r'C:\Users\eivinhug\OneDrive - NTNU\PhD\AbaqusModels\SplitDisk\SplitDisk_UMAT_1_5_mmDisp_0_05_Fric\txt'

onlyfiles = [f for f in listdir(writedist) if isfile(join(writedist, f))]
strains=[]
for file in onlyfiles:
	with open(join(writedist, file), 'r') as f:
		do=False
		length=[]
		strain=[]
		for line in f:
			try:
				float(line[0])
				do=True
			except:
				pass
			if do:
				length.append(float(line.split('\t')[0]))
				strain.append(float((line.split('\t')[1]).split('\n')[0]))
		print(length)
		print(strain)
		strains.append(strain)		
	plt.plot(length,strain,label=file)
	plt.legend()
plt.show()

straint=np.transpose(strains)

Write_file=os.path.join(writedist,'Allfilesinonefile.txt')

if not os.path.exists(os.path.dirname(Write_file)):
	os.makedirs(os.path.dirname(Write_file))

with open(Write_file, 'w') as f:
	namewithtab='Length (m)'
	
	for name in onlyfiles:
		namewithtab=namewithtab+'\t'+name
	f.writelines(namewithtab+'\n')
	for fd in range(len(length)):
		Length=length[fd] 
		Strain=list(straint[fd])
		Line=str(Length)
		for s in Strain:
			Line=Line+'\t'+str(s)
		
		f.writelines(Line+'\n')
f.close()