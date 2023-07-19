#!/usr/bin/env python
# -*- coding: latin-1 -*-
# Desenvolvimento Aberto
# ScrolledText.py
 
# importa modulo 
 
from tkinter import *
 
from tkinter.scrolledtext import ScrolledText
 
 
# Cria formulario
formulario = Tk()
formulario.title = "Desenvolvimento Aberto"
 
# Evento do Botão
def clique():
    area.insert(END, texto.get() + "\n")
 
# Declara Variaveis
conteudo = "Escreva um texto dentro da caixa de texto. \n" + \
           "Voce tambem pode adicionar novas linhas nesta caixa " + \
           "escrevendo no editor e clicando no botao\n";
 
# Declara Componentes
rotulo = Label(formulario, text="Insira um texto na caixa de texto:")
 
area = ScrolledText(formulario, height =10, width = 40)
 
texto = Entry(formulario)
 
botao = Button(formulario, text="Ok", command=clique)
 
# Define propriedades para os componentes
area["font"] = ("Consolas",14)
area.insert(END,conteudo)
 
# Posiciona componentes na tela
rotulo.pack(padx=10)
area.pack(padx=10, fill=BOTH)
texto.pack(fill =X, padx=10, pady=10)
botao.pack(padx=10)
 
#loop do tcl
mainloop()