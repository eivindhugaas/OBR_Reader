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

from scipy.interpolate import Rbf
from copy import deepcopy
import matplotlib.pyplot as plt
import os
import collections
# shutil is here for using the correct operative specific move commands.
import shutil
from math import log
import numpy as np
from collections import defaultdict
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.axes3d import Axes3D, get_test_data
from matplotlib import cm
import numpy as np
from os import listdir
from os.path import isfile, join


from Smoothening_Functions.SmootheningFunctions import smoothening as smth
smth=smth()

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


if __name__ == '__main__':
	
	base_location=r'C:\Users\eivinhug\OneDrive - NTNU\PhD\Testing\Laminate_F\OBR_Files\F08_Fatigue_25102018'

	metadatadict=smth.metadatadict(metafile=os.path.join(base_location,'F08_MeasurementMetadata.txt'))
	referencemeta=smth.referencemetadatalist(metafile=os.path.join(base_location,'F08_ReferenceMetadata.txt'))
	print(referencemeta)
	dumplocation=os.path.join(base_location,'dictdump_2')
	plotdisp=1.8
	
	measurements,cycles=smth.numberandcyclesfromdisplist(disp=plotdisp,metadatadict=metadatadict)
	
	RefPos, Fibernumbers, Reflength, =zip(*referencemeta)
	
	onlyfiles = [f for f in listdir(dumplocation) if isfile(join(dumplocation, f))]
	onefiledict=defaultdict(dict)
	reflengthdict=defaultdict(dict)
	maxdict=defaultdict(dict)
	dictlist=[]
	possiblenames=['fibre','Fiber','Fibre','Fiber']
	for file in onlyfiles:
		onefiledict=deepcopy(np.load(os.path.join(dumplocation,file)).item())
		filenamelist=file.split('_')
		for i in range(len(filenamelist)):
			filename=filenamelist[i]
			
			if any(name in filename for name in possiblenames):
			
				try:
					print('b',filename.split(' '))
					Fibernumber=int(filename.split(' ')[-1])
				except:
					print('c',filename)
					Fibernumber=int(filenamelist[i+1])
		for measurement, straindata in onefiledict.items():
			if measurement in measurements:
				length,strain=zip(*list(straindata.items()))
				maxstrain=max(strain)
				for length,strain in straindata.items():
					if strain==maxstrain:
						print(length)

				maxdict[measurement][Fibernumber]=maxstrain
				
				for ref in referencemeta:
					if Fibernumber==ref[1]:
						refl=ref[2]
						reflength=smth.find_nearest(datadict=straindata, X_Value_To_Be_Found=refl)
				reflengthdict[measurement][Fibernumber]=straindata[reflength]
				
	print(reflengthdict)
	print("maxdict",maxdict)
	fig = plt.figure(figsize=plt.figaspect(0.5))
	
	#self,lengthlist=[],measurements=[],dictionary={},plotvalue=1.8,newdict={}
	
	plotdict3=smth.preparedictforplotting(lengthlist=Fibernumbers,measurements=measurements,dictionary=maxdict)

	X1,Y1=np.meshgrid(cycles,RefPos)
	Z1=np.array(plotdict3)
	ax = fig.add_subplot(2, 1, 1, projection='3d')
	#ax.set_zlim(0, 12000)
	#ax.plot_wireframe(X1, Y1, Z1, rstride=1, cstride=1)

	ax.plot_surface(X1, Y1, Z1,cmap=cm.coolwarm,
                        linewidth=0, antialiased=False)#,cmap=cm.coolwarm,linewidth=0, antialiased=False)
	
	plotdict4=smth.preparedictforplotting(lengthlist=Fibernumbers,measurements=measurements,dictionary=reflengthdict)

	X1,Y1=np.meshgrid(cycles,RefPos)
	Z1=np.array(plotdict4)
	ax = fig.add_subplot(2, 1, 2, projection='3d')
	#ax.set_zlim(0, 12000)
	#ax.plot_wireframe(X1, Y1, Z1, rstride=1, cstride=1)

	ax.plot_surface(X1, Y1, Z1,cmap=cm.coolwarm,
                        linewidth=0, antialiased=False)
	plt.show()		
	fig = plt.figure(figsize=plt.figaspect(0.5))
	fig.suptitle('Strain concentration evolvment at %s mm displacement (max displacement was 3.6 mm)'%(str(plotdisp)), fontsize=16) 
	plotdict4=smth.preparedictforplotting(lengthlist=Fibernumbers,measurements=measurements,dictionary=reflengthdict)

	X1,Y1=np.meshgrid(cycles,RefPos)
	Z1=np.array(plotdict4)
	ax = fig.add_subplot(1, 1, 1, projection='3d')
	ax.set_xlabel('Cycles')#, fontsize=20)
	ax.set_ylabel('Length from middle of sample (stops at 25 mm, but extrapolated to show probable strain curve from mid sample measurement.)')	
	ax.set_zlabel('Microstrain')
	#ax.set_zlim(0, 12000)
	#ax.plot_wireframe(X1, Y1, Z1, rstride=1, cstride=1)

	ax.plot_surface(X1, Y1, Z1,cmap=cm.coolwarm,
                        linewidth=0, antialiased=False)
	
	
	plt.show()			
	
		
	
		
	

	