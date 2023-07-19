import subprocess

driveLetter = 'X:' 
networkPath = '\\\\10.0.20.42\atual' 
user = 'compartilhar' 
password = 'ruaf305'

winCMD = 'NET USE ' + driveLetter + ' ' + networkPath + ' /User:' + user + ' ' + password
subprocess.call(winCMD, shell=True)
