from tkinter import *
from tkinter import filedialog


def Save():
    name = filedialog.asksaveasfile(mode='w', defaultextension=".txt")
    t = textField.get(0.0, END)  # Pega o texto do textField
    name.write(t.rstrip())  # Escreve o texto no arquivo criado

root = Tk()

menu = Menu(root)
root.config(menu=menu)

subMenu = Menu(menu, tearoff=0)
menu.add_cascade(label="File", menu=subMenu)
subMenu.add_command(label="Save", command=Save)

textField = Text(root)
textField.pack(side=LEFT, expand=True, fill='both')

scrollBar = Scrollbar(root)
scrollBar.pack(side=RIGHT, fill=Y)

scrollBar.config(command=textField.yview)
textField.config(yscrollcommand=scrollBar.set)

root.mainloop()