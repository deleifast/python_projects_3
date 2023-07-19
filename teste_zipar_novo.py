import zipfile
from datetime import datetime

myfile = open("bla.zip", "wb")
zip = zipfile.ZipFile(myfile, mode="w")
info = zipfile.ZipInfo()
info.filename="numbers.txt"
info.compress_type = zipfile.ZIP_DEFLATED
#info.external_attr = (0644 << 16)
info.date_time = datetime.now().timetuple()
zip.writestr(info, "1234567890" * 10000)
zip.close()
myfile.close()