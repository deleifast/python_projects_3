#encoding: iso-8859-1
from tkinter import Tk, Label, Button

class Exemplo:
    def __init__(self, aplicacao):

        # Remove as bordas/decoração
        aplicacao.overrideredirect(True)

        #Cor de fundo como no exemplo da outra resposta
        root["bg"] = "gray"

        self.label = Label(aplicacao, text="Primeira janela")
        self.label.pack()

        self.greet_button = Button(aplicacao, text="Chamar função", command=self.minhafuncao)
        self.greet_button.pack()

        self.close_button = Button(aplicacao, text="Fechar", command=aplicacao.quit)
        self.close_button.pack()

    def minhafuncao(self):
        print("Testando!")

root = Tk()
minhajanela = Exemplo(root)
root.mainloop()