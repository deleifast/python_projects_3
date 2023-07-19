import  sqlite3
conn = sqlite3.connect('dnslj01.db')
c = conn.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS endereco (caixa TEXT, ip TEXT)''')

try:
	
    with open("C:\Remarca\lojas\lj01.ip_101.txt", "r") as f:
        rows = f.readlines()
        for row in rows:
            fields = row.split(' ')
            c.execute(f'INSERT INTO endereco (caixa, ip)'\
                    f"VALUES ('{fields[0]}','{fields[1]}')")
except:
    pass

conn.commit()

for row in c.execute('SELECT * FROM endereco'):
    print(row)

conn.close()
