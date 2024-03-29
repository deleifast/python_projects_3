import os, os.path
import tkinter as tk
import tkinter.ttk as ttk

os.chdir('C:\\REMARCA\cx15')


class AppBase:
    def __init__(self):
        self.mywin = tk.Tk()
        self.mywin.geometry("%dx%d+%d+%d" % (800, 600, 5, 5))
        self.frame1 = tk.Frame(self.mywin)
        self.frame1.pack()


        
		lb_header = ['name', 'surname']
   		with open("sat_cx15.txt") as cx15:
			f15 = cx15.read()

		lb_list = [
        (f15) ,
        ('Larry', 'Black') ,
        ('Walter', 'White') ,
        ('Fred', 'Becker') 
        ]

        self.tree = ttk.Treeview(columns=lb_header, show="headings")
        self.tree.grid(in_=self.frame1)

        for col in lb_header:
            self.tree.heading(col, text=col.title())
        for item in lb_list:
            self.tree.insert('', 'end', values=item)

    def start(self):
        self.mywin.mainloop()

app=AppBase()
app.start()