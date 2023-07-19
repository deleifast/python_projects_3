#encoding: iso-8859-1

import tkinter
 
class megaSenaApp_tk(tkinter.Tk):
# tkinter.tk � a classe base para a janela padr�o. A nossa classe megaSenaApp_tk ir� herdar todas as funcionalidades da classe padr�o.
 
    def __init__(self,parent):
        tkinter.Tk.__init__(self,parent)
        # no construtor da nossa classe, apenas chamamo o construtor da classe pai, tkinter.Tk.__init__()).
        self.parent = parent
        # geralmente necessitaremos  de acessar o pai de um objeto. � uma boa t�cnica  sempre salvar uma referencia ao pai.
        self.initialize()
        #no m�todo initialize criamos os demais objetos que ser�o apresentados na tela, inicializamos as vari�veis globais (irc..),
                   #inicializamos o hardware caso necess�rio, etc..
         
         
    def initialize(self):   
        self.grid()     #vamos dispor os objetos na tela dentro de uma grade         
        self.lblPalpite1= tkinter.Label(self, text="00")     #este objeto ir� apresentar o primeiro n�mero
        self.lblPalpite1.grid(column=0, row=0)               #nesta posi��o
         
        self.lblPalpite2= tkinter.Label(self, text="01")     #este objeto ir� apresentar o segundo  n�mero
        self.lblPalpite2.grid(column=1, row=0)               #nesta posi��o    
 
        self.lblPalpite3= tkinter.Label(self, text="02")     #este objeto ir� apresentar o terceiro n�mero
        self.lblPalpite3.grid(column=2, row=0)               #nesta posi��o    
 
        self.lblPalpite4= tkinter.Label(self, text="03")     #este objeto ir� apresentar o quarto  n�mero
        self.lblPalpite4.grid(column=4, row=0)               #nesta posi��o    
 
        self.lblPalpite5= tkinter.Label(self, text="04")     #este objeto ir� apresentar o quinto  n�mero
        self.lblPalpite5.grid(column=5, row=0)               #nesta posi��o    
 
        self.lblPalpite6= tkinter.Label(self, text="05")     #este objeto ir� apresentar o sexto  n�mero
        self.lblPalpite6.grid(column=6, row=0)               #nesta posi��o    
 
        self.btnGeraPalpite = tkinter.Button(self,text=u"Estou com sorte!")  #criamos o objeto bot�o
        self.btnGeraPalpite.grid(column=3,row=1)                   # e o colocamos na posi��o coluna 3, linha 1
 
 
 
#este � ponto onde o programa se inicia
#se foi chamado a partir do interpretador python, o _name_  automaticamente ser� "__main__"
if __name__ == "__main__":
    app = megaSenaApp_tk(None)      #criamos uma aplica��o sem nenhum pai, pois � a principal.
    app.title('Minha Mega-Sena')    #especificamos o t�tulo de nossa aplica��o
    app.mainloop()                  #o programa entra no loop de espera de eventos (pressionar de menus, bot�es, etc..)