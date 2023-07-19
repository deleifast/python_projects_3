from tkinter import *




root = Tk()
root.geometry("400x400")

GENDERS = [
    ("Male", "M"),
    ("Female", "F"),
    ("Other", "O")
]

v = StringVar()
v.set("L")  # initialize

for text, gender in GENDERS:
    b = Radiobutton(root, text=text,
                    variable=v, value=gender)
    b.pack(anchor=W)

root.mainloop()