import os
import shutil

pastaOld = 'C:/enviados/'
pastaNew = 'C:/envio/'

#pegando a lista de arquivos dentro de cada pasta
old = os.listdir(pastaOld)
new = os.listdir(pastaNew)

print('old: {}'.format(old))
print('new: {}'.format(new))

#fazendo a interseção de cada pasta e imprimindo
inter = list(set(old).intersection(new))
print('intersection: {}'.format(inter))

# removendo os items da pasta antiga
[os.remove(pastaOld + item) for item in inter]

# movendo os arquivos da pasta new para a pasta old
[shutil.move(pastaNew + item, pastaOld + item) for item in new]
