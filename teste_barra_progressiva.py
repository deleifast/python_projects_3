import tkinter as tk
from tkinter import ttk
import os, time, subprocess
from tkinter import messagebox
from tkinter import *

gui = tk.Tk()
gui.title("PDVCORAL_REMARCA - NAGUMO **(LOJA 01)**")
gui.geometry("600x100")
gui.resizable(0,0)


style = ttk.Style(gui)
# add label in the layout
style.layout('text.Horizontal.TProgressbar', 
             [('Horizontal.Progressbar.trough',
               {'children': [('Horizontal.Progressbar.pbar',
                              {'side': 'left', 'sticky': 'ns'})],
                'sticky': 'nswe'}), 
              ('Horizontal.Progressbar.label', {'sticky': ''})])
# set initial text
style.configure('text.Horizontal.TProgressbar', text='0 %')
# create progressbar
variable = tk.DoubleVar(gui)
pbar = ttk.Progressbar(gui, style='text.Horizontal.TProgressbar', length = 600, variable=variable)
pbar.place(x=1, y=40)



def increment():
    pbar.step()  # increment progressbar 
    style.configure('text.Horizontal.TProgressbar', 
                    text='{:g} %'.format(variable.get()))  # update label

    gui.after(100, increment)

pbar.stop()



label = Label(gui)
label.pack()

mensagem= StringVar()
lbl = Label(gui, text="Aguarde iniciando processos...." , fg="red", font="Arial 15")
lbl.place(x=1, y=2)

increment()



gui.mainloop()