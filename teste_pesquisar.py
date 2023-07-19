def pesquisar_registro( txt, posicao ):
	
	resultado = ""
	with open( 'clitef15.log', 'r' ) as a:
		for linha in a:
			if resultado == "":
				if txt in linha:
					resultado = linha
					res = resultado.split('= ')[posicao].strip('\n')
					return res;
		else: a.close()
	return None;


print (pesquisar_registro( 'cupom', 1 )) # Nome da variavel e posição do resultado dsp do '='

