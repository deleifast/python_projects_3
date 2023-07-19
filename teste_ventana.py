#encoding: iso-8859-1

import os, shutil, subprocess, time, glob, copy, os.path, sys, socket, threading, rarfile, datetime, win32gui, win32con
from zipfile import ZipFile
from pathlib import Path
from datetime import datetime


try: import tkinter
except ImportError:
    import Tkinter as tkinter
    import ttk
else: from tkinter import ttk
from tkinter import *


def startProgram():
    SW_MINIMIZE = 6
    info = subprocess.STARTUPINFO()
    info.dwFlags = subprocess.STARTF_USESHOWWINDOW
    info.wShowWindow = SW_MINIMIZE
    subprocess.Popen(r'C:/PDV/ventanarf_central.exe', startupinfo=info)
startProgram()
