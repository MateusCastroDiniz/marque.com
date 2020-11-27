import sqlite3


class Banco:

    def __init__(self):
        self.conexao = sqlite3.connect('banco.db')
        self.createtable()

    def createtable(self):
        c = self.conexao.cursor()

        c.execute("""create table if not exists usuarios (
                 idusuario integer primary key autoincrement ,
                 nome text,
                 telefone text,
                 email text,
                 usuario text,
                 senha text)""")
        self.conexao.commit()
        c.close()
#  se afobe não fabiano2
