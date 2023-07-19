from satcfe import BibliotecaSAT
from satcfe import ClienteSATLocal
cliente = ClienteSATLocal(
         BibliotecaSAT('/pdv/dllsat32bits.dll'),  # ou DLL no Windows
         codigo_ativacao='123123123')

resposta = cliente.consultar_sat()

print (resposta.msg)
