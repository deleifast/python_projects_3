import os
import sys
from ctypes import *

lib = cdll.LoadLibrary('ecdSweda.dll')

lib.ecdSweda.dll(3)
