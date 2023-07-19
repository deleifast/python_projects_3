import configparser
config = configparser.ConfigParser()
config['SALCOMM']={}
config['PRINCIPAL']['LOG']='SIM'
with open('SALCOMM.INI', 'w') as configfile:
	config.write(configfile)
