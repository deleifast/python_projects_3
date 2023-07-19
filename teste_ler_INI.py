#encoding: iso-8859-1
import configparser
 
config = configparser.ConfigParser(defaults=None, strict=False, allow_no_value=True)
config.optionxform = str

config.read('PDVSAL.INI')

caixa = config.get('IMPRESSORA','CAIXA')
modelo = config.get('IMPRESSORA','MODELO')
with open("printer_cx01.txt", "w") as stream:
	print("Pdv 01 -", "Sat:",caixa,"Impressora:",modelo, file=stream)

