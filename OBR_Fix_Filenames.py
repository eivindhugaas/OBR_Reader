import os

location=r'C:\Users\eivinhug\Documents\OBR_Data\E07_Fatigue_14092018\Fixed'

list_of_files=os.listdir(r'C:\Users\eivinhug\Documents\OBR_Data\E07_Fatigue_14092018\Fixed')

fibres=['fibre 1','fibre 2','fibre 3']
maxnumber=329

list_of_files=os.listdir(r'C:\Users\eivinhug\Documents\OBR_Data\E07_Fatigue_14092018\Fixed')
nextprefix=1.
simplifiedlist=[]
properlist=[]

dont=True
for fibre in fibres:
    n=1
    print(fibre)
    for filename in sorted(list_of_files):
        fibrelist=[]

        #dontrunthislooptwiceforfsake
        
        #print(filename.split('_')[0]+'_'+filename.split('_')[1]+'_'+numberstring+'.obr')
        
        if filename.split('_')[1]==fibre:
            n=n+1
            numberstring=str(n).zfill(4)            
            print(filename,'E07_'+fibre+'_'+numberstring+'.obr')
            os.rename(os.path.join(location,filename),os.path.join(location,'E07_'+fibre+'_'+numberstring+'.obr'))
    

    
    
