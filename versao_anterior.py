#encoding: iso-8859-1

import os, shutil, time, datetime
from pathlib import Path
from datetime import datetime
from threading import Thread

os.chdir('C:\\PDV')

atual = input('Nome do programa que ser� atualizado: ')

t = datetime.now().strftime("%d-%m-%Y")

os.rename(atual, atual+(t))

src=atual+(t)
dst="C://REMARCA/vers�es_anteriores"

Thread(target=shutil.copy, args=[src, dst]).start()

print (dst)
print (src)
	
