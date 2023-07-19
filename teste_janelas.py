import os, time, subprocess, logging
from tkinter import * 
from tkinter.ttk import *
master = Tk() 
master.geometry("200x200") 

  
def openNewWindow(): 
	     
       
    newWindow = Toplevel(master) 
     
    
    newWindow.title("Escolha o motivo:") 
      
    newWindow.geometry("400x200")
    
    R1 = Radiobutton(newWindow, text="Teste", command = execute)
    R1.pack(anchor = NW)
    
def execute():
	subprocess.call("psexec.exe -d -i -u Nano -p pdv \\\\192.168.8.38 ""c:\\pdv\inicia_pdv.bat", shell=True)
  
label = Label(master,  
              text ="This is the main window") 
  
label.pack(pady = 10) 
btn = Button(master,  
             text ="Click to open a new window",  
             command = openNewWindow) 
btn.pack(pady = 10) 
mainloop() 
