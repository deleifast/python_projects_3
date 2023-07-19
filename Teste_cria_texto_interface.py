import tkinter
from tkinter import *

def criarPL ():
		global nome_pl
def salvar():
	arq = open("{0}.txt".format(nome_pl.get()), "w")
	arq.close()

janela2 = Tk()
janela2.title("Criar Playlist")

bt_salvar =Button(janela2, width=20, text="SALVAR", command=salvar)

nome_pl = Entry(janela2)
nome_pl.insert(END, "NOME DA PLAYLIST")
nome_pl.pack()

nome_pl.place  (x=170, y=2)
bt_salvar.place(x=2, y=2)

janela2.geometry("400x27+250+250")

janela2.mainloop()