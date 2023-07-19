#encoding: iso-8859-1
#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  exCommonDialogs.py.py
#
#  Copyright 2017 tavares &lt;tavares@tavares-Inspiron-5558&gt;
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
import tkinter.scrolledtext as tkst
import tkinter.messagebox as tkmsg
 
class TesteDialogs(object):
    appname= "Demonstrador de diálogos no Tkinter"
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
 
        self.editor = tkst.ScrolledText(master = self.minhaTela,wrap= tk.WORD,width  = 20,height = 10)
        self.editor.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
 
    def createMenuBar(self):
 
        menubar = tk.Menu(self.root)
 
        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label="Sair", command=self.root.quit)
        menubar.add_cascade(label="Arquivo", menu=filemenu)
 
        showStdDialogsmenu = tk.Menu(menubar, tearoff=0)
        showStdDialogsmenu.add_command(label="askokcancel",command=self.testeaskokcancel)
        showStdDialogsmenu.add_command(label="askquestion",command=self.testeaskquestion)
        showStdDialogsmenu.add_command(label="askretrycancel",command=self.testeaskretrycancel)
        showStdDialogsmenu.add_command(label="askaskyesno",command=self.testeaskyesno)
        showStdDialogsmenu.add_command(label="showerror",command=self. testeshowerror)
        showStdDialogsmenu.add_command(label="showinfo",command=self. testeshowinfo)
        showStdDialogsmenu.add_command(label="showwarning",command=self. testeshowwarning)
 
        menubar.add_cascade(label='Diálogos' , menu= showStdDialogsmenu)
 
        self.root.config(menu=menubar)
 
    def testeshowwarning(self):
        result= tkmsg.showwarning(title='Meu dialogo showwarning', message='Atenção com altas velocidades na estrada!')
 
    def testeshowinfo(self):
        result= tkmsg.showerror(title='Meu dialogo showinfo', message='Analise bem em quem está votando!\nNão desperdice seu voto')
 
    def testeshowerror(self):
        result= tkmsg.showerror(title='Meu dialogo showerror', message='Nosso País foi muito roubado!\nPressione OK para mudar isto!')
 
    def testeaskyesno(self):
        result= tkmsg.askyesno(title='Meu dialogo askyesno', message='Você acha que corrupção deve ser crime inafiançavel?')
        if result == True:
            print ('Voce escolheu SIM')
        else:
            print ('Voce escolheu NÃO')
 
    def testeaskretrycancel(self):
        result= tkmsg.askretrycancel(title='Meu dialogo askretrycancel', message='Tento realizar a conexão outra vez?')
        print (result)
        if result == True:
            print ('Voce escolheu SIM')
        else:
            print ('Voce escolheu NÃO')
 
    def testeaskquestion(self):
        result= tkmsg.askquestion(title='Meu dialogo askquestion', message='Estudar sempre é importante para todos?')
        print (result)
        if result == 'yes':
            print ('Voce escolheu SIM')
        else:
            print ('Voce escolheu NÃO')
 
    def testeaskokcancel(self):
        result= tkmsg.askokcancel(title='Meu dialogo askokcancel', message='Confirma sair do programa?')
        print (result)
        if result == True:
            print ('Voce escolheu OK')
        else:
            print ('Voce escolheu Cancelar')
 
    def testeOpenFileName(self):
        pass
 
    def testeAsksaveasfile(self):
        pass
 
    def testeasksaveasfilename(self):
        pass
 
    def testeaskdirectory(self):
        pass
 
    def execute(self):
        self.root.mainloop()
 
def main(args):
 
    appProc=  TesteDialogs()
    appProc.execute()
    return 0
 
if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))