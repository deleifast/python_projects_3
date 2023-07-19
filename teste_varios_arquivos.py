import os

try:
	if os.path.exists('rel_loja01.txt'):
		os.remove('rel_loja01.txt')
	else:
		pass

	with open("rel_loja01.txt", "w") as file:
		for temp in ["C:/REMARCA/lojas/lj01.cpu_101.txt", "C:/REMARCA/lojas/lj01.key_101.txt","C:/REMARCA/lojas/lj01.Caixa01lj01.txt"]:
			with open(temp, "r") as t:
				file.writelines(t)
except FileNotFoundError:
			with open("rel_loja01.txt", "a") as arquivo:
					print('Caixa01 -  SEM CONEXÃO OU PDV COM DEFEITO', file=arquivo)

try:	
	with open("rel_loja01.txt", "a") as file:
		for temp in ["C:/REMARCA/lojas/lj01.cpu_102.txt", "C:/REMARCA/lojas/lj01.key_102.txt","C:/REMARCA/lojas/lj01.Caixa02lj01.txt"]:
			with open(temp, "r") as t:
				file.writelines(t)
except FileNotFoundError:
			with open("rel_loja01.txt", "a") as arquivo:
					print('Caixa02 -  SEM CONEXÃO OU PDV COM DEFEITO', file=arquivo)
try:	
	with open("rel_loja01.txt", "a") as file:
		for temp in ["C:/REMARCA/lojas/lj01.cpu_103.txt", "C:/REMARCA/lojas/lj01.key_103.txt","C:/REMARCA/lojas/lj01.Caixa03lj01.txt"]:
			with open(temp, "r") as t:
				file.writelines(t)
except FileNotFoundError:
			with open("rel_loja01.txt", "a") as arquivo:
					print('Caixa03 -  SEM CONEXÃO OU PDV COM DEFEITO', file=arquivo)
try:	
	with open("rel_loja01.txt", "a") as file:
		for temp in ["C:/REMARCA/lojas/lj01.cpu_128.txt", "C:/REMARCA/lojas/lj01.key_128.txt","C:/REMARCA/lojas/lj01.Caixa04lj01.txt"]:
			with open(temp, "r") as t:
				file.writelines(t)
except FileNotFoundError:
			with open("rel_loja01.txt", "a") as arquivo:
					print('Caixa04 -  SEM CONEXÃO OU PDV COM DEFEITO', file=arquivo)
try:	
	with open("rel_loja01.txt", "a") as file:
		for temp in ["C:/REMARCA/lojas/lj01.cpu_105.txt", "C:/REMARCA/lojas/lj01.key_105.txt","C:/REMARCA/lojas/lj01.pdv-emprestimo.txt"]:
			with open(temp, "r") as t:
				file.writelines(t)
except FileNotFoundError:
			with open("rel_loja01.txt", "a") as arquivo:
					print('Caixa05 -  SEM CONEXÃO OU PDV COM DEFEITO', file=arquivo)
try:	
	with open("rel_loja01.txt", "a") as file:
		for temp in ["C:/REMARCA/lojas/lj01.cpu_106.txt", "C:/REMARCA/lojas/lj01.key_106.txt","C:/REMARCA/lojas/lj01.Caixa06lj01.txt"]:
			with open(temp, "r") as t:
				file.writelines(t)
except FileNotFoundError:
			with open("rel_loja01.txt", "a") as arquivo:
					print('Caixa06 -  SEM CONEXÃO OU PDV COM DEFEITO', file=arquivo)
try:	
	with open("rel_loja01.txt", "a") as file:
		for temp in ["C:/REMARCA/lojas/lj01.cpu_107.txt", "C:/REMARCA/lojas/lj01.key_107.txt","C:/REMARCA/lojas/lj01.Caixa07lj01.txt"]:
			with open(temp, "r") as t:
				file.writelines(t)
except FileNotFoundError:
			with open("rel_loja01.txt", "a") as arquivo:
					print('Caixa07 -  SEM CONEXÃO OU PDV COM DEFEITO', file=arquivo)
try:	
	with open("rel_loja01.txt", "a") as file:
		for temp in ["C:/REMARCA/lojas/lj01.cpu_108.txt", "C:/REMARCA/lojas/lj01.key_108.txt","C:/REMARCA/lojas/lj01.Caixa08lj01.txt"]:
			with open(temp, "r") as t:
				file.writelines(t)
except FileNotFoundError:
			with open("rel_loja01.txt", "a") as arquivo:
					print('Caixa08 -  SEM CONEXÃO OU PDV COM DEFEITO', file=arquivo)
try:	
	with open("rel_loja01.txt", "a") as file:
		for temp in ["C:/REMARCA/lojas/lj01.cpu_109.txt", "C:/REMARCA/lojas/lj01.key_109.txt","C:/REMARCA/lojas/lj01.Caixa09lj01.txt"]:
			with open(temp, "r") as t:
				file.writelines(t)
except FileNotFoundError:
			with open("rel_loja01.txt", "a") as arquivo:
					print('Caixa09 -  SEM CONEXÃO OU PDV COM DEFEITO', file=arquivo)
try:	
	with open("rel_loja01.txt", "a") as file:
		for temp in ["C:/REMARCA/lojas/lj01.cpu_110.txt", "C:/REMARCA/lojas/lj01.key_110.txt","C:/REMARCA/lojas/lj01.Caixa10lj01.txt"]:
			with open(temp, "r") as t:
				file.writelines(t)
except FileNotFoundError:
			with open("rel_loja01.txt", "a") as arquivo:
					print('Caixa10 -  SEM CONEXÃO OU PDV COM DEFEITO', file=arquivo)
try:	
	with open("rel_loja01.txt", "a") as file:
		for temp in ["C:/REMARCA/lojas/lj01.cpu_111.txt", "C:/REMARCA/lojas/lj01.key_111.txt","C:/REMARCA/lojas/lj01.Caixa11lj01.txt"]:
			with open(temp, "r") as t:
				file.writelines(t)
except FileNotFoundError:
			with open("rel_loja01.txt", "a") as arquivo:
					print('Caixa11 -  SEM CONEXÃO OU PDV COM DEFEITO', file=arquivo)
try:	
	with open("rel_loja01.txt", "a") as file:
		for temp in ["C:/REMARCA/lojas/lj01.cpu_112.txt", "C:/REMARCA/lojas/lj01.key_112.txt","C:/REMARCA/lojas/lj01.Caixa12lj01.txt"]:
			with open(temp, "r") as t:
				file.writelines(t)
except FileNotFoundError:
			with open("rel_loja01.txt", "a") as arquivo:
					print('Caixa12 -  SEM CONEXÃO OU PDV COM DEFEITO', file=arquivo)
try:	
	with open("rel_loja01.txt", "a") as file:
		for temp in ["C:/REMARCA/lojas/lj01.cpu_113.txt", "C:/REMARCA/lojas/lj01.key_113.txt","C:/REMARCA/lojas/lj01.Caixa13lj01.txt"]:
			with open(temp, "r") as t:
				file.writelines(t)
except FileNotFoundError:
			with open("rel_loja01.txt", "a") as arquivo:
					print('Caixa13 -  SEM CONEXÃO OU PDV COM DEFEITO', file=arquivo)
try:	
	with open("rel_loja01.txt", "a") as file:
		for temp in ["C:/REMARCA/lojas/lj01.cpu_114.txt", "C:/REMARCA/lojas/lj01.key_114.txt","C:/REMARCA/lojas/lj01.Caixa14lj01.txt"]:
			with open(temp, "r") as t:
				file.writelines(t)
except FileNotFoundError:
			with open("rel_loja01.txt", "a") as arquivo:
					print('Caixa14 -  SEM CONEXÃO OU PDV COM DEFEITO', file=arquivo)
try:	
	with open("rel_loja01.txt", "a") as file:
		for temp in ["C:/REMARCA/lojas/lj01.cpu_115.txt", "C:/REMARCA/lojas/lj01.key_115.txt","C:/REMARCA/lojas/lj01.Caixa15lj01.txt"]:
			with open(temp, "r") as t:
				file.writelines(t)
except FileNotFoundError:
			with open("rel_loja01.txt", "a") as arquivo:
					print('Caixa15 -  SEM CONEXÃO OU PDV COM DEFEITO', file=arquivo)
try:	
	with open("rel_loja01.txt", "a") as file:
		for temp in ["C:/REMARCA/lojas/lj01.cpu_116.txt", "C:/REMARCA/lojas/lj01.key_116.txt","C:/REMARCA/lojas/lj01.Caixa16lj01.txt"]:
			with open(temp, "r") as t:
				file.writelines(t)
except FileNotFoundError:
			with open("rel_loja01.txt", "a") as arquivo:
					print('Caixa16 -  SEM CONEXÃO OU PDV COM DEFEITO', file=arquivo)
try:	
	with open("rel_loja01.txt", "a") as file:
		for temp in ["C:/REMARCA/lojas/lj01.cpu_117.txt", "C:/REMARCA/lojas/lj01.key_117.txt","C:/REMARCA/lojas/lj01.Caixa17lj01.txt"]:
			with open(temp, "r") as t:
				file.writelines(t)
except FileNotFoundError:
			with open("rel_loja01.txt", "a") as arquivo:
					print('Caixa17 -  SEM CONEXÃO OU PDV COM DEFEITO', file=arquivo)
try:	
	with open("rel_loja01.txt", "a") as file:
		for temp in ["C:/REMARCA/lojas/lj01.cpu_118.txt", "C:/REMARCA/lojas/lj01.key_118.txt","C:/REMARCA/lojas/lj01.Caixa18lj01.txt"]:
			with open(temp, "r") as t:
				file.writelines(t)
except FileNotFoundError:
			with open("rel_loja01.txt", "a") as arquivo:
					print('Caixa18 -  SEM CONEXÃO OU PDV COM DEFEITO', file=arquivo)
try:	
	with open("rel_loja01.txt", "a") as file:
		for temp in ["C:/REMARCA/lojas/lj01.cpu_119.txt", "C:/REMARCA/lojas/lj01.key_119.txt","C:/REMARCA/lojas/lj01.Caixa19lj01.txt"]:
			with open(temp, "r") as t:
				file.writelines(t)
except FileNotFoundError:
			with open("rel_loja01.txt", "a") as arquivo:
					print('Caixa19 -  SEM CONEXÃO OU PDV COM DEFEITO', file=arquivo)
try:	
	with open("rel_loja01.txt", "a") as file:
		for temp in ["C:/REMARCA/lojas/lj01.cpu_120.txt", "C:/REMARCA/lojas/lj01.key_120.txt","C:/REMARCA/lojas/lj01.Caixa20lj01.txt"]:
			with open(temp, "r") as t:
				file.writelines(t)
except FileNotFoundError:
			with open("rel_loja01.txt", "a") as arquivo:
					print('Caixa20 -  SEM CONEXÃO OU PDV COM DEFEITO', file=arquivo)
try:	
	with open("rel_loja01.txt", "a") as file:
		for temp in ["C:/REMARCA/lojas/lj01.cpu_121.txt", "C:/REMARCA/lojas/lj01.key_121.txt","C:/REMARCA/lojas/lj01.Caixa21lj01.txt"]:
			with open(temp, "r") as t:
				file.writelines(t)
except FileNotFoundError:
			with open("rel_loja01.txt", "a") as arquivo:
					print('Caixa21 -  SEM CONEXÃO OU PDV COM DEFEITO', file=arquivo)
try:	
	with open("rel_loja01.txt", "a") as file:
		for temp in ["C:/REMARCA/lojas/lj01.cpu_122.txt", "C:/REMARCA/lojas/lj01.key_122.txt","C:/REMARCA/lojas/lj01.Caixa22lj01.txt"]:
			with open(temp, "r") as t:
				file.writelines(t)
except FileNotFoundError:
			with open("rel_loja01.txt", "a") as arquivo:
					print('Caixa22 -  SEM CONEXÃO OU PDV COM DEFEITO', file=arquivo)
try:	
	with open("rel_loja01.txt", "a") as file:
		for temp in ["C:/REMARCA/lojas/lj01.cpu_123.txt", "C:/REMARCA/lojas/lj01.key_123.txt","C:/REMARCA/lojas/lj01.Caixa23lj01.txt"]:
			with open(temp, "r") as t:
				file.writelines(t)
except FileNotFoundError:
			with open("rel_loja01.txt", "a") as arquivo:
					print('Caixa23 -  SEM CONEXÃO OU PDV COM DEFEITO', file=arquivo)
try:	
	with open("rel_loja01.txt", "a") as file:
		for temp in ["C:/REMARCA/lojas/lj01.cpu_124.txt", "C:/REMARCA/lojas/lj01.key_124.txt","C:/REMARCA/lojas/lj01.Caixa24lj01.txt"]:
			with open(temp, "r") as t:
				file.writelines(t)
except FileNotFoundError:
			with open("rel_loja01.txt", "a") as arquivo:
					print('Caixa24 -  SEM CONEXÃO OU PDV COM DEFEITO', file=arquivo)
