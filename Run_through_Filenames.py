
from os import listdir, rename
from os.path import isfile, join
import shutil

mypath=r'F:\F04_Sorted_V2'

onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

prefix="F04_fibre 1"

newnumber=str((-1+1)).zfill(4)
for file in onlyfiles:
	if prefix in file:
	
		numberwithext=file.split("_")[-1]
		fibre=file.split("_")[-2]
		filenumber=numberwithext.split(".")[0]
		floatnumber=int(filenumber)
		
		if newnumber!=filenumber:
			print(file)
		
		newnumber=str((floatnumber+1)).zfill(4)
		

	

		
