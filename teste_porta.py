#encoding: iso-8859-1
import ntplib
import datetime, time
import socket
import tkinter as tk
from tkinter import *

gui = tk.Tk()

gui.geometry('410x100')
gui.title('Pdvcoral - Remarca')
gui.resizable(0,0)

msg = Label(gui, text='Sincronizado relógio do Pdv:', fg="red", font='Arial 18')
msg.place(x=1, y=1)

res = StringVar()

lblres = Label(gui, text= res, font="Arial 20", fg= "black")
lblres.place(x=60, y=50)

def res_texto(res):
    lblres.config(text=res)


try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print ("Socket successfully created")
except socket.error as err:
    print ("socket creation failed with error %s" %(err))

# default port for socket
port = 80

try:
    host_ip = socket.gethostbyname('www.google.com')
except socket.gaierror:
    # this means could not resolve the host
    print ("there was an error resolving the host")
    sys.exit()

# connecting to the server
s.connect((host_ip,port))

print ("the socket has successfully connected to google \
on port == %s" %(host_ip))

c = ntplib.NTPClient()
response = c.request('1.br.pool.ntp.org', version=3)
dt_ = datetime.datetime.fromtimestamp( response.tx_time )
res = dt_.strftime('%d-%m-%Y - %H:%M:%S')
res_texto(res)


def sair():
	gui.destroy()
	return

gui.after(3000, sair)

gui.mainloop()