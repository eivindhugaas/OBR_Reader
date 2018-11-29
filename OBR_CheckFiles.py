import os

list_of_files=os.listdir(r'C:\Users\eivinhug\Documents\OBR_Data\E07_Fatigue_14092018\Fixed')

fibres=['fibre 1','fibre 2','fibre 3']
maxnumber=328

list_of_files=os.listdir(r'C:\Users\eivinhug\Documents\OBR_Data\E07_Fatigue_14092018\Fixed')
nextprefix=1.
simplifiedlist=[]
properlist=[]

for entry in list_of_files:
    prefix=entry.split('_')[-1].split('.')[0]
    fibre=entry.split('_')[1]
    simplifiedlist.append(fibre+'_'+prefix)
        

for fibre in fibres:
    for i in range(2,maxnumber+1):
        prefix=str(i).zfill(4)
        properlist.append(fibre+'_'+prefix)


diff=sorted(set(properlist).difference(set(simplifiedlist)))
print(diff)

    
    

        
    
