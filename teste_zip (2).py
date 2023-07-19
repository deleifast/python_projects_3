import os
import zipfile
 
pdv_zip = zipfile.ZipFile('C:\\pdv\\atual\\pdv.zip', 'w')
 
for files in os.walk('C:\\pdv\\atual\pdv'):
 
    for file in files:
        if file.startswith('PDV'):
            pdv_zip.write(os.path.join(folder, file), os.path.relpath(os.path.join(folder,file), 'C:\\pdv\\atual'), compress_type = zipfile.ZIP_DEFLATED)
 
pdv_zip.close()