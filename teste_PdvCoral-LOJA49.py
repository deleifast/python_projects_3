#encoding: iso-8859-1
import os, shutil, subprocess, time, glob, copy, os.path, sys, socket, threading
from zipfile import ZipFile


try: import tkinter
except ImportError:
    import Tkinter as tkinter
    import ttk
else: from tkinter import ttk
from tkinter import *




class GUI_Core(object):

    def __init__(self):
        self.root = tkinter.Tk()
        self.progbar = ttk.Progressbar(self.root)
        self.progbar.config(orient ="horizontal",length = 400, mode='determinate')
        self.progbar.pack()
        self.msg = Label(self.root, text='Aguarde, iniciando servi�os do Pdv/SAT...', fg="red", font='Arial 18')
        self.msg.pack()
		

        self.progbar.start()
        self.secondary_thread = threading.Thread(target=pdv)
        self.secondary_thread.start()
        self.root.after(10, self.check_thread)
					

    def check_thread(self):
        if self.secondary_thread.is_alive():
            self.root.after(10, self.check_thread)
        else:
            self.progbar.stop()

						

def pdv():

		time.sleep(30)
		# initialize
		driveLetter = 'X:' 
		networkPath = '\\\\10.0.20.42\Atual' 
		user = 'compartilhar' 
		password = 'ruaf305'

		# Connect to map network drive to letter Q
		winCMD = 'NET USE ' + driveLetter + ' ' + networkPath + ' /User:' + user + ' ' + password
		exitcode = subprocess.call(winCMD, shell=True)
		print (exitcode)

		if exitcode == 0:
			print(winCMD)

		else:
				exitcode == 2

				os.chdir('C:\\PDV')

				path = 'C:\\PDV'
				dir = os.listdir(path)
				for file in dir:
					if file == "pdv.txt":
						os.remove(file)

				hostName    = ""

				ipAddress   = socket.gethostbyname_ex(socket.gethostname())

				time.sleep(5)
				msg = Label(gui.root, text="Sem conex�o com o Servidor, enviando e-mail....", fg="blue", font= 'Arial 18')
				msg.pack()

#				print("PDV e IP {} : {}".format(hostName,ipAddress))

				with open('pdv.txt', 'a') as caixa:
					caixa.write(str("PDV e IP {} : {}".format(hostName,ipAddress)))
					caixa.close()

				
				os.startfile(r"Enviando_Email_i.exe")

				time.sleep(10)

				os.startfile(r"Acertar_horario_i.exe")

				time.sleep(10)

				os.startfile(r"c:\\pdv\pdvsal.exe")

				time.sleep(10)

				msg.pack_forget()
				msg = Label(gui.root, text='Processos inicializados sem atualiza��o!' + '\n' + 'Remarca verificar!', bg = "yellow", fg="red", font= 'Arial 18')
				msg.pack()


				sys.exit()

		
#		print('Copiando arquivos para o PDV e SAT sendo iniciado, aguarde....' + '\n')	
		msg = Label(gui.root, text='Copiando arquivos para o PDV, aguarde....', fg="blue", font= 'Arial 18')
		msg.pack()



		PATHPDV='X://loja49_pdv.zip'
		PATHPLUGIN='X://loja49_plugin.zip'

		if os.path.isfile(PATHPDV):
			
			dest_dir = "C:\\PDV"
			for file in glob.glob(r'X:/loja49_pdv.zip'):
				print(file)
			shutil.copy(file, dest_dir)

		else:
#			print("Sem arquivos(PDV) para atualizar no Servidor" + "\n")
			time.sleep(5)
			msg.pack_forget()
			msg = Label(gui.root, text="Sem arquivos(PDV) para atualizar no Servidor", fg="blue", font= 'Arial 18')
			msg.pack()


		if os.path.isfile(PATHPLUGIN):
			
			dest_dir = "C:\\PDV\PLUGIN"
			for file in glob.glob(r'X:/loja49_plugin.zip'):
				print(file)
			shutil.copy(file, dest_dir)

		else:
			time.sleep(5)
#			print("Sem arquivos(PLUGIN) para atualizar no Servidor" + "\n")
			msg.pack_forget()
			msg = Label(gui.root, text="Sem arquivos(PLUGIN) para atualizar no Servidor", fg="blue", font= 'Arial 18')
			msg.pack()


		# Disconnect anything on drive letter Q
		winCMD = 'NET USE ' + driveLetter + ' /delete /y'
		print(winCMD)
		subprocess.call(winCMD, shell=True)

		PATHPDV='C://PDV/loja49_pdv.zip'
		PATHPLUGIN='C://PDV/PLUGIN/loja49_plugin.zip'

		if os.path.isfile(PATHPDV):

		# specifying the zip file name
			file_pdv = "c:\\pdv\loja49_pdv.zip"
		 
		# opening the zip file in READ mode
			with ZipFile(file_pdv, 'r') as zip:
			# printing all the contents of the zip file
			#	zip.printdir()

				with open("versao_pdv.txt", "w") as pdv:
					for file_info in zip.infolist():
						print(file_info.filename, file_info.date_time, 'tamanho do arquivo descompactado = ', file_info.file_size, file=pdv)

			# extracting all the files
				time.sleep(5)
				msg.pack_forget()
				msg = Label(gui.root, text="Extraindo todos os arquivos do pdv agora...", fg="blue", font= 'Arial 18')
				msg.pack()

#				print('Extraindo todos os arquivos agora...')
				zip.extractall('c:\\pdv')
				time.sleep(5)
				msg.pack_forget()
				msg = Label(gui.root, text="Pdv OK!", fg="blue", font= 'Arial 18')
				msg.pack()

#				print('Pronto pdv!' + '\n')
		else:
			time.sleep(5)
			msg.pack_forget()
			msg = Label(gui.root, text="Sem arquivos(PDV) para descompactar", fg="blue", font= 'Arial 18')
			msg.pack()

#			print("Sem arquivos(PDV) para descompactar" + "\n")

		if os.path.isfile(PATHPLUGIN):

		# specifying the zip file name
			file_plugin = "c:\\pdv\plugin\loja49_plugin.zip"
		 
		# opening the zip file in READ mode
			with ZipFile(file_plugin, 'r') as zip:
			# printing all the contents of the zip file
			#	zip.printdir()

				with open("versao_plugin.txt", "w") as pdv:
					for file_info in zip.infolist():
						print(file_info.filename, file_info.date_time, 'tamanho do arquivo descompactado = ', file_info.file_size, file=pdv)

			# extracting all the files
				time.sleep(5)
				msg.pack_forget()
				msg = Label(gui.root, text="Extraindo todos os arquivos do plugin agora...", fg="blue", font= 'Arial 18')
				msg.pack()

#				print('Extraindo todos os arquivos agora...')
				zip.extractall('c:\\pdv\plugin')
				time.sleep(5)
				msg.pack_forget()
				msg = Label(gui.root, text="Plugin OK!", fg="blue", font= 'Arial 18')
				msg.pack()

#				print('Pronto plugin!' + '\n')

		else:
			time.sleep(5)
			msg.pack_forget()
			msg = Label(gui.root, text="Sem arquivos(PLUGIN) para descompactar", fg="blue", font= 'Arial 18')
			msg.pack()

#			print("Sem arquivos(PLUGIN) para descompactar" + "\n")	


		os.chdir('C:\\PDV')

		os.startfile(r"Acertar_horario_i.exe")

		time.sleep(10)

		os.startfile(r"Deleta_Arquivo_loja49.exe")

		time.sleep(10)

		msg.pack_forget()
		msg = Label(gui.root, text='Processos inicializados com sucesso!', fg="blue", font= 'Arial 18')
		msg.pack()

		time.sleep(10)

		os.startfile(r"pdvsal.exe")
		
		gui.root.destroy()

		
	
gui = GUI_Core()
gui.root.wm_iconbitmap('icon1.ico')
gui.root.title("Atualizador REMARCA/NAGUMO - Versao 2.0")
gui.root.mainloop()