import numpy as np
data, abertura, maxima, minima, fechamento = np.loadtxt('relatorio.csv',
														delimiter = ',',
														unpack = True,
														dtype = 'str')

y = data[0]
print (y)