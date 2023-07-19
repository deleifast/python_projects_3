import os
import glob

current_directory = os.path.dirname(os.path.abspath(__file__))

os.chdir('C:\LOG')

files = glob.glob('*.*')
for file in files:
	print(file)
	os.unlink(file)
	os.remove(file)
