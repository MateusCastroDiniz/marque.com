from usuario import usuarios
from tkinter import *


class Appliction:

    def __init__(self, master=None):
        self.fonte = ("Verdana", "10")

        self.cont1 = Frame(master)
        self.cont1["pady"] = "10"
        self.cont1.pack()
        self.cont2 = Frame(master)
        self.cont2["padx"] = "20"
        self.cont2["pady"] = "5"
        self.cont2.pack()
        self.cont3 = Frame(master)
        self.cont3["padx"] = "20"
        self.cont3["pady"] = "5"
        self.cont3.pack()
        self.cont4 = Frame(master)
        self.cont4["padx"] = "20"
        self.cont4["pady"] = "5"
        self.cont4.pack()
        self.cont5 = Frame(master)
        self.cont5["padx"] = "20"
        self.cont5["pady"] = "5"
        self.cont5.pack()
        self.cont6 = Frame(master)
        self.cont6["padx"] = "20"
        self.cont6["pady"] = "5"
        self.cont6.pack()
        self.cont7 = Frame(master)
        self.cont7["padx"] = "20"
        self.cont7["pady"] = "5"
        self.cont7.pack()
        self.cont8 = Frame(master)
        self.cont8["padx"] = "20"
        self.cont8["pady"] = "10"
        self.cont8.pack()
        self.cont9 = Frame(master)
        self.cont9["pady"] = "15"
        self.cont9.pack()

        self.titulo = Label(self.cont1, text="Cadastre-se aqui:")
        self.titulo["font"] = ("Calibri", "9", "bold")
        self.titulo.pack()

        self.lbidusuario = Label(self.cont2, text="IdUsuario", font=self.fonte, width=10)
        self.lbidusuario.pack(side=LEFT)


root = Tk()
Appliction(root)
root.mainloop()
