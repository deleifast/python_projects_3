import os
import zipfile
 
# Method extract files from a zip.
def unzip(path):
	file = zipfile.ZipFile(path, "r")
 # list file information
	for info in file.infolist():
		print (info.filename, info.date_time, info.file_size)
 # list filenames
	for name in file.namelist():
		 if not os.path.exists(os.path.dirname(name)):

 # Create that directory
os.mkdir(os.path.dirname(name))
 # Take extension
ext = os.path.splitext(name)[1]
 # check extension file
if ext in (".txt"):
	
 # Write files to disk
	temp = open(name, "wb") # create the file
	data = file.read(name) #read the binary data
	temp.write(data)
	temp.close()
	file.close()
 
# List all *.zip files and extract them.
def list_dir(dir):

 #filename = "C:tempextract"
	for pathzip in os.listdir(dir):
		extzip = os.path.splitext(pathzip)[1]
		if extzip in (".zip"):

 # Call unzip method (Extract Files)
			unzip(pathzip)
			print ("Extracted files")
 
#---MAIN---
if __name__ == "__main__":
	dir = raw_input("Directory: ").strip()
	list_dir(dir)