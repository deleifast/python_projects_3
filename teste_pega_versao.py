from win32api import *
  
def get_version_number(file_path): 
  
    File_information = GetFileVersionInfo(file_path, "\\") 
  
    ms_file_version = File_information['FileVersionMS'] 
    ls_file_version = File_information['FileVersionLS'] 
  
    return [str(HIWORD(ms_file_version)), str(LOWORD(ms_file_version)), 
            str(HIWORD(ls_file_version)), str(LOWORD(ls_file_version))] 
  
file_path = r'C:\pdv\pdvsal.exe'
  
version = ".".join(get_version_number(file_path)) 
  
print(version)
