#encoding: iso-8859-1


from tkinter import *

# Guarda as configurações padrão para os
# botões que serão definidos mais tarde
button_default_config = {
    "font": "Arial 10 normal",
    "bg": "gray",
    "fg": "white"
}


class Window(Frame):
    """ Janela principal """

    def __init__(self):
        """ Método construtor da janela"""
        super().__init__(master=None)  # Aqui iniciamos a nossa superclasse (Frame)

        # Definições de titulos, largura
        # e altura da janela principal
        self.master.geometry("800x600")
        self.master.title("MainWindow")

        # Para os botões, definimos o texto e depois passamos o
        # dicionario de atributos usando "**" para o botão
        button1 = Button(self, text="Button1", **button_default_config)

        # Coloque cada botão em seu lugar e defina o
        # preenchimento dele usando o NSEW que significa
        # que o botão irá se ajustar ao tamanho dos items
        # ao seu redor e dentro da sua própria celula.
        button1.grid(row=0, column=0, pady=40, sticky=NSEW)

        # Ao criar outro botão devemos fazer da mesma forma
        # para que fique tudo igual, passaremos o mesmo
        # dicionário de attributos que passamos ao primeiro
        button2 = Button(self, text="Button2", **button_default_config)

        # Definimos outra fonte ao 2° botão, pois
        # as celulas irão se ajustar automaticamente
        button2.configure(font="Arial 20 normal")

        # Configurando novamente o grid
        button2.grid(row=0, column=1, pady=40, sticky=NSEW)

        # Essa é a parte mais importante, pois, define o
        # esticamento de cada celula do grid. Se possivel
        # comente as 2 linhas abaixo e teste para entender melhor
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)

        # Epacotamos o frame na janela
        self.pack(fill=BOTH, expand=True)


if __name__ == '__main__':
    window = Window()
    window.mainloop()