from usuario import Usuarios
from tkinter import *


class Application:

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

        self.lblidusuario = Label(self.cont2, text="IdUsuario", font=self.fonte, width=10)
        self.lblidusuario.pack(side=LEFT)

        self.txtidusuario = Entry(self.cont2)
        self.txtidusuario["width"] = 10
        self.txtidusuario["font"] = self.fonte
        self.txtidusuario.pack(side=LEFT)

        self.btnbuscar = Label(self.cont3, text="Busca de Identificação:", font=self.fonte, width=10)
        self.btnbuscar["command"] = self.buscarusuario
        self.btnbuscar.pack(side=LEFT)

        self.lblnome = Label(self.cont3, text="Nome:", font=self.fonte, width=10)
        self.lblnome.pack(side=LEFT)

        self.txtnome = Entry(self.cont3)
        self.txtnome["width"] = 25
        self.txtnome["font"] = self.fonte
        self.txtnome.pack(side=LEFT)

        self.lbltelefone = Label(self.cont4, text="Telefone:", font=self.fonte, width=10)
        self.lbltelefone.pack()

        self.txttelefone = Entry(self.cont4)
        self.txttelefone["width"] = 25
        self.txttelefone["font"] = self.fonte
        self.txttelefone.pack(side=LEFT)

        self.lblemail = Label(self.cont5, text="E-mail", font=self.fonte, width=10)
        self.lblemail.pack(side=LEFT)

        self.txtemail = Entry(self.cont5)
        self.txtemail["width"] = 25
        self.txtemail["font"] = self.fonte
        self.txtemail.pack(side=LEFT)

        self.lblusuario = Label(self.cont6, text="Usuário:", font=self.fonte, width=10)
        self.lblusuario.pack(side=LEFT)

        self.txtusuario = Entry(self.cont6)
        self.txtusuario["width"] = 25
        self.txtusuario["font"] = self.fonte
        self.txtusuario.pack(side=LEFT)

        self.lblsenha = Label(self.cont7, text="Senha:", font=self.fonte, width=10)
        self.lblsenha.pack(side=LEFT)

        self.txtsenha = Entry(self.cont7)
        self.txtsenha["width"] = 25
        self.txtsenha["font"] = self.fonte
        self.txtsenha.pack(side=LEFT)

        self.btnInserir = Button(self.cont8, text="Inserir", font=self.fonte, width=12)
        self.btnInserir["command"] = self.inserirUsuario
        self.btnInserir.pack(side=LEFT)

        self.btnAlterar = Button(self.cont8, text="Alterar", font=self.fonte, width=12)
        self.btnAlterar["command"] = self.alterarUsuario
        self.btnAlterar.pack(side=LEFT)

        self.btnExcluir = Button(self.cont8, text="Excluir", font=self.fonte, width=12)
        self.btnExcluir["command"] = self.excliorUsuario
        self.btnExcluir.pack(side=LEFT)

        self.lblmsg = Label(self.cont9, text="")
        self.lblmsg["font"] = ("Verdana", "9", "italic")
        self.lblmsg.pack()

    def inserirusuario(self):
        user = Usuarios()

        user.nome = self.txtnome.get()
        user.telefone = self.txttelefone.get()
        user.email = self.txtemail.get()
        user.usuario = self.txtusuario.get()
        user.senha = self.txtsenha.get()

        self.lblmsg["text"] = user.inserirUsuario()

        self.txtidusuario.delete(0, END)
        self.txtnome.delete(0, END)
        self.txttelefone.delete(0, END)
        self.txtusuario.delete(0, END)
        self.txtsenha.delete(0, END)

    def alterarusuario(self):
        self.txtidusuario.delete(0, END)
        self.txtnome.delete(0, END)
        self.txttelefone.delete(0, END)
        self.txtemail.delete(0, END)
        self.txtusuario.delete(0, END)
        self.txtsenha.delete(0, END)

    def alterarusuario(self):
        user = Usuarios()

        user.idusuario = self.txtidusuario.get()
        user.nome = self.txtnome.get()
        user.telefone = self.txttelefone.get()
        user.email = self.txtemail.get()
        user.usuario = self.txtusuario.get()
        user.senha = self.txtsenha.get()

        self.lblmsg["text"] = user.updateuser()

        self.txtidusuario.delete(0, END)
        self.txtnome.delete(0, END)
        self.txttelefone.delete(0, END)
        self.txtemail.delete(0, END)
        self.txtusuario.delete(0, END)
        self.txtsenha.delete(0, END)

    def excluirusuario(self):
        user = Usuarios()
        user. idusuario = self.txtidusuario.get()

        self.lblmsg["text"] = user.deleteuser()

        self.txtidusuario.delete(0, END)
        self.txtnome.delete(0, END)
        self.txttelefone.delete(0, END)
        self.txtemail.delete(0, END)
        self.txtusuario.delete(0, END)
        self.txtsenha.delete(0, END)

    def buscarusuario(self):
        user = Usuarios()

        idusuario = self.txtidusuario.get()
        


root = Tk()
Application(root)
root.mainloop()
