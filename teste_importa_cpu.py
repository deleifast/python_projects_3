import  sqlite3
conn = sqlite3.connect('cpulj01.db')
c = conn.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS cpu (caixa TEXT, cpu TEXT, memoria TEXT, disco_total TEXT, disco_usado TEXT, disco_livre TEXT)''')

try:
	
    with open("C:\Remarca\lojas\lj01.cpu_101.txt", "r") as f:
        rows = f.readlines()
        for row in rows:
            fields = row.split(',')
            c.execute(f'INSERT INTO cpu (caixa, cpu, memoria, disco_total, disco_usado, disco_livre)'\
                    f"VALUES ('{fields[0]}','{fields[1]}','{fields[2]}','{fields[3]}','{fields[4]}','{fields[5]}')")
except:
    pass
conn.commit()

for row in c.execute('SELECT * FROM cpu'):
    print(row)

conn.close()
