from tkinter import* 
janela =Tk()#criamos a janela
E = Text(janela)#criamos o widget Text.
x=open("relimp_loja01.txt","r") #função de abertura para ler
z = x.read() #função ler, read
E.insert(0.0,z)#aqui inserimos o texto dentro do widget Text.
E.pack()#empacotanos o widget Text
janela.mainloop()#fazemos o loop da janela. 
