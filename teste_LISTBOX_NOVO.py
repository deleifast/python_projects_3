from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import glob

def browse(*args):
    directory.set(filedialog.askdirectory())
    return

def parse(*args):
    all_files = None
    all_files = glob.glob( directory.get() + "/*.py")

def main_menu():    
    root = Tk()
    root.title("Parse Files")
    mainframe = ttk.Frame(root, padding="3 3 12 12")
    mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
    mainframe.columnconfigure(0, weight=1)
    mainframe.rowconfigure(0, weight=1)
    global directory
    directory = StringVar()

    ttk.Label(mainframe, text="Directory of Files: ").grid(column=1, row=1, sticky=E)
    dir_entry = ttk.Entry(mainframe, width=30, textvariable=directory)
    dir_entry.grid(column=2, row=1, sticky=(W, E))
    ttk.Button(mainframe, text="Browse", command=browse).grid(column=3, row=1, sticky=(W,E))
    ttk.Button(mainframe, text="Parse", command=parse).grid(column=3, row=3, sticky=W)

    for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

    dir_entry.focus()
    root.bind('<Return>', parse)
    root.mainloop()