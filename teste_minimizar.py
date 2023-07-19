import subprocess 

def startProgram(): 
    SW_MINIMIZE = 6 
    info = subprocess.STARTUPINFO() 
    info.dwFlags = subprocess.STARTF_USESHOWWINDOW 
    info.wShowWindow = SW_MINIMIZE 
    subprocess.Popen(r'C:\\pdv\\ventanarf_central.exe', startupinfo=info) 
startProgram() 
