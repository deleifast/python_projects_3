import tkinter as tk

root = tk.Tk()

def print_selection(event):
    for key in listbox.selection_get().split():
        print(extras[key])

extras = {
    'object1': 1,
    'object2': 2,
    }

listbox = tk.Listbox(root, selectmode='multiple')
for key in extras:
    listbox.insert('end', key)
listbox.grid(row=0, column=0)
listbox.bind('<Key-Return>', print_selection)
tk.mainloop()