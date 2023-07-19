#encoding: iso-8859-1
import tkinter as tk
import sys
import pygubu
 
 
class myApp(object):
     
    def __init__(self, **kw):
        #insira toda a inicialização aqui
        self.root = tk.Tk()
        self.root.title("Exp1- 20/11/2017 - Caderno de laboratório")
                            
        #1: Crie um buider
        self.builder = builder = pygubu.Builder()
         
        #2: leia o arquivo  ui .
        builder.add_from_file('exp2.ui')       
         
        #3: Create a janela principal
        self.mainwindow = builder.get_object('Frame_1', self.root)
 
 
    def execute(self):
        self.root.mainloop()
 
 
 
def main(args):
    app_proc = myApp()
    app_proc.execute()
    return 0
 
     
    return 0
 
 
if __name__ == '__main__':
    sys.exit(main(sys.argv))