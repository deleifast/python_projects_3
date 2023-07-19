import configparser
config = configparser.ConfigParser()
config['NFCE']={}
config['NFCE']['TPEMIS']='9'
with open('MODONFCE.INI', 'w') as configfile:
	config.write(configfile)