#encoding: iso-8859-1

from tkinter import *

gui = Tk() #makes a blank popup, under the variable name 'root'

topFrame = Frame(gui)
topFrame.pack(anchor = S)
bottomFrame = Frame(gui)
bottomFrame.pack(side=BOTTOM, anchor = W)

gui.title("PDVCORAL_REMARCA - NAGUMO **(LOJA 14)**")
gui.geometry("800x250")
gui.resizable(0,0)

def sel():
   selection = "CLICOU OPÇÃO: " + str(var.get()) + " DO MENU!!!"
   label.config(text = selection, bg="red", fg="yellow", font="Terminal 12")

var= IntVar()

R1 = Radiobutton(gui, text="1 - Reiniciar CAIXA", variable=var, value=1, font="Arial 10", command=sel)
R1.pack( anchor = NW )

R2 = Radiobutton(gui, text="2 - Reiniciar WINDOWS", variable=var, value=2, font="Arial 10", command=sel)
R2.pack( anchor = NW )

mensagem= StringVar()
lbl = Label(gui, text="ATENÇÃO : Caixas 05 e 06 NÃO FUCIONAM, USAM WINDOWS XP" , bg="yellow", fg="black", font="Arial 16")
lbl.pack(fill=X)

label = Label(gui)
label.pack()

res = " "

lblaguarde = Label(gui, text= res, font="Arial 20", fg= "red")
lblaguarde.place(x=300, y=110)

def Aguarde(event):
	res = "Aguarde..."
	res_texto(res)
	
def res_texto(res):
    lblaguarde.config(text=res)


button1 = Button(bottomFrame, text='Button 1', fg='red')
button2 = Button(bottomFrame, text='Button 2', fg='blue')
button3 = Button(bottomFrame, text='Button 3', fg='green')
button4 = Button(bottomFrame, text='Button 4', fg='pink')
btn1 = Button(topFrame, text="Caixa 1", bg="white", fg="black")
#btn.pack(side=LEFT, anchor=W, expand=0)
btn1.bind('<Button-1>')
btn2 = Button(topFrame, text="Caixa 2", bg="white", fg="black")
#btn.pack(side=LEFT, anchor=W, fill=X, expand=0)
btn2.bind('<Button-1>')
btn3 = Button(topFrame, text="Caixa 3", bg="white", fg="black")
#btn.pack(side=LEFT, anchor=W, expand=0)
btn3.bind('<Button-1>')



button1.grid(column=0, row = 1)
button2.grid(column=0, row = 2)
button3.grid(column=1, row = 2)
button4.grid(column=1, row = 1)

btn1.grid(column=2, row = 2)
btn2.grid(column=3, row = 2)
btn3.grid(column=4, row = 2)

gui.mainloop()