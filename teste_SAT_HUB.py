from satcfe import ClienteSATHub

cliente = ClienteSATHub('192.168.141.14', 8088, numero_caixa=124)
resposta = cliente.consultar_sat()