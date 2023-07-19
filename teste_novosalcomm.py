#encoding: iso-8859-1

import os, shutil, subprocess, time, glob, sys, os.path, socket, datetime
from pathlib import Path
from datetime import datetime

# Mapeando drive de rede
driveLetter = 'Q:' 
networkPath = '\\\\192.168.141.14\C$' 
user = 'pdv' 
password = 'pdv'

winCMD = 'NET USE ' + driveLetter + ' ' + networkPath + ' /User:' + user + ' ' + password
exitcode = subprocess.call(winCMD, shell=True)
print (exitcode)

if exitcode == 2:
	
		exitcode == 2

		os.chdir('C:\\Remarca')

		path = 'C:\\Remarca'
		dir = os.listdir(path)
		for file in dir:
			if file == "pdv_cx14_lj14.txt":
				os.remove(file)

		with open('pdv_cx14_lj14.txt', 'a') as caixa:
			caixa.write('Salcomm não alterado')
			caixa.close()


else:
		exitcode == 0
		print("Conectado Caixa 14")

		os.chdir('C:\\REMARCA')

		t = datetime.now().strftime("%d-%m-%Y")

		os.rename('Q://PDV/Salcomm.ini','Q://PDV/Salcomm.'+(t))
		
		print('Copiando Salcomm.ini, aguarde....')
		time.sleep(10)

		dest_dir = "Q:\\PDV"
		for file in glob.glob(r'C:/REMARCA/Salcomm.ini'):
			print(file)
		shutil.copy(file, dest_dir)
		
		
		# Desconectando drive Q
		winCMD = 'NET USE ' + driveLetter + ' /delete /yes'
		print(winCMD)
		subprocess.call(winCMD, shell=True)

