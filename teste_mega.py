#encoding: iso-8859-1

import tkinter
 
class megaSenaApp_tk(tkinter.Tk):
# tkinter.tk é a classe base para a janela padrão. A nossa classe megaSenaApp_tk irá herdar todas as funcionalidades da classe padrão.
 
    def __init__(self,parent):
        tkinter.Tk.__init__(self,parent)
        # no construtor da nossa classe, apenas chamamo o construtor da classe pai, tkinter.Tk.__init__()).
        self.parent = parent
        # geralmente necessitaremos  de acessar o pai de um objeto. É uma boa técnica  sempre salvar uma referencia ao pai.
        self.initialize()
        #no método initialize criamos os demais objetos que serão apresentados na tela, inicializamos as variáveis globais (irc..),
                   #inicializamos o hardware caso necessário, etc..
         
         
    def initialize(self):   
        self.grid()     #vamos dispor os objetos na tela dentro de uma grade         
        self.lblPalpite1= tkinter.Label(self, text="00")     #este objeto irá apresentar o primeiro número
        self.lblPalpite1.grid(column=0, row=0)               #nesta posição
         
        self.lblPalpite2= tkinter.Label(self, text="01")     #este objeto irá apresentar o segundo  número
        self.lblPalpite2.grid(column=1, row=0)               #nesta posição    
 
        self.lblPalpite3= tkinter.Label(self, text="02")     #este objeto irá apresentar o terceiro número
        self.lblPalpite3.grid(column=2, row=0)               #nesta posição    
 
        self.lblPalpite4= tkinter.Label(self, text="03")     #este objeto irá apresentar o quarto  número
        self.lblPalpite4.grid(column=4, row=0)               #nesta posição    
 
        self.lblPalpite5= tkinter.Label(self, text="04")     #este objeto irá apresentar o quinto  número
        self.lblPalpite5.grid(column=5, row=0)               #nesta posição    
 
        self.lblPalpite6= tkinter.Label(self, text="05")     #este objeto irá apresentar o sexto  número
        self.lblPalpite6.grid(column=6, row=0)               #nesta posição    
 
        self.btnGeraPalpite = tkinter.Button(self,text=u"Estou com sorte!")  #criamos o objeto botão
        self.btnGeraPalpite.grid(column=3,row=1)                   # e o colocamos na posição coluna 3, linha 1
 
 
 
#este é ponto onde o programa se inicia
#se foi chamado a partir do interpretador python, o _name_  automaticamente será "__main__"
if __name__ == "__main__":
    app = megaSenaApp_tk(None)      #criamos uma aplicação sem nenhum pai, pois é a principal.
    app.title('Minha Mega-Sena')    #especificamos o título de nossa aplicação
    app.mainloop()                  #o programa entra no loop de espera de eventos (pressionar de menus, botões, etc..)