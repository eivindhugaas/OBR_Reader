import matplotlib.pyplot as plt
from ReaderFunctions.ReaderFunctions import readers as rdr
import os
rdr=rdr()

#If you want to load strain and length from some file, then this works, but its in the format of the originators file system, so it may need some tweaking to cater your needs.
#path=r'C:\Users\eivinhug\OneDrive - NTNU\PhD_Backup\NTNU\PhD\Testing\Laminate_E\OBR_Files\E01_FatigueTest_2_28082018'
#filename='Output_E01_fibre 1_45_53.txt'
#res=rdr.Output_Reader_pick_Measurement(location=os.path.join(path,filename),Measurement=53)
#Strain=res[1]
#Length=res[0]

#Hard coded strain:
Strain=[29.68388, 16.915997, 25.484955, 17.04044, 21.270474, 25.44866, 8.553405, 16.953329, 17.046661, 25.454882, 21.311956, 21.271513, -4.311961, 4.18337, -4.307813, 12.705664, -8.526442, 4.282925, 0.060148, -4.309887, -4.26011, -8.472517, -4.220703, 4.276702, 4.191666, 12.72433, 12.676627, 16.992737, 4.301591, 118.965752, 152.98233, -203.921127, -356.81842, -165.6465, 3368.32324, -157.136658, 2459.39722, 1767.08276, 1121.45007, 700.937378, 1061.90601, 1121.44177, 1202.11938, 1473.95032, 1592.86523, 1295.47058, 1575.92859, 917.50708, 1066.16711, 1363.46643, 1465.47571, 1193.55042, 1393.25085, 1291.28406, 1095.823, 1694.77075, 1401.70972, 1142.63245, 1253.10803, 1197.78662, 891.994202, 917.49884, 1189.31836, 1660.87964, 2688.72339, 2170.58203, 913.294739, 1032.16919, 1240.38269, 1291.36084, 1117.16296, 1304.10596, 1151.16711, 590.513672, -33.958511, -361.097198, 288.841248, 352.615326, -7259.30566, 195.382248, 12.749218, 21.243511, 25.499474, 4.258036, 16.926367, 12.7907, 8.44348, 8.536812, 8.441405, 8.532664, 4.233147, -4.212407, 12.716033, -0.014518, 0.008296, 8.52022, 16.982367, 8.551331, 8.472517, 12.757515, 16.920143, 4.272554, 12.691145, 0.026963, 12.747145, -0.062222, 8.513997, 16.945034, 8.536812, 8.44348, 12.763737, 8.551331, 12.689071, 8.482886, 21.246622, 726.304138, 1155.38269, 1321.09973, 1227.54736, 930.233521, 840.993164, 1180.80225, 1473.98462, 1308.28296, 858.069885, 586.143616, -2272.50928, 2038.92505, 2811.93481, -1788.20081, 747.616089, 696.609863, 662.569458, 734.827454, 798.552795, 896.181763, 917.473938, 972.647949, 870.73822, 1095.90808, 1635.4093, 1316.75659, 1027.98376, 2140.78711, 3461.87573, 3784.70386, -4906.02246, 2098.38623, 1032.19104, -1516.42078, 3521.33325, 450.235962, 161.37291, 276.123138, -1270.05396, -3151.75757, 2569.8396, 1614.09839, 926.020081, 683.858582, 981.197205, 917.562134, 1282.75354, 1354.96484, 1469.72131, -947.254272, 1049.22424, -6787.77979, -327.022552, 1015.16608, -3538.36157, -1677.78845, 581.907349, 67.926354, 662.595398, 12.703589, -649.905273, -76.445534, -2174.71558, 2582.51514, -5649.36377, -4056.49365, 11094.834, -959.922607, 713.556946, 1057.677, -3457.63086, -12738.7842, -998.226257, 4468.53955, -7480.17188, -5657.96484, 55.166763, 764.563232, 2603.80444, 505.448334, 794.270935, 348.307526, -6864.23096]

#Hard coded length:
Length=[16.380491, 16.384474, 16.388456, 16.392439, 16.396423, 16.400406, 16.404388, 16.408373, 16.412355, 16.416338, 16.42032, 16.424305, 16.428287, 16.43227, 16.436253, 16.440237, 16.44422, 16.448202, 16.452187, 16.456169, 16.460152, 16.464134, 16.468119, 16.472101, 16.476084, 16.480068, 16.484051, 16.488033, 16.492016, 16.496, 16.499983, 16.503965, 16.507948, 16.511932, 16.515915, 16.519897, 16.523882, 16.527864, 16.531847, 16.535829, 16.539814, 16.543796, 16.547779, 16.551762, 16.555746, 16.559729, 16.563711, 16.567696, 16.571678, 16.575661, 16.579643, 16.583628, 16.58761, 16.591593, 16.595577, 16.59956, 16.603542, 16.607525, 16.611509, 16.615492, 16.619474, 16.623457, 16.627441, 16.631424, 16.635406, 16.639391, 16.643373, 16.647356, 16.651339, 16.655323, 16.659306, 16.663288, 16.667271, 16.671255, 16.675238, 16.67922, 16.683205, 16.687187, 16.69117, 16.695152, 16.699137, 16.703119, 16.707102, 16.711086, 16.715069, 16.719051, 16.723034, 16.727018, 16.731001, 16.734983, 16.738966, 16.74295, 16.746933, 16.750916, 16.7549, 16.758882, 16.762865, 16.766848, 16.770832, 16.774815, 16.778797, 16.782782, 16.786764, 16.790747, 16.794729, 16.798714, 16.802696, 16.806679, 16.810661, 16.814646, 16.818628, 16.822611, 16.826595, 16.830578, 16.83456, 16.838543, 16.842527, 16.84651, 16.850493, 16.854475, 16.858459, 16.862442, 16.866425, 16.870409, 16.874392, 16.878374, 16.882357, 16.886341, 16.890324, 16.894306, 16.898291, 16.902273, 16.906256, 16.910238, 16.914223, 16.918205, 16.922188, 16.92617, 16.930155, 16.934137, 16.93812, 16.942104, 16.946087, 16.950069, 16.954052, 16.958036, 16.962019, 16.966002, 16.969986, 16.973969, 16.977951, 16.981934, 16.985918, 16.989901, 16.993883, 16.997866, 17.00185, 17.005833, 17.009815, 17.0138, 17.017782, 17.021765, 17.025747, 17.029732, 17.033714, 17.037697, 17.041679, 17.045664, 17.049646, 17.053629, 17.057613, 17.061596, 17.065579, 17.069561, 17.073546, 17.077528, 17.081511, 17.085495, 17.089478, 17.09346, 17.097443, 17.101427, 17.10541, 17.109392, 17.113375, 17.117359, 17.121342, 17.125324, 17.129309, 17.133291, 17.137274, 17.141256, 17.145241, 17.149223, 17.153206, 17.15719, 17.161173, 17.165155, 17.169138]

Diff=[]
      
for i in range(len(Strain)): #finds the strain difference between measurements, the first difference is between the first and the first. The second is first to second amd so on.
   m=Strain[i]
   if i==0:
      lastm=Strain[0]   
   else:
      lastm=Strain[i-1]   
   Diffi=m-lastm
   Diff.append(Diffi)   
LDiff=[]

for i in range(len(Length)): #finds the length difference between measurements, the first difference is between the first and the first. The second is first to second amd so on.
   m=Length[i]
   if i==0:
      lastm=Length[0]   
   else:
      lastm=Length[i-1]   
   Diffi=m-lastm
   LDiff.append(Diffi)
   
Ln=sum(LDiff)/len(LDiff)

smoothn=[]

for i in range(len(Diff)): #sorts what measurements shuld be average assumed (0.0) and kept as is (1.0).
   if i==0 or i==len(Diff)-1:
      n=1.
   elif abs(Diff[i])>187.5*Ln*1000:
      n=0.
   elif abs(Strain[i])<50.:
      n=1.
   else:
      n=1.
   smoothn.append(n)

smoothslist=[]

for i in range(len(smoothn)): #adds another 1.0 in ranges longer than two 0.0's
   currentsmoothn=smoothn[i]
   lastsmoothn=1.0
   nextsmoothn=1.0  
   if i>0 and i<len(smoothn)-1:
      currentsmoothn=smoothn[i]
      lastsmoothn=smoothn[i-1]
      nextsmoothn=smoothn[i+1]
   if currentsmoothn==0.0 and lastsmoothn==0.0:
      if nextsmoothn==1.0:
         smooths=1.0
   else:
      smooths=currentsmoothn
   smoothslist.append(smooths)
   
n=0
avgloc=[]
avg=[]
for i in range(len(smoothslist)): #finds at what location in strain array the strain should be averaged, finds also the values which should be taken as the average.
   if smoothslist[i]==0.0 and i!=0 and i!=len(smoothslist)-1:
      n=n+1
      if n==1:
         firstavg=Strain[i-1]
         avg.append(firstavg)
         avgloc.append(i)
      if smoothslist[i+1]==1.0:
         secondavg=Strain[i+1]
         n=0
         avg.append(secondavg)
         avgloc.append(i)

t=0
a=0
SmoothStrains=[]

for i in range(len(Strain)):
   Smoothstrain=Strain[i]
   if i>=avgloc[t] and i<=avgloc[t+1]:
      a=a+1
      Smoothstraininc=((avg[t+1]-avg[t])/(avgloc[t+1]-avgloc[t]+2))
      Smoothstrain=(avg[t]+(Smoothstraininc*a))
   if i>=avgloc[t+1] and t<(len(avgloc)-2):
      t=t+2
      a=0
   
   SmoothStrains.append(Smoothstrain)

#SuperDuperSmoothStrains=[]
#a=0
#t=0
#for i in range(len(Strain)):
   #Smoothstrain=Strain[i]
   #if i>=avgloc[t] and i<=avgloc[t+1]:
      #a=a+1
      #Start=Diff[avgloc[t]]
      #Stop=Diff[avgloc[t+1]]
      #Diffinc=((Stop-Start)/(avgloc[t+1]-avgloc[t]+2))
      #Diffsmoothstraininc=Start+(Diffinc*a)
      #Smoothstrain=(avg[t]+(Diffsmoothstraininc*a))
      
   #if i>=avgloc[t+1] and t<(len(avgloc)-2):
      #t=t+2
      #a=0
      
   #SuperDuperSmoothStrains.append(Smoothstrain)

SuperSmoothStrains=[]
Supersmoothn=[]
for i in range(len(smoothn)):   
   if abs(SmoothStrains[i]-Strain[i])<800.:  
      SuperSmoothStrains.append(Strain[i])
      Supersmoothn.append(1.0)
   else:
      SuperSmoothStrains.append(SmoothStrains[i])
      Supersmoothn.append(smoothn[i])

plt.plot(SuperSmoothStrains)

smoothslist=[]
smoothn=Supersmoothn
for i in range(len(smoothn)): #adds another 1.0 in ranges longer than two 0.0's
   currentsmoothn=smoothn[i]
   lastsmoothn=1.0
   nextsmoothn=1.0  
   if i>0 and i<len(smoothn)-1:
      currentsmoothn=smoothn[i]
      lastsmoothn=smoothn[i-1]
      nextsmoothn=smoothn[i+1]
   if currentsmoothn==0.0 and lastsmoothn==0.0:
      if nextsmoothn==1.0:
         smooths=1.0
   else:
      smooths=currentsmoothn
   smoothslist.append(smooths)
smoothslist=Supersmoothn

n=0
avgloc=[]
avg=[]

for i in range(len(smoothslist)):
   if smoothslist[i]==0.0 and i!=0 and i!=len(smoothslist)-1:
      n=n+1
      if n==1:
         firstavg=Strain[i-1]
         avg.append(firstavg)
         avgloc.append(i)
      if smoothslist[i+1]==1.0:
         secondavg=Strain[i+1]
         n=0
         avg.append(secondavg)
         avgloc.append(i)

t=0
a=0
SmoothStrains=[]

for i in range(len(Strain)):
   Smoothstrain=Strain[i]
   if i>=avgloc[t] and i<=avgloc[t+1]:
      a=a+1
      Smoothstraininc=((avg[t+1]-avg[t])/(avgloc[t+1]-avgloc[t]+2))
      Smoothstrain=(avg[t]+(Smoothstraininc*a))
   if i>=avgloc[t+1] and t<(len(avgloc)-2):
      t=t+2
      a=0
   
   SmoothStrains.append(Smoothstrain)

#SuperDuperSmoothStrains=[]
#a=0
#t=0
#for i in range(len(Strain)):
   #Smoothstrain=Strain[i]
   #if i>=avgloc[t] and i<=avgloc[t+1]:
      #a=a+1
      #Start=Diff[avgloc[t]]
      #Stop=Diff[avgloc[t+1]]
      #Diffinc=((Stop-Start)/(avgloc[t+1]-avgloc[t]+2))
      #Diffsmoothstraininc=Start+(Diffinc*a)
      #Smoothstrain=(avg[t]+(Diffsmoothstraininc*a))
      
   #if i>=avgloc[t+1] and t<(len(avgloc)-2):
      #t=t+2
      #a=0
      
   #SuperDuperSmoothStrains.append(Smoothstrain)

plt.plot(SmoothStrains)
plt.show()
#Absdiff=[]
#for i in range(len(Diff)):
   #Absdiff.append(abs(Diff[i]))
   
