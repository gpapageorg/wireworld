import tkinter as tk
from tkinter import *
from engine import Engine
from gui import Gui
import os
import platform
import ctypes
from tkinter import filedialog as fd

mainbg = '#205375'
secbg = '#F66B0E'
maincol = '#EFEFEF'

MAIN_PATH = os.getcwd()+os.path.sep + 'animations'  + os.path.sep

class MainFrame():

    def __init__(self, root):
        self.root = root

        # Layout Options
        self.root.title("Wireworld Animator")
        self.root.geometry('295x470')
        self.root.configure(background  = mainbg)
        self.root.resizable(True,True)

        # Add Main Header
        self.title1 = tk.Label(root, text = 'Wireworld', font = 'Verdana 20 bold', background = secbg)
        self.title2 = tk.Label(root, text = 'Animator', font = 'Verdana 20 bold', background = secbg)
        self.title3 = tk.Label(root, text = 'by George Papageorgiou', font = 'Verdana 16', background = secbg)
        self.title4 = tk.Label(root, text = 'up1092811@upnet.gr', font = 'Verdana 14', background = secbg)

        self.title1.pack(fill = 'x')
        self.title2.pack(fill = 'x')
        self.title3.pack(fill = 'x')
        self.title4.pack(fill = 'x')


        self.f1 = tk.Frame(root, background = mainbg)
        self.f1.pack(fill = 'x')
        self.f2 = tk.Frame(root, background = mainbg)
        self.f3 = tk.Frame(root, background = mainbg)

        # Add Buttons

        self.ba1 = tk.Button(self.f1, text="00", background= maincol, font = 'verdana 13 ',height = 1, width = 2, command = lambda: self.call_animator('and', int(self.t1.get("1.0",END)), '00'))
        self.ba2 = tk.Button(self.f1, text="01", background= maincol, font = 'verdana 13 ',height = 1, width = 2, command = lambda: self.call_animator('and', int(self.t1.get("1.0",END)), '01'))
        self.ba3 = tk.Button(self.f1, text="10", background= maincol, font = 'verdana 13 ',height = 1, width = 2, command = lambda: self.call_animator('and', int(self.t1.get("1.0",END)), '10'))
        self.ba4 = tk.Button(self.f1, text="11", background= maincol, font = 'verdana 13 ',height = 1, width = 2, command = lambda: self.call_animator('and', int(self.t1.get("1.0",END)), '11'))

        self.bo1 = tk.Button(self.f1, text="00", background= maincol, font = 'verdana 13 ',height = 1, width = 2, command = lambda: self.call_animator('or', int(self.t1.get("1.0",END)), '00'))
        self.bo2 = tk.Button(self.f1, text="01", background= maincol, font = 'verdana 13 ',height = 1, width = 2, command = lambda: self.call_animator('or', int(self.t1.get("1.0",END)), '01'))
        self.bo3 = tk.Button(self.f1, text="10", background= maincol, font = 'verdana 13 ',height = 1, width = 2, command = lambda: self.call_animator('or', int(self.t1.get("1.0",END)), '10'))
        self.bo4 = tk.Button(self.f1, text="11", background= maincol, font = 'verdana 13 ',height = 1, width = 2, command = lambda: self.call_animator('or', int(self.t1.get("1.0",END)), '11'))

        self.bn1 = tk.Button(self.f1, text="00", background= maincol, font = 'verdana 13 ',height = 1, width = 2, command = lambda: self.call_animator('not', int(self.t1.get("1.0",END)), '0'))
        self.bn2 = tk.Button(self.f1, text="01", background= maincol, font = 'verdana 13 ',height = 1, width = 2, command = lambda: self.call_animator('not', int(self.t1.get("1.0",END)), '1'))

        self.bna1 = tk.Button(self.f1, text="00", background= maincol, font = 'verdana 13 ',height = 1, width = 2, command = lambda: self.call_animator('xor', int(self.t1.get("1.0",END)), '00'))
        self.bna2 = tk.Button(self.f1, text="01", background= maincol, font = 'verdana 13 ',height = 1, width = 2, command = lambda: self.call_animator('xor', int(self.t1.get("1.0",END)), '01'))
        self.bna3 = tk.Button(self.f1, text="10", background= maincol, font = 'verdana 13 ',height = 1, width = 2, command = lambda: self.call_animator('xor', int(self.t1.get("1.0",END)), '10'))
        self.bna4 = tk.Button(self.f1, text="11", background= maincol, font = 'verdana 13 ',height = 1, width = 2, command = lambda: self.call_animator('xor', int(self.t1.get("1.0",END)), '11'))
       
        self.bd1 = tk.Button(self.f1, text="C", background= maincol, font = 'verdana 13 ',height = 1, width = 2, command = lambda: self.call_animator('diode', int(self.t1.get("1.0",END)), 'C'))
        self.bd2 = tk.Button(self.f1, text="R", background= maincol, font = 'verdana 13 ',height = 1, width = 2, command = lambda: self.call_animator('diode', int(self.t1.get("1.0",END)), 'R'))
        
        self.f2.pack(fill='x')
        self.f3.pack(fill='x')
       


        self.by1 = tk.Button(self.f3, text="Run Anything!", background= maincol, font = 'verdana 13 ',height = 1, width = 15, command = lambda: self.call_animator(fd.askopenfilename(), int(self.t1.get("1.0",END)), ''))


        # Add Labels
        self.l1 = tk.Label(self.f1, text = 'AND', font = 'verdana 17 ', background= maincol, height = 1, width = 6, borderwidth= 4, relief='ridge')
        self.l2 = tk.Label(self.f1, text = 'OR', font = 'verdana 17 ', background= maincol, height = 1, width = 6, borderwidth= 4, relief='ridge')
        self.l3 = tk.Label(self.f1, text = 'XOR', font = 'verdana 17 ', background= maincol, height = 1, width = 6, borderwidth= 4, relief='ridge')
        self.l4 = tk.Label(self.f1, text = 'NOT', font = 'verdana 17 ', background= maincol, height = 1, width = 6, borderwidth= 4, relief='ridge')
        self.l5 = tk.Label(self.f1, text = 'Diode', font = 'verdana 17 ', background= maincol, height = 1, width = 6, borderwidth= 4, relief='ridge')
        self.l6 = tk.Label(self.f2, text = 'Delay', font = 'verdana 17 ', background= maincol, height = 1, width = 6, borderwidth= 4, relief='ridge')

        # Add Text
        self.t1 = tk.Text(self.f2, font = 'verdana 17 ', background= maincol, height = 1, width = 4)
        self.t1.insert(END,'400')

        self.l1.grid(row = 0, column = 0, padx= 13, pady= 5)
        self.ba1.grid(row = 0, column = 1, padx= 5, pady= 5)
        self.ba2.grid(row = 0, column = 2, padx= 5, pady= 5)
        self.ba3.grid(row = 0, column = 3, padx= 5, pady= 5)
        self.ba4.grid(row = 0, column = 4, padx= 5, pady= 5)

        self.l2.grid(row = 1, column = 0, padx= 13, pady= 5)
        self.bo1.grid(row = 1, column = 1, padx= 5, pady= 5)
        self.bo2.grid(row = 1, column = 2, padx= 5, pady= 5)
        self.bo3.grid(row = 1, column = 3, padx= 5, pady= 5)
        self.bo4.grid(row = 1, column = 4, padx= 5, pady= 5)

        self.l3.grid(row = 2, column = 0, padx= 5, pady= 5)
        self.bna1.grid(row = 2, column = 1, padx= 5, pady= 5)
        self.bna2.grid(row = 2, column = 2, padx= 5, pady= 5)
        self.bna3.grid(row = 2, column = 3, padx= 5, pady= 5)
        self.bna4.grid(row = 2, column = 4, padx= 5, pady= 5)

        self.l4.grid(row = 3, column = 0, padx= 5, pady= 5)
        self.bn1.grid(row = 3, column = 1, padx= 5, pady= 5)
        self.bn2.grid(row = 3, column = 2, padx= 5, pady= 5)

        self.l5.grid(row = 4, column=0, padx = 5, pady = 5)
        self.bd1.grid(row = 4, column=1, padx = 5, pady = 5)
        self.bd2.grid(row = 4, column=2, padx = 5, pady = 5)

        self.l6.grid(row = 0, column=0, padx = 13, pady = 5)
        self.t1.grid(row = 0, column=1, padx = 5, pady = 5)
        self.by1.grid(row = 0, column=0, padx = 13, pady = 5)


    def call_animator(self, name, delay, var):
        name = os.path.basename(name)
        if(name.find('.txt') == -1):
            initial_state = Engine.load(MAIN_PATH  + name + str(var) + '.txt')
        else:
            initial_state = Engine.load(MAIN_PATH  + name + str(var))


        ww = Engine(initial_state)
        Gui(ww, delay).start() 

root = tk.Tk()
photo = PhotoImage(file = "w.png")
root.iconphoto(False, photo)
if(platform.system() == 'Windows'):
    myappid = 'mycompany.myproduct.subproduct.version' # arbitrary string
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

main = MainFrame(root)

root.mainloop()
