
palavras = set()
with open('c:/remarca/lojas/lj01.verpdv_101.txt') as arq:
    for linha in arq: # para cada linha do arquivo
        for palavra in linha.split('c:\\pdv'): # para cada palavra da linha
            palavras.add(palavra) # adiciona a palavra no set

palavras_em_ordem = sorted(palavras)
print(palavras_em_ordem)
