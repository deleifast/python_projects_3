import pyodbc

dbpath = "c:\\pdv\plu.mdb"
driver = "{Microsoft Access Driver (*.mdb, *.accdb)}"
conn = pyodbc.connect("DRIVER={};DBQ={}".format(driver, dbpath))

cursor = conn.cursor()

cursor.execute("SELECT top 5 * FROM Produtos")
for row in cursor:
	print (row.CODIGO, row.NOME_C)