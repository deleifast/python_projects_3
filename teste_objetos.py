#encoding: iso-8859-1

from tkinter import *
from platform import python_version


def main(args):

	root = Tk()

	Label(root, text="Texto superior", bg="red", fg="white").pack()
	Label(root, text="Texto intermediário", bg="yellow", fg="black").pack()
	Label(root, text="Texto inferior", bg="green", fg="white").pack()

	mainloop()

	return 0

if __name__ == '__main__':
    import sys
    print (python_version())   #somente para verificar que estamos no ambiente virtual python 3.5
    sys.exit(main(sys.argv))