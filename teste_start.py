import os

os.system("start retag.exe")
kill=input("Do you want to kill all running notepad ? (Y/y)")
kill = kill.lower()
if kill == 'y':
  print ("Now I'm killing all running notepads")
  result=os.system("taskkill /im retag.exe /f")
  # process result
  if result == 0:
    print ("All nodepads should be death now...")
  else:
    print ("Error executing taskkill command !!!")
else:
  print ("I let them running. Kill them self if you want !")