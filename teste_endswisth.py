import os, shutil
try:
	for arquivo in os.listdir('c://pdv'):
	  x = arquivo
	  os.rename(x,x.lower())
except OSError:
	pass
	

