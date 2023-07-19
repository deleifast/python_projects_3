#encoding: iso-8859-1

import tkinter as tk


def consulta():
    d = (Inventory_data.get ("Inventory_data")). get (entrada.get())
    # Resto del código

ventana = tk.Tk()
ventana.geometry("500x300+100+100")
ventana.title("MijaGato")

tk.Label(ventana, text="Name Of Tag").place(x=200, y=100)
entrada = tk.StringVar()
tk.Entry(ventana, textvariable=entrada, width=30).place(x=150, y=140)
tk.Button(ventana, text="Start",  command = consulta).place(x=220, y=180)
ventana.mainloop()