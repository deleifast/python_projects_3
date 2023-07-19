import os, glob

for file in glob.glob('*.dll'):
	if file.startswith('S'):
		os.startfile('SAT_SWEDA.exe')
	else:
		os.startfile('SAT_DIMEP.exe')
			