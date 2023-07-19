import ntplib
from time import ctime
c = ntplib.NTPClient()
response = c.request('200.20.186.75')
print (ctime(response.tx_time))
