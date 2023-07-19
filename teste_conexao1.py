import win32com.client
import pyodbc
'''
def ado():

 
  connect with com dispatch objs
  
	conn = win32com.client.Dispatch(r'ADODB.Connection')
	DSN = ('PROVIDER = Microsoft.Jet.OLEDB.4.0;DATA SOURCE = ' + db +  ';')
	conn.Open(DSN)

	rs = win32com.client.Dispatch(r'ADODB.Recordset')
	strsql = "select * from Produtos"
	rs.Open(strsql, conn, 1, 3)
	t = rs.GetRows()
	conn.Close()
	return t
'''
def odbc():
	'''
  connects with odbc
  '''        
	constr = 'Driver={Microsoft Access Driver (*.mdb, *.accdb)};Dbq=' + db
	conn = pyodbc.connect(constr, autocommit=True)
	cur = conn.cursor()
	strsql = "select * from Produtos"
	cur.execute(strsql)
	t = list(cur)
	conn.close()
	return t

if __name__ == '__main__':
	db = 'c:\pdv\plu.mdb'
#	data1 = ado()