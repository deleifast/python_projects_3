import tkinter as tk
from tkinter import scrolledtext

win = tk.Tk()
def add_to_frame(i):
    if i<10000:
        text_area.insert(tk.END, "step " + str(i) + "\n")
        text_area.see(tk.END)
        win.after(1,add_to_frame,i+1)
text_area = scrolledtext.ScrolledText(win)


text_area.see(tk.END)
text_area.pack()
i=0
win.after(1,add_to_frame,i)

win.mainloop()
