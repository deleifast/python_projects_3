
try: import tkinter
except ImportError:
    import Tkinter as tkinter
    import ttk
else: from tkinter import ttk
from tkinter import *


root = tkinter.Tk()
frame = tkinter.Frame(root)
frame.grid()
s = ttk.Style()
s.theme_use('clam')
s.configure("red.Horizontal.TProgressbar", foreground='red', background='red')
ttk.Progressbar(frame, style="red.Horizontal.TProgressbar", orient="horizontal", length=600,mode="determinate", maximum=4, value=1).grid(row=1, column=1)
frame.pack()
tkinter.mainloop()