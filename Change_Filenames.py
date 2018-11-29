
from os import listdir, rename
from os.path import isfile, join
import shutil

mypath=r'F:\F04_Cycle1330Filesrenamed'
newpath=r'F:\F04_Cycle1330Filesrenamed'
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

prefix="F04_"
oldprefix="F04_Cycle1300_fibre 3"
startnumber=259

copy=False

for file in onlyfiles:
	if oldprefix in file:
	
		numberwithext=file.split("_")[-1]
		fibre=file.split("_")[-2]
		filenumber=numberwithext.split(".")[0]
		floatnumber=int(filenumber)
		newnumber=str((floatnumber+startnumber)).zfill(4)
		
		newfilename=prefix+fibre+"_"+newnumber+".obr"
		
		dst_dir=join(newpath,newfilename)
		src_dir=join(mypath,file)
		print(file)
		print(newfilename)
		

		if copy:
		
			shutil.copy(src_dir,dst_dir)
			
		else:
			src_dir=src_dir=join(newpath,file)
			rename(src_dir,dst_dir)
		
