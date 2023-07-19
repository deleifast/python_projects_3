def make_4gb_file(f):
	f = open(f, "w")
	f.seek ( 4 * 1024 * 1024 * 1024 - 1)
	f.write("\0")
	f.close()

import zipfile
z = zipfile.ZipFile("c://pdv/xml/xml.zip", "w", zipfile.ZIP_DEFLATED)
make_4gb_file("c://pdv/xml")
z.write("c://pdv/xml")
z.close()