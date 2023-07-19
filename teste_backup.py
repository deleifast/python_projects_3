import os
import time
import glob
import zipfile

# The files and directories to backup
source = [r'c:\pdv\xmlsat']
# If you are using Windows, use source = [r'C:\Documents', r'D:\Work']

# The directory where to store the backup
target_dir = 'c:\\pdv\\bkpxml'

# The date - the subdirectory in the main backup directory
today = target_dir + time.strftime('%Y%m%d')
# The time - the name of the zip archive
now = time.strftime('%H%M%S')

# Create the subdirectory if it doesn't exist
if not os.path.exists(today):
        os.mkdir(today)  # make directory
        print ('Successfully created directory'), today

# The name of the zip file
target = today + os.sep + now + '.zip'

# The zip command to run
#zip_command = exec("zip -qr {0} {1}".format(target, ' '.join(source)))

# open the zip file for writing, and write stuff to it

file = zipfile.ZipFile("test.zip", "w")

for name in glob.glob("c:\\pdv\\xmlsat\*"):
    file.write(name, os.path.basename(name), zipfile.ZIP_DEFLATED)

file.close()

# Run the backup
#if os.system() == 0:
#        print ('Successful backup to'), target
#else:
#        print ('Backup FAILED')