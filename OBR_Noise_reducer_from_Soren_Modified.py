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


if __name__ == '__main__':
	
	'''
	------------------------------------------------------------------------------ Start Input F08 --------------------------------------------------------------------------------------------
	'''
	
	#base_location=r'C:\Users\eivinhug\OneDrive - NTNU\PhD\Testing\Laminate_F\OBR_Files\F08_Fatigue_25102018'

	#metafile='F08_MeasurementMetadata.txt'
	
	#measurementfile = 'F_08_fibre 1_'
	
	#plotvalue=1.8
	
	#constant_diff=1./1000. #mm
	
	#if measurementfile=='F_08_fibre 1_':
		#startlength=17.67
		#endlength=17.72
		#midlelength=17.695#6935
		
		#startlength=midlelength-(115/1000)
		#endlength=midlelength+(115/1000)
		
		#MaxDifferenceBetweenCycles=300 #200 #
		 
		#MaxDifferenceBetweenLoadSteps=400 #500
		
		#MaxDifference=1000 #1000 #		
		
	#if measurementfile=='F_08_fibre 2_':
		#startlength=18.10
		#endlength=18.36
		#midlelength=18.23-(2/1000)
		
		#startlength=midlelength-(115/1000)
		#endlength=midlelength+(115/1000)	
	
		#MaxDifferenceBetweenCycles=300 #200 #
		 
		#MaxDifferenceBetweenLoadSteps=300 #500
		
		#MaxDifference=1000 #1000 #			
	
	
	#if measurementfile=='F_08_fibre 3_':
		#startlength=17.53
		#endlength=17.80
	
		#midlelength=17.665
		
		#startlength=midlelength-(115/1000)
		#endlength=midlelength+(115/1000)		

		#MaxDifferenceBetweenCycles=300 #200 #
		 
		#MaxDifferenceBetweenLoadSteps=300 #500
		
		#MaxDifference=1000 #1000 #		
	
	
	#if measurementfile=='F_08_fibre 4_':
		#startlength=17.73
		#endlength=17.96

	'''
	-------------------------------------------------------------------------Start input F04 -------------------------------------------
	'''
	
	base_location=r'C:\Users\eivinhug\OneDrive - NTNU\PhD\Testing\Laminate_F\OBR_Files\F04_Fatigue_11112018' #.txt measurement files
	
	metafile='F04_MeasurementMetadata_7.txt' #metadatafile containing overview of measurements
	
	measurementfile = 'F04_fibre 1_' #which fiber
	
	plotvalue=20.8#2.763 #which value to plot in the 3D graphs
	
	constant_diff=1./1000. #mm #resolution of the measurements, can be set to whatever, but should follow what can be achieved with the current set of files.
	
	if measurementfile=='F04_fibre 1_':
		startlength=18.06
		endlength=18.55
		MaxDifferenceBetweenCycles=400 #200 #
		 
		MaxDifferenceBetweenLoadSteps=300 #500
		
		MaxDifference=1200 #1000		
		midlelength=((startlength+endlength)/2)
	
	if measurementfile=='F04_fibre 2_':
		startlength=18.10 
		endlength=18.28
	
	if measurementfile=='F04_fibre 3_':
		startlength=19.78
		endlength=19.97
	
	'''
	--------------------------------------------------------------- End input, the next section may be changed to accomodate several different measurement lengths and dictionaries ---------------------------------------------------------------
	'''	
	
	file_location5 = os.path.join(base_location,'RAW_L1')
	file_location6 = os.path.join(base_location,'RAW_L2')
	#file_location7 = os.path.join(base_location,'RAW_L3')
	
	metadatatuple=smth.metadatatuple(metafile=os.path.join(base_location,metafile))
	
	dumplocation=os.path.join(base_location,'dictdump')
	
	lengthlist=np.arange(startlength,endlength,constant_diff)	
	middleengthlist=np.arange(startlength-midlelength,endlength-midlelength,constant_diff)*1000	

	'''
	----------------------------------------------------------------- End pre-processes, intitate modules for establishing dictionaries ------------------------------------------------------------------------------------
	'''	
	
	allfilesdict5=deepcopy(smth.Measurement_Dictionary(File_Location=file_location5,File_Name_Base=measurementfile))
	
	allfilesdict6=deepcopy(smth.Measurement_Dictionary(File_Location=file_location6,File_Name_Base=measurementfile))
	
	#allfilesdict7=deepcopy(smth.Measurement_Dictionary(File_Location=file_location7,File_Name_Base=measurementfile))
	
	AllDictsInList=[allfilesdict5,allfilesdict6]#,allfilesdict7]
	
	allfilesdict=deepcopy(smth.CombineDictionaries(Dictinonary_List=AllDictsInList))
	
	newdict=deepcopy(smth.changemeasurementdict(measurementdict=allfilesdict,metadatalist=metadatatuple)) #Combines Metadata and MeasurementDictionary to create a dictionary with all information needed.
	
	allfilesdictconstantx=deepcopy(smth.rbfidict(Dict=newdict,lengthlist=lengthlist))
	
	summedfiles=deepcopy(smth.summedmeasurementdictionary(dictionary=allfilesdictconstantx,metadata=metadatatuple))
	
	
	'''
	---------------------------------------------------------------------------- Established dictionary of all files, start identifying noise ------------------------------------------------------------------------------------
	'''		

	
	MDiffDictonlyNoise=deepcopy(smth.noiseoveronemeasurement(data=allfilesdictconstantx,Max_Difference=MaxDifference))
	
	DispDiffDictonlyNoise=deepcopy(smth.noiseoverloadsteps(data=allfilesdictconstantx,Max_Difference_Between_Load_Steps=MaxDifferenceBetweenLoadSteps))
	
	NDiffDictonlyNoise=deepcopy(smth.noiseovercycles(data=allfilesdictconstantx,Max_Difference_Between_Cycles=MaxDifferenceBetweenCycles))
	
	
	'''----------- Dictioniaries established identifying where in the measurement dictionaries there are noise, intitated removig theese measurements from the measurement dicts ------------------------------------------------------------------------------------
	'''			

	removednoise=deepcopy(smth.removenoise(noisedict=MDiffDictonlyNoise,data=allfilesdictconstantx))
	
	removedmorenoise=deepcopy(smth.removenoise(noisedict=NDiffDictonlyNoise,data=removednoise))
	
	removedevenmorenoise=deepcopy(smth.removenoise(noisedict=DispDiffDictonlyNoise,data=removedmorenoise))
	
	'''
	------------------------------------ End removing noise from measurement dictionaries, intitiate interpolation between the remaining measurements -------------------------------------------------------------------------------------------------------
	'''	
	
	noisefree=deepcopy(smth.rbfidict(Dict=removedevenmorenoise,lengthlist=lengthlist,function='linear',smooth=0.0))
	
	summedfilesnoisefree=deepcopy(smth.summedmeasurementdictionary(dictionary=noisefree,metadata=metadatatuple))
	
	'''
	------------------------------ End noise reduction, new noise free dictionaries established, start preparing dictionaries for plotting at given plot value. ----------------------------------------------------------------------------------------
	------------------------------ Give what sort of interpolation/extrapolation function shall be used, relevant if the plot value is outside the ramping at some cycles. -------------------------------------------------------------------------------------------------------
	------------------------------ See rbf interpolation documentation on internet to see what functions are available, 'thin_plate' or 'linear' are usually the best.  -------------------------------------------------------------------------------------------------------
	
	'''
	function='linear'
	
	addedcycleswithnoise=deepcopy(smth.interpolatetovalue(dictionary=allfilesdictconstantx,values=[plotvalue],function=function,onlyreturnthevalues=True))
	
	addedcycleswithnoisesummed=deepcopy(smth.interpolatetovalue(dictionary=summedfiles,values=[plotvalue],function=function,onlyreturnthevalues=True))
	
	addedcyclesnoisefree=deepcopy(smth.interpolatetovalue(dictionary=noisefree,values=[plotvalue],function=function,onlyreturnthevalues=True))
	
	addedcyclesnoisefreesummed=deepcopy(smth.interpolatetovalue(dictionary=summedfilesnoisefree,values=[plotvalue],function=function,onlyreturnthevalues=False))
	
	'''
	------------------------------ End interpolation, start calculating the area underneath the strainfields ----------------------------------------------------------------------------------------
	------------------------------ The area serves two purposes, one is to get the displacement and another is to check that there are no 'funny' measurements ----------------------------------------------------------------------------------------
	------------------------------ resulting from faulty noise reduction or poor file administration. After this it plots the areas to get a nice overview. ----------------------------------------------------------------------------------------

	'''	
	
	areaundergraph=smth.areaundergraph(data=addedcyclesnoisefreesummed)
	
	smth.plotsecondleveldict(data=areaundergraph, plottype='3D')
	
	'''
	------------------------------ End integration of strain fieldm start dumping of whatever dict you want to dumplocation as a numpy file.  ----------------------------------------------------------------------------------------
	'''		
	dumpdict=summedfilesnoisefree
	
	if not os.path.exists(dumplocation):
		os.makedirs(dumplocation)	
	
	np.save(os.path.join(dumplocation,measurementfile+'dict'),dumpdict)		
	print('Dumped Dict')
	
	'''
	--------------------------------- End dumping, start plotting of results, this section is rather dynamic and changed according to need.  ----------------------------------------------------------------------------------------
	'''		

	cycles=list(addedcycleswithnoise.keys())
	fig = plt.figure(figsize=plt.figaspect(0.5))
	
	plotdict1=smth.preparedictforplotting(lengthlist=lengthlist,plotvalue=plotvalue,newdict=addedcycleswithnoise)

	X1,Y1=np.meshgrid(cycles,middleengthlist)
	Z1=np.array(plotdict1)
	ax = fig.add_subplot(2, 2, 1, projection='3d')

	ax.plot_wireframe(X1, Y1, Z1, rstride=1, cstride=1)#,cmap=cm.coolwarm,linewidth=0, antialiased=False)		

	plotdict2=smth.preparedictforplotting(lengthlist=lengthlist,plotvalue=plotvalue,newdict=addedcyclesnoisefree)#allfilesdictconstantx)

	X1,Y1=np.meshgrid(cycles,middleengthlist)
	Z1=np.array(plotdict2)
	ax = fig.add_subplot(2, 2, 2, projection='3d')

	ax.plot_surface(X1, Y1, Z1)#,cmap=cm.coolwarm,linewidth=0, antialiased=False)	
	
	
	plotdict3=smth.preparedictforplotting(lengthlist=lengthlist,plotvalue=plotvalue,newdict=addedcycleswithnoisesummed)#allfilesdictconstantx)

	X1,Y1=np.meshgrid(cycles,middleengthlist)
	Z1=np.array(plotdict3)
	ax = fig.add_subplot(2, 2, 3, projection='3d')
	ax.plot_wireframe(X1, Y1, Z1, rstride=1, cstride=1)
	#ax.plot_surface(X1, Y1, Z1,cmap=cm.coolwarm,
        #               linewidth=0, antialiased=False)#,cmap=cm.coolwarm,linewidth=0, antialiased=False)		

	plotdict4=smth.preparedictforplotting(lengthlist=lengthlist,plotvalue=plotvalue,newdict=addedcyclesnoisefreesummed)#allfilesdictconstantx)

	X1,Y1=np.meshgrid(cycles,middleengthlist)
	Z1=np.array(plotdict4)
	ax = fig.add_subplot(2, 2, 4, projection='3d')

	#ax.plot_surface(X1, Y1, Z1)#,cmap=cm.coolwarm,linewidth=0, antialiased=False)		
	ax.plot_wireframe(X1, Y1, Z1, rstride=1, cstride=1)
	
	plt.show()

	fig = plt.figure(figsize=plt.figaspect(0.5))
	fig.suptitle('Strain along fiber adjacent to hole at %s mm displacement (max displacement was 3.6 mm)'%(str(plotvalue)), fontsize=16) 
	plotdict3=smth.preparedictforplotting(lengthlist=lengthlist,plotvalue=plotvalue,newdict=addedcyclesnoisefreesummed)#allfilesdictconstantx)

	X1,Y1=np.meshgrid(cycles,middleengthlist)
	Z1=np.array(plotdict3)
	ax = fig.add_subplot(1, 1, 1, projection='3d')
	ax.set_zlim(0, 25000)
	#ax.set_xlim(0, 2000)
	ax.plot_wireframe(X1, Y1, Z1, rstride=2, cstride=2)
	
	#ax.plot_surface(X1, Y1, Z1,cmap=cm.coolwarm,
        #               linewidth=0, antialiased=False)#,cmap=cm.coolwarm,linewidth=0, antialiased=False)			

	plt.show()
	
	fig = plt.figure(figsize=plt.figaspect(0.5))
	fig.suptitle('Strain along fiber adjacent to hole at %s mm displacement (max displacement was 3.6 mm)'%(str(plotvalue)), fontsize=16) 

	plotdict3=smth.preparedictforplotting(lengthlist=lengthlist,plotvalue=plotvalue,newdict=addedcyclesnoisefreesummed)#allfilesdictconstantx)

	X1,Y1=np.meshgrid(cycles,middleengthlist)
	Z1=np.array(plotdict3)
	ax = fig.add_subplot(1, 1, 1, projection='3d')
	ax.set_zlim(0, 12000)
	#ax.plot_wireframe(X1, Y1, Z1, rstride=1, cstride=1)
	ax.set_xlabel('Cycles')#, fontsize=20)
	ax.set_ylabel('Length along fiber, with 0 mm being hole center (mm)')	
	ax.set_zlabel('Microstrain')	
	surf = ax.plot_surface(X1, Y1, Z1,cmap=cm.coolwarm,
                       linewidth=0, antialiased=False)#,cmap=cm.coolwarm,linewidth=0, antialiased=False)	
	
	fig.colorbar(surf, shrink=0.5, aspect=5)

	plt.show()	
	
	
	'''
	------------------------------------------------------------------------------------------------- Ended plotting -------------------------------------------------------------------------------------------------------
	'''
	np.save(os.path.join("\dictdump",measurementfile), summedfilesnoisefree) 
	


