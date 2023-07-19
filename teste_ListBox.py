from tkinter import *

root = Tk()

mylist = ('c:\pdv\lista.txt')

var = StringVar(value=mylist)
box = Listbox(master=root, listvariable=var)
box.pack(fill=BOTH, expand=True)

#mylist.append('four')
#mylist.remove('two')
mylist.insert(END, mylist)

var.set(mylist)

root.mainloop()