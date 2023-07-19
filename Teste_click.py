from tkinter import *

def foo():
    print ('foo')

root = Tk()

frame = Frame(root)
frame.pack()

button1 = Button(frame, text = 'Foo!')
button1.pack()
button1.bind('<Button-1>', foo)

root.mainloop()