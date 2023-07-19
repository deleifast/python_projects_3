#encoding: iso-8859-1
import sys
import time
import subprocess
import os
import os.path
import logging
import tkinter
from tkinter import messagebox
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# hide main window
root = tkinter.Tk()
root.withdraw()

# initialize
driveLetter = 'Q:' 
networkPath = '\\\\192.168.1.101\C$' 
user = 'compartilhar' 
password = 'ruaf305'

# Connect to map network drive to letter Q
winCMD = 'NET USE ' + driveLetter + ' ' + networkPath + ' /User:' + user + ' ' + password
retorno = subprocess.call(winCMD, shell=True)

if retorno == 0:
	
	os.chdir('Q:\\')

	class MyHandler(FileSystemEventHandler):
		def on_any_event(self, event):
			print ('Evento', event.event_type,' caminho:', event.src_path)

	path = 'Q:\\MATRIZ'
	logging.basicConfig(level=logging.INFO,
						format='%(asctime)s - %(message)s',
						datefmt='%Y-%m-%d %H:%M:%S')
	observer = Observer()
	observer.schedule(MyHandler(), path, recursive=True)
	observer.start()

	try:
		while True:
			time.sleep(1)
	except KeyboardInterrupt:
		observer.stop()
	observer.join()

	winCMD = 'NET USE ' + driveLetter + ' /delete /yes'
	subprocess.call(winCMD, shell=True)

else:
	resp = messagebox.showerror("Erro", "SEM CONEXÃO COM A LOJA, VERIFICAR!")	
	
 
