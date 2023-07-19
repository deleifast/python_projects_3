import os 
import time, glob, re
import datetime as dt

path = 'c://programas_python//ip.txt'
  
modification_time = os.path.getmtime(path) 
file_time = dt.datetime.fromtimestamp(os.path.getmtime(path))
print("Last modification time since the epoch:", modification_time, file_time) 
  
local_time = time.ctime(modification_time) 
print("Last modification time(Local time):", local_time)

print(file_time.strftime("%d/%m/%Y"))

path = "c://pdv"

files = glob.glob(os.path.join(path,'pdvsal.exe'))
files.sort(key=lambda x:[int(c) if c.isdigit() else c for c in re.split(r'(\d+)', x)])

files1 = glob.glob(os.path.join(path,'satsal.dll'))
files1.sort(key=lambda x:[int(c) if c.isdigit() else c for c in re.split(r'(\d+)', x)])

files2 = glob.glob(os.path.join(path,'nfce.dll'))
files2.sort(key=lambda x:[int(c) if c.isdigit() else c for c in re.split(r'(\d+)', x)])


with open('versao_pdv.txt',"w") as stream:
	for file in (files, files1, files2):
		file_time = dt.datetime.fromtimestamp(os.path.getmtime(path))
		print(file,('-'), file_time.strftime("%d/%m/%Y"), file=stream)
