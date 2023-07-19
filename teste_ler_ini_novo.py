import configparser, subprocess

config = configparser.ConfigParser(defaults=None, strict=False, allow_no_value=True)
config.optionxform = str

try:
    config.read('config.ini')
    letra = config.get('dados', 'path')
    endereco = config.get('dados','ip')
    usuario = config.get('dados', 'user')
    senha = config.get('dados', 'senha')

    winCMD = 'NET USE ' + letra + ' ' + '\\\\'  + endereco + ' ' + '/User:' + usuario + ' ' + senha
    exitcode = subprocess.call(winCMD, shell=True)
    print (exitcode)

except:
    pass
    print("Sem arquivo config.ini, verificar!!!")


#config.set('dados', 'nome', 'paulo')

