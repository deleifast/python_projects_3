import zipfile

zip_archive = zipfile.ZipFile("teste.zip", "r")

with open("versao.txt", "w") as pdv:
	for file_info in zip_archive.infolist():
		print(file_info.filename, file_info.date_time, 'tamanho do arquivo descompactado = ', file_info.file_size, file=pdv)



