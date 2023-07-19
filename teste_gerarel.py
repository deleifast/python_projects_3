#encoding: iso-8859-1
from pathlib import Path
import os

    
os.chdir("c:\\remarca\\lojas")

try:
    with open("relimp_lojas.txt", "w") as f:
        for file in Path('c:\\remarca\\lojas').glob('lj*.imp_*.txt'):
            print(file.read_text(), file= f)
except FileNotFoundError:
    print("Arquivo não encontrado", file=f)

try:
    with open('relimp_lojas.txt', 'r') as fr:
        lines = fr.readlines()
        min_len = 7

        with open('relimp_lojas.txt', 'w') as fw:
            for line in lines:
                if len(line.strip('\n')) >= min_len:
                    fw.write(line)
                    print(line)
except:
    pass

try:
    with open("relip_lojas.txt", "w") as f:
        for file in Path('c:\\remarca\\lojas').glob('lj*.ip_*.txt'):
            print(file.read_text(), file= f)
except FileNotFoundError:
    print("Arquivo não encontrado", file=f)

try:
    with open('relip_lojas.txt', 'r') as fr:
        lines = fr.readlines()
        min_len = 7

        with open('relip_lojas.txt', 'w') as fw:
            for line in lines:
                if len(line.strip('\n')) >= min_len:
                    fw.write(line)
                    print(line)
except:
    pass

try:
    with open("relcpu_lojas.txt", "w") as f:
        for file in Path('c:\\remarca\\lojas').glob('lj*.cpu_*.txt'):
            print(file.read_text(), file= f)
except FileNotFoundError:
    print("Arquivo não encontrado", file=f)

try:
    with open('relcpu_lojas.txt', 'r') as fr:
        lines = fr.readlines()
        min_len = 7

        with open('relcpu_lojas.txt', 'w') as fw:
            for line in lines:
                if len(line.strip('\n')) >= min_len:
                    fw.write(line)
                    print(line)
except:
    pass

try:
    with open("relverpdv_lojas.txt", "w") as f:
        for file in Path('c:\\remarca\\lojas').glob('lj*.verpdv_*.txt'):
            print(file.read_text(), file= f)
except FileNotFoundError:
    print("Arquivo não encontrado", file=f)

try:
    with open('relverpdv_lojas.txt', 'r') as fr:
        lines = fr.readlines()
        min_len = 7

        with open('relverpdv_lojas.txt', 'w') as fw:
            for line in lines:
                if len(line.strip('\n')) >= min_len:
                    fw.write(line)
                    print(line)
except:
    pass

try:
    with open("reldns_lojas.txt", "w") as f:
        for file in Path('c:\\remarca\\lojas').glob('lj*.dns_*.txt'):
            print(file.read_text(), file= f)
except FileNotFoundError:
    print("Arquivo não encontrado", file=f)

try:
    with open('reldns_lojas.txt', 'r') as fr:
        lines = fr.readlines()
        min_len = 7

        with open('reldns_lojas.txt', 'w') as fw:
            for line in lines:
                if len(line.strip('\n')) >= min_len:
                    fw.write(line)
                    print(line)
except:
    pass

try:
    with open("relkey_lojas.txt", "w") as f:
        for file in Path('c:\\remarca\\lojas').glob('lj*.key_*.txt'):
            print(file.read_text(), file= f)
except FileNotFoundError:
    print("Arquivo não encontrado", file=f)

try:
    with open('relkey_lojas.txt', 'r') as fr:
        lines = fr.readlines()
        min_len = 7

        with open('relkey_lojas.txt', 'w') as fw:
            for line in lines:
                if len(line.strip('\n')) >= min_len:
                    fw.write(line)
                    print(line)
except:
    pass
'''
try:
    f = open('relkey_lojas.txt','r')
    a = ['LTSC','2019']
    lst = []
    for line in f:
        for word in a:
            if word in line:
                line = line.replace(word,'')
        lst.append(line)
    f.close()
    f = open('relkey_lojas.txt','w')
    for line in lst:
        f.write(line)
    f.close()
except:
    pass
'''
try:
    with open("relsat_lojas.txt", "w") as f:
        for file in Path('c:\\remarca\\lojas').glob('lj*.sat_*.txt'):
            print(file.read_text(), file= f)
except FileNotFoundError:
    print("Arquivo não encontrado", file=f)

try:
    with open('relsat_lojas.txt', 'r') as fr:
        lines = fr.readlines()
        min_len = 7

        with open('relsat_lojas.txt', 'w') as fw:
            for line in lines:
                if len(line.strip('\n')) >= min_len:
                    fw.write(line)
                    print(line)
except:
    pass


