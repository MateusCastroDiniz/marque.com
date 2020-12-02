from tkinter import*


class Application:
    def __init__(self, master=None):
        self.fpadrao = ("Arial", "10")
        self.pgn1 = Frame(master)
        self.pgn1["pady"] = 10
        self.pgn1.pack()

        self.pgn2 = Frame(master)
        self.pgn2["padx"] = 20
        self.pgn2.pack()

        self.pgn3 = Frame(master)
        self.pgn3["padx"] = 20
        self.pgn3.pack()

        self.pgn4 = Frame(master)
        self.pgn4["pady"] = 20
        self.pgn4.pack()

        self.titulo = Label(self.pgn1, text="Dados do Usuário")
        self.titulo["font"] = ("Arial", "10", "bold")
        self.titulo.pack()

        self.nomeLabel = Label(self.pgn2, text="Nome", font=self.fpadrao)
        self.nomeLabel.pack(side=LEFT)

        self.nome = Entry(self.pgn2)
        self.nome["width"] = 20
        self.nome["font"] = self.fpadrao
        self.nome.pack(side=LEFT)

        self.senhaLabel = Label(self.pgn3, text="Senha", font=self.fpadrao)
        self.senhaLabel.pack(side=LEFT)

        self.senha = Entry(self.pgn3)
        self.senha["width"] = 20
        self.senha["font"] = self.fpadrao
        self.senha["show"] = "*"
        self.senha.pack(side=LEFT)

        self.autenticar = Button(self.pgn4)
        self.autenticar["text"] = "Autenticar"
        self.autenticar["font"] = ("Calibri", "8")
        self.autenticar["width"] = 12
        self.autenticar["command"] = self.login
        self.autenticar.pack()

        self.mensagem = Label(self.pgn4, text="", font=self.fpadrao)
        self.mensagem.pack()

    # Método verificar senha
    def login(self):
        usuario = self.nome.get()
        senha = self.senha.get()
        if usuario == "Dina" and senha == "1190":
            self.mensagem["text"] = "Autenticado"
        else:
            self.mensagem["text"] = "Erro na autenticação"


root = Tk()
Application(root)
root.mainloop()
