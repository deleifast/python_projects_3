# Import the required library
from tkinter import *
from tkinter import ttk

import socket, threading, pickle, time

# Create an instance of tkinter frame
win=Tk()

# Set the geometry
win.geometry("700x350")

# Add a text widget
text=Text(win, width=80, height=15)
text.pack()

# Create a Label widget
label=Label(win, text="", font=('Calibri 15'))
label.pack()



win.mainloop()

