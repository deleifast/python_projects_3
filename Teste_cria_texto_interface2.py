# -*- coding: utf-8 -*-
#
#  exFileDialogs.py
#
#  Copyright 2017 tavares <tavares@tavares-Inspiron-5558>
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#
#
import tkinter as tk
import tkinter.filedialog as fdlg
#encoding: iso-8859-1
import tkinter.scrolledtext as tkst
from tkinter.constants import END,HORIZONTAL, VERTICAL, NW, N, E, W, S, SUNKEN, LEFT, RIGHT, TOP, BOTH, YES, NE, X, RAISED, SUNKEN, DISABLED, NORMAL, CENTER

class TesteDialogs(object):
	appname= "Demonstrador"
	frameWidth      = 1200
	frameHeight     = 600
	padx            = 5
	pady            = 5


	def __init__(self, **kw):

		self.root = tk.Tk()

		self.root.title(self.appname)

		self.root.geometry('%dx%d' % (self.frameWidth, self.frameHeight))

		self.createMenuBar()

		self.minhaTela = tk.Frame(self.root)
		self.minhaTela.pack( padx= "5", pady="5",expand=1, fill="both")

		#self.editor = tkst.ScrolledText(master = self.minhaTela,wrap= tk.WORD,width  = 20,height = 10)
		#self.editor.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
		#self.editor.insert(tk.INSERT, "Esta e uma linha no editor")



	def createMenuBar(self):

		menubar = tk.Menu(self.root)

		filemenu = tk.Menu(menubar, tearoff=0)
		filemenu.add_command(label="Sair", command=self.root.quit)
		menubar.add_cascade(label="Arquivo", menu=filemenu)

		showFileDialogsmenu = tk.Menu(menubar, tearoff=0)
		showFileDialogsmenu.add_command(label="Configurar PRINI", command = self.programaINI)
		showFileDialogsmenu.add_command(label="askopenfilename", command=self.testeOpenFileName)
		showFileDialogsmenu.add_command(label="asksaveasfile", command=self.testeAsksaveasfile)
		showFileDialogsmenu.add_command(label="asksaveasfilename", command=self.testeasksaveasfilename)
		showFileDialogsmenu.add_command(label="askdirectory", command=self. testeaskdirectory)

		menubar.add_cascade(label="DialogosArquivos", menu= showFileDialogsmenu)


		self.root.config(menu=menubar)

	def programaINI(self):
		opcoes = {}
		mensagem= StringVar()
		lbl = Label(gui, text="Remarca - telefone: (11)2755-7911 " , fg="red", font="Arial 15")
		lbl.place(x=140, y=225)
	
	
	
	
	
	
	def testeOpenFile(self):
		#primeiro definimos as op��es

		opcoes = {}                 # as op��es s�o definidas em um dicion�rio
		opcoes['defaultextension'] = '.txt'
		opcoes['filetypes'] = [('Todos arquivos', '.*'), ('arquivos texto', '.txt')]
		opcoes['initialdir'] = ''    # ser� o diret�rio atual
		opcoes['initialfile'] = '' #apresenta todos os arquivos no diretorio
		opcoes['parent'] = self.root
		opcoes['title'] = 'Dialogo que retorna um objeto arquivo'

		#retorna um arquivo aberto no modo leitura

		arquivo= fdlg.askopenfile(mode='r', **opcoes)

		if(arquivo):
			print("Fechamos o arquivo")
			arquivo.close()    # n�o iremos fazer nada agora com o arquivo. fechamos
	

	def testeOpenFileName(self):
		#primeiro definimos as op��es

		opcoes = {}                 # as op��es s�o definidas em um dicion�rio
		opcoes['defaultextension'] = '.txt'
		opcoes['filetypes'] = [('Todos arquivos', '.*'), ('arquivos texto', '.txt')]
		opcoes['initialdir'] = ''    # ser� o diret�rio atual
		opcoes['initialfile'] = '' #apresenta todos os arquivos no diretorio
		opcoes['parent'] = self.root
		opcoes['title'] = 'Dialogo que retorna o nome de um arquivo para ser aberto'

		#retorna o NOME de um arquivo

		nomeArquivo= fdlg.askopenfilename(**opcoes)

		if(nomeArquivo):

			arquivo= open(nomeArquivo,'r')
			print("Fechamos o arquivo")
			arquivo.close()    # n�o iremos fazer nada agora com o arquivo. fechamos


	def testeAsksaveasfile(self):
		#primeiro definimos as op��es

		opcoes = {}                 # as op��es s�o definidas em um dicion�rio
		opcoes['defaultextension'] = '.txt'
		opcoes['filetypes'] = [('Todos arquivos', '.*'), ('arquivos texto', '.txt')]
		opcoes['initialdir'] = ''    # ser� o diret�rio atual
		opcoes['initialfile'] = '' #apresenta todos os arquivos no diretorio
		opcoes['parent'] = self.root
		opcoes['title'] = 'Dialogo que salva  um objeto arquivo'

		#retorna um arquivo aberto no modo escrita

		arquivo= fdlg.asksaveasfile(mode='w', **opcoes)

		if(arquivo):
			print("Fechamos o arquivo")
			arquivo.close()    # n�o iremos fazer nada agora com o arquivo. fechamos



	def testeasksaveasfilename(self):
		#primeiro definimos as op��es

		opcoes = {}                 # as op��es s�o definidas em um dicion�rio
		opcoes['defaultextension'] = '.txt'
		opcoes['filetypes'] = [('Todos arquivos', '.*'), ('arquivos texto', '.txt')]
		opcoes['initialdir'] = ''    # ser� o diret�rio atual
		opcoes['initialfile'] = '' #apresenta todos os arquivos no diretorio
		opcoes['parent'] = self.root
		opcoes['title'] = 'Dialogo que retorna o nome de um arquivo para ser salvo'

		#retorna o NOME de um arquivo

		nomeArquivo= fdlg.asksaveasfilename(**opcoes)

		if(nomeArquivo):

			arquivo= open(nomeArquivo,'r')
			print("Fechamos o arquivo")
			arquivo.close()    # n�o iremos fazer nada agora com o arquivo. fechamos


	def testeaskdirectory(self):
		#primeiro definimos as op��es

		opcoes = {}                 # as op��es s�o definidas em um dicion�rio
		#opcoes['defaultextension'] = '.txt'
		#opcoes['filetypes'] = [('Todos arquivos', '.*'), ('arquivos texto', '.txt')]
		opcoes['initialdir'] = ''    # ser� o diret�rio atual
		#opcoes['initialfile'] = '' #apresenta todos os arquivos no diretorio
		opcoes['parent'] = self.root
		opcoes['title'] = 'Dialogo que retorna o nome do diretorio selecionado'

		#retorna o caminho completo  de um diret�rio

		nomeDiretorio= fdlg.askdirectory(**opcoes)

		print (nomeDiretorio)



	def execute(self):
		self.root.mainloop()



def main(args):

	appProc=  TesteDialogs()
	appProc.execute()
	return 0

if __name__ == '__main__':
	import sys
	sys.exit(main(sys.argv))