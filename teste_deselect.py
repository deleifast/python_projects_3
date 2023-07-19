import tkinter as tk

# --- functions ---

def subwindow():
    # you don't need `global` 
    # because you will not assign value
    #global var_option1
    #global var_option2

    window = tk.Toplevel(master)

    if var_option1.get(): # you need get()
        tk.Label(window, text="Option 1").pack()

    if var_option2.get(): # you need get()
        tk.Label(window, text="Option 2").pack()

    submit = tk.Button(window, text="Submit", command=window.destroy)
    submit.pack()

# --- main ---

master = tk.Tk()

# it creates global variable so you don't need `global`
# It has to be after tk.Tk()
var_option1 = tk.BooleanVar(value=False)
# or 
var_option2 = tk.BooleanVar()
var_option2.set(False)  # you need set()


lbl_title  = tk.Label(master, text="TICK BUTTONS")
cb_option1 = tk.Checkbutton(master, text="Option1", variable=var_option1)
cb_option2 = tk.Checkbutton(master, text="Option2", variable=var_option2)
btn_submit = tk.Button(master, text="Submit", command=subwindow)

lbl_title.pack()
cb_option1.pack()
cb_option2.pack()
btn_submit.pack()

master.mainloop()