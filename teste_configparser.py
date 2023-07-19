from configparser import ConfigParser
config = ConfigParser()

print(config.sections())

config.read('pdvsal.ini')
print(config.sections())
