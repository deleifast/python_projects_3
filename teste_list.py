arquivo = open('relsat_loja01.txt', "w")
lista = [linha.strip() for linha in arquivo]
arquivo.close()
print (lista) 
