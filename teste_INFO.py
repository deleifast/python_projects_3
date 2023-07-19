#encoding: iso-8859-1

import os, time, subprocess, shutil, os.path, sys, glob

os.chdir('C:\\PDV')

try:
	f = open('versao_pdv.txt','r')
	f.close()
	
	with open("pdv_cx01.txt", "w") as stream:
		for line in open('pdvsal.ini'):
			palavra = ('CAIXA')
			if palavra in line:
				with open("pdv_cx01.txt", "a") as stream:
					for line1 in open('versao_pdv.txt'):
						print('Checkout 01 -', (line), (line1), file=stream)

except FileNotFoundError:
	with open("pdv_cx01.txt", "w") as stream:
			print('Caixa01 -  SEM ARQUIVO - VERSÃO_PDV.TXT NA PASTA PDV, ATUALIZAR  - PDVCORAL-LOJA14.EXE', file=stream)

dest_dir = "C:\\REMARCA\cx01"
for file in glob.glob(r'C:/pdv/pdv_cx01.txt'):
	print(file)
	shutil.copy(file, dest_dir)
