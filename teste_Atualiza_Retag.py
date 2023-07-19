import os, shutil, subprocess, time, glob, sys, os.path

# initialize
driveLetter = 'Q:' 
networkPath = '\\\\LABSALINHA\C$' 
user = 'Administrador' 
password = 'remarca'

# Connect to map network drive to letter Q
winCMD = 'NET USE ' + driveLetter + ' ' + networkPath + ' /User:' + user + ' ' + password
print(winCMD)
subprocess.call(winCMD, shell=True)

os.chdir('Q:\\')
os.remove('Q://Retag/retag.old')
os.system("taskkill /s LABSALINHA /u Administrador /p remarca /im RETAG.EXE")
os.rename('Q://Retag/retag.exe','Q://Retag/retag.old')

print('Copiando arquivos para o Retag, aguarde....')
time.sleep(5)

dest_dir = "Q:\\RETAG"
for file in glob.glob(r'C:/Atualizacao_Retag/*.EXE'):
	print(file)
	shutil.copy(file, dest_dir)

dest_dir = "Q:\\RETAG\PLUGIN"
for file in glob.glob(r'C:/Atualizacao_Retag/Plugin/*.DLL'):
	print(file)
	shutil.copy(file, dest_dir)

os.chdir('Q:\\RETAG')

print ("Diretorio atual: %s" % os.getcwd())

os.system("psexec.exe -d -i -u remarca\Administrador -p remarca \\\\LABSALINHA ""c://windows/system32/taskmgr.exe")
time.sleep(5)
os.system("psexec.exe -d -i -u remarca\Administrador -p remarca \\\\LABSALINHA ""c://retag/retag.exe")
time.sleep(5)
os.system("taskkill /s LABSALINHA /u Administrador /p remarca /im TASKMGR.EXE")

# Disconnect anything on drive letter Q
winCMD = 'NET USE ' + driveLetter + ' /delete /yes'
print(winCMD)
subprocess.call(winCMD, shell=True)


