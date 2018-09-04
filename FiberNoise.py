import matplotlib.pyplot as plt
from ReaderFunctions.ReaderFunctions import readers as rdr
import os
rdr=rdr()

path=r'C:\Users\eivinhug\OneDrive - NTNU\PhD_Backup\NTNU\PhD\Testing\Laminate_E\OBR_Files\E01_FatigueTest_2_28082018'
filename='Output_E01_fibre 1_45_53.txt'
res=rdr.Output_Reader_pick_Measurement(location=os.path.join(path,filename),Measurement=53)

Strain=res[1]
Length=res[0]
threshold=500.


Diff=[]
      
for i in range(len(Strain)): #finds the difference between measurements, the first difference is between the first and the first. The second is first to second amd so on.
   m=Strain[i]
   if i==0:
      lastm=Strain[0]   
   else:
      lastm=Strain[i-1]   
   Diffi=m-lastm
   Diff.append(Diffi)   
LDiff=[]

for i in range(len(Length)): #finds the difference between measurements, the first difference is between the first and the first. The second is first to second amd so on.
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

SuperDuperSmoothStrains=[]
a=0
t=0
for i in range(len(Strain)):
   Smoothstrain=Strain[i]
   if i>=avgloc[t] and i<=avgloc[t+1]:
      a=a+1
      Start=Diff[avgloc[t]]
      Stop=Diff[avgloc[t+1]]
      Diffinc=((Stop-Start)/(avgloc[t+1]-avgloc[t]+2))
      Diffsmoothstraininc=Start+(Diffinc*a)
      Smoothstrain=(avg[t]+(Diffsmoothstraininc*a))
      
   if i>=avgloc[t+1] and t<(len(avgloc)-2):
      t=t+2
      a=0
      
   SuperDuperSmoothStrains.append(Smoothstrain)

SuperSmoothStrains=[]

for i in range(len(SmoothStrains)):
   if abs(SmoothStrains[i]-Strain[i])<800.:
      SuperSmoothStrains.append(Strain[i])
   else:
      SuperSmoothStrains.append(SmoothStrains[i])


plt.plot(SuperDuperSmoothStrains)
plt.plot(SuperSmoothStrains)
plt.plot(Strain)
plt.show()
#Absdiff=[]
#for i in range(len(Diff)):
   #Absdiff.append(abs(Diff[i]))
   
   