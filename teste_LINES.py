from tkinter import *
from tkinter.ttk import *

root = Tk()

tree = Treeview(root)

tree["columns"]=("one","two")
tree.column("one", width=100 )
tree.column("two", width=100)
tree.heading("one", text="coulmn A")
tree.heading("two", text="column B")

tree.insert("" , 0,    text="Line 1", values=("1A","1b"))

id2 = tree.insert("", 1, "dir2", text="Dir 2")
tree.insert(id2, "end", "dir 2", text="sub dir 2", values=("2A","2B"))

##alternatively:
tree.insert("", 3, "dir3", text="Dir 3")
tree.insert("dir3", 3, text=" sub dir 3",values=("3A"," 3B"))

tree.insert("", 4, "Caixa 14", text="Caixa 14")
tree.insert("Caixa 14", 4, text=" teste",values=("3A"," 3B"))

tree.pack()
root.mainloop()