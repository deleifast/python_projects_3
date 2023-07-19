#encoding: iso-8859-1
import time
import logging
import sys
import subprocess
import os
import os.path
import tkinter
from tkinter import messagebox

from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler

# hide main window
root = tkinter.Tk()
root.withdraw()

# initialize
driveLetter = 'Q:' 
networkPath = '\\\\192.168.141.150\C$' 
user = 'compartilhar' 
password = 'ruaf305'

# Connect to map network drive to letter Q
winCMD = 'NET USE ' + driveLetter + ' ' + networkPath + ' /User:' + user + ' ' + password
retorno = subprocess.call(winCMD, shell=True)

if retorno == 0:
	class Event(LoggingEventHandler):
		def on_modified(self, event):
			print("***DIGITE CRTL-C PARA SAIR***")

	if __name__ == "__main__":
		logging.basicConfig(level=logging.INFO,
			                format='%(asctime)s - %(message)s',
				            datefmt='%d-%m-%Y %H:%M:%S') 
		path = sys.argv[1] if len(sys.argv) > 1 else 'Q:\\PDV'
		event_handler = Event()
		observer = Observer()
		observer.schedule(event_handler, path, recursive=True)
		observer.start()
		try:
			while True:
				time.sleep(1)
		except KeyboardInterrupt:
			observer.stop()
			winCMD = 'NET USE ' + driveLetter + ' /delete /yes'
			subprocess.call(winCMD, shell=True)

		observer.join()

else:
	resp = messagebox.showerror("Erro", "SEM CONEXÃO COM A LOJA, VERIFICAR!")	
