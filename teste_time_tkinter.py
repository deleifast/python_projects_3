import tkinter as tk
import time

class showtime():
    def __init__(self, t=30):
        self.ticker=t
        self.count = 0
        self.root = tk.Tk()
        self.label = tk.Label(text="00:00:00")
        self.label.pack()
        self.update_label()
        self.root.mainloop()

    def update_label (self):
        if self.count>=self.ticker:
            self.root.destroy()
            return
        else:
            self.count+=1
            now = time.strftime("%H:%M:%S")
            self.label.configure(text=now)
            self.root.after(1000, self.update_label)

app = showtime(10)        
print ('script terminado')  