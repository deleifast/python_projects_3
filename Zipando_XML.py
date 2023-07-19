import os 
from zipfile import ZipFile
from os import walk

os.chdir('c://pdv/xml')

current_directory = 'c://pdv/xml'
total = 0
cnt = 0
zip_list = []
name_count = 0 

file_names = os.listdir(current_directory)
file_count = len(os.listdir(current_directory))

while cnt<file_count:
    zip_list = []
    if file_count-cnt>9:
        zip_list = file_names[cnt:cnt+10]
        cnt = cnt+10
    else:
        zip_list = file_names[cnt:]
        cnt = file_count
    name_count +=1
    with ZipFile(str(name_count)+'.zip', 'w') as myzip:
        for f in zip_list:
            myzip.write(f)

