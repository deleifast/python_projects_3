import configparser
import pyodbc

config = configparser.ConfigParser()    
config.read('db_connect.ini')

constr = 'DRIVER={{{drv}}};DATABASE={db};Trusted_Connection={tc};'\
              .format(drv=config['SERVER']['driver'],
                      db=config['SERVER']['database'],
                      tc=config['SERVER']['Trusted_Connection'])

conn = pyodbc.connect(constr)
