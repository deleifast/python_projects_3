#encoding: iso-8859-1


from tkinter import *

# Guarda as configura��es padr�o para os
# bot�es que ser�o definidos mais tarde
button_default_config = {
    "font": "Arial 10 normal",
    "bg": "gray",
    "fg": "white"
}


class Window(Frame):
    """ Janela principal """

    def __init__(self):
        """ M�todo construtor da janela"""
        super().__init__(master=None)  # Aqui iniciamos a nossa superclasse (Frame)

        # Defini��es de titulos, largura
        # e altura da janela principal
        self.master.geometry("800x600")
        self.master.title("MainWindow")

        # Para os bot�es, definimos o texto e depois passamos o
        # dicionario de atributos usando "**" para o bot�o
        button1 = Button(self, text="Button1", **button_default_config)

        # Coloque cada bot�o em seu lugar e defina o
        # preenchimento dele usando o NSEW que significa
        # que o bot�o ir� se ajustar ao tamanho dos items
        # ao seu redor e dentro da sua pr�pria celula.
        button1.grid(row=0, column=0, pady=40, sticky=NSEW)

        # Ao criar outro bot�o devemos fazer da mesma forma
        # para que fique tudo igual, passaremos o mesmo
        # dicion�rio de attributos que passamos ao primeiro
        button2 = Button(self, text="Button2", **button_default_config)

        # Definimos outra fonte ao 2� bot�o, pois
        # as celulas ir�o se ajustar automaticamente
        button2.configure(font="Arial 20 normal")

        # Configurando novamente o grid
        button2.grid(row=0, column=1, pady=40, sticky=NSEW)

        # Essa � a parte mais importante, pois, define o
        # esticamento de cada celula do grid. Se possivel
        # comente as 2 linhas abaixo e teste para entender melhor
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)

        # Epacotamos o frame na janela
        self.pack(fill=BOTH, expand=True)


if __name__ == '__main__':
    window = Window()
    window.mainloop()