import shutil
import os
import xml.etree.ElementTree as ET

def obter_cnpj_emissor( arquivoNFe ):
    nsNFe = {'nfe': 'http://www.portalfiscal.inf.br/nfe'}
    root = ET.parse( arquivoNFe ).getroot()
    node = root.findall( "./nfe:tPag", nsNFe )
    if( len(node) != 1 ):
        return None
    return node[0].text

def obter_arquivos_xml( diretorio ):
    return [ os.path.join( diretorio, arq ) for arq in os.listdir( diretorio ) if arq.endswith(".xml") ]

def copiar_arquivos( origem, destino, cnpj ):
    for arquivo in obter_arquivos_xml( origem ):
        if( cnpj == obter_cnpj_emissor( arquivo ) ):
            print( "CNPJ '{}' encontrado no arquivo '{}'...".format(cnpj,arquivo) )
            print( "Copiando arquivo '{}' para diretorio '{}'".format(arquivo,destino) )
            shutil.copy( arquivo, destino )
        else:
            print("CNPJ '{}' NAO ENCONTRADO no arquivo '{}'.".format(cnpj,arquivo))
            
copiar_arquivos('c:\programas_python','c:\programas_python\data','15347973000179')            

    
