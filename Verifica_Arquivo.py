import os
import os.path
import glob
import shutil

PATHPDV='X://PDV.ZIP'
PATHPLUGIN='X://PLUGIN.ZIP'

if os.path.isfile(PATHPDV):

	dest_dir = "C:\\PDV"
	for file in glob.glob(r'X:/PDV.ZIP'):
		print(file)
	shutil.copy(file, dest_dir)

else:
	print("Sem arquivo(PDV) para atualizar no Servidor")

if os.path.isfile(PATHPLUGIN):

	dest_dir = "C:\\PDV\PLUGIN"
	for file in glob.glob(r'X:/PLUGIN.ZIP'):
		print(file)
	shutil.copy(file, dest_dir)

else:
	print("Sem arquivo(PLUGIN) para atualizar no Servidor")

'''PATH='C://PDV/PLUGIN/PLUGIN.ZIP'

if os.path.isfile(PATH) and os.access(PATH, os.R_OK):
	os.remove("C://PDV/PLUGIN/PLUGIN.zip")

	dest_dir = "C:\\PDV\PLUGIN"
	for file in glob.glob(r'X:/PLUGIN.ZIP'):
		print(file)
	shutil.copy(file, dest_dir)

else:
	dest_dir = "C:\\PDV\PLUGIN"
	for file in glob.glob(r'X:/PLUGIN.ZIP'):
		print(file)
	shutil.copy(file, dest_dir) '''
