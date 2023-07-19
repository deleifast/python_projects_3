import datetime
mtime = datetime.datetime.fromtimestamp(fname.stat().st_mtime, tz=datetime.timezone.utc)
print(mtime)
datetime.datetime(2018, 10, 17, 10, 49, 0, 249980)
