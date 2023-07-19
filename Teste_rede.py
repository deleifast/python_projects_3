import subprocess, socket, os, sys, os.path

# initialize
driveLetter = 'X:' 
networkPath = '\\\\192.168.14.115\Atual' 
user = 'remarca' 
password = 'remarca'

# Connect to map network drive to letter Q
winCMD = 'NET USE ' + driveLetter + ' ' + networkPath + ' /User:' + user + ' ' + password

exitcode = subprocess.call(winCMD, shell=True)
print (exitcode)
if exitcode == 0:
	print(winCMD)

else:
		path = "c:\pdv\prini"
		dir = os.listdir(path)
		for file in dir:
			if file == "caixa.txt":
				os.remove(file)

		ips = subprocess.check_output("ipconfig").decode('utf-8')
		print (ips)
		with open('caixa.txt', 'a') as caixa:
			caixa.write(ips)
			caixa.close()


