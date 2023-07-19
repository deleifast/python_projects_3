import os, re, glob, time

path = 'c:\pdv'
#files = glob.glob(os.path.join('salcomm.exe'))
#files.sort(key=lambda x:[int(c) if c.isdigit() else c for c in re.split(r'(\d+)', x)])

#files1 = glob.glob(os.path.join('clisitef32i.dll'))
#files1.sort(key=lambda x:[int(c) if c.isdigit() else c for c in re.split(r'(\d+)', x)])

files2 = sorted(glob.glob('pdvsal.exe'), key=os.path.getmtime)
#with open('versao_pdv.txt',"w") as stream:
#	for file in files:
#		print("{} - {}".format(file, time.ctime(os.path.getmtime(file))), file=stream)

#with open('versao_pdv.txt',"a") as stream:
#	for file in files1:
#		print("{} - {}".format(file, time.ctime(os.path.getmtime(file))), file=stream)

with open('versao_pdv.txt',"w") as stream:
	for file in files2:
		print("{} - {}".format(file, time.ctime(os.path.getmtime(file))), file=stream)
