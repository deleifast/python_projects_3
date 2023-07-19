from tkinter import *
from subprocess import *

def func():
    proc = Popen("psexec.exe -d -i -u pdv\PDV -p pdv \\\\192.168.141.11 ""c:\\pdv\deleta_clisitef.bat", stdout=PIPE, stderr=PIPE, shell=True)
    proc = proc.communicate()
    output.insert(END, proc)

Master = Tk()
Check = Button(Master, text="Executar", command=func)
Quit = Button(Master, text="Sair", fg="red", command=Master.quit)
output = Text(Master, width=100, height=40)

Check.pack(padx=20, pady=8)
Quit.pack(padx=20, pady=18)
output.pack()

Master.mainloop()