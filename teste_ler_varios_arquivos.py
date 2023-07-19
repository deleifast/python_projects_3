def multi_open(_list):
    out=""
    for x in _list:
        try:
            with open(x) as f:
                out+=f.read()
        except:
            pass
            # print(f"Cannot open file {x}")
    return(out)

fl = ["C:/REMARCA/lojas/lj01.sat_101.txt", "C:/REMARCA/lojas/lj01.key_101.txt"]
print('Caixa01 -', multi_open(fl))
