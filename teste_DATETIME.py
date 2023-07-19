import os,time
import datetime
import shutil

import datetime as dt

now = dt.datetime.now()
ago = now-dt.timedelta(hours=24)
strftime = "%H:%M %m/%d/%Y"
created = 'c:\\pdv\xmlsat\000002664'
dest = 'c:\\pdv\xmlsat\teste'

for root, dirs,files in os.walk(created):  
    for fname in files:
        path = os.path.join(root, fname)
        st = os.stat(path)    
        mtime = dt.datetime.fromtimestamp(st.st_mtime)
        if mtime > ago:
            print("True:  ", fname, " at ", mtime.strftime("%H:%M %m/%d/%Y"))
            shutil.move(path, dest)
            # this is actual move