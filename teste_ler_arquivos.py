import os, os.path

os.chdir('C:\REMARCA\cx10')

with open("sat_cx10.txt", "w") as stream:
	for line in open('sat.txt'):
		print('Caixa10 - ', (line).rstrip(), file=stream)
