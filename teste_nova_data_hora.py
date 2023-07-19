import urllib3
import os

zone_offset = -2

path = "http://www.timeapi.org/utc/"

if zone_offset < 0:
    path += "%i+hours+ago?\d-\m-\Y+\H:\M:\S" % -zone_offset
elif zone_offset > 0:
    path += "in+%i+hours?\d-\m-\Y+\H:\M:\S" % zone_offset
else:
    path += "?\d-\m-\Y+\H:\M:\S"

path = path.replace("+", "%20")

stream = urllib3.request.urlopen(path)
all = stream.read()
stream.close()

date, time = all.split()

os.system("date %s" % date)
os.system("time %s" % time)

