#encoding: iso-8859-1

import os, shutil, time, datetime
from pathlib import Path
from datetime import datetime

t = datetime.now().strftime("%d-%m-%Y")

if os.path.exists('c:\pdv\versões_anteriores_'+(t)):
	print ('existe')

else:
	dir = './versões_anteriores_'+(t)
	os.makedirs(dir)

current_directory = os.path.dirname(os.path.abspath(__file__))
shutil.rmtree(current_directory + '\versões_anteriores_'+(t))


source = os.listdir("c://pdv")
destination = 'c://pdv/versões_anteriores_'+(t)
for files in source:
    if files.startswith("pdvsal.exe"):
        shutil.move(files,destination)



	
