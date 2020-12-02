from Banco import Banco


#  Código finalizado!
from Banco import Banco


class Usuarios(object):

    def __init__(self, idusuario=0, nome="", telefone="",
                 email="", usuario="", senha=""):
        self.info = {}
        self.idusuario = idusuario
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.usuario = usuario
        self.senha = senha

#  Insert User code (Concluído).
    def inserirusuario(self):

        banco = Banco()
        try:

            c = banco.conexao.cursor()

            c.execute("insert into usuarios (nome, telefone, email,"
                      " usuario, senha) values('" + self.nome + "', '" +
                      self.telefone + "', '" + self.email + "', '" + self.usuario +
                      "', '" + self.senha + "' )")
            banco.conexao.commit()
            c.close()
            return "Usuário cadastrado com sucesso!"
        except Error:
            return "Houve um problema ao cadastrar o usuário"

#  Update User code (Concluído).

    def updateuser(self):
        banco = Banco()
        try:

            c = banco.conexao.cursor()

            c.execute("update usuarios set nome = '" + self.nome + "',"
                      " telefone = '" + self.telefone + "', email = '" + self.email +
                      "', usuario = '" + self.usuario + "', senha = '" + self.senha +
                      "' where idusuario = " + self.idusuario + " ")

            banco.conexao.commit()
            c.close()
            return "Cadastro de usuário atualizado com sucesso!"
        except Error:
            return "Houve um erro ao atualizar o seu cadastro."

    def deleteuser(self):

        banco = Banco()
        try:

            c = banco.conexao.cursor()

            c.execute("delete from usuarios where idusuario = " + self.idusuario + " ")

            banco.conexao.commit()
            c.close()

            return "Usuário excluído com sucesso!"
        except Error:
            return "Ocorreu um erro na exclusão do usuário"

    def selectuser(self, idusuario):
        banco = Banco()
        try:

            c = banco.conexao.cursor()

            c.execute("select * from usuarios where idusuario = " + idusuario + "  ")

            for linha in c:
                self.idusuario = linha[0]
                self.nome = linha[1]
                self.telefone = linha[2]
                self.email = linha[3]
                self.usuario = linha[4]
                self.senha = linha[5]

            c.close()
            return "Busca feita com sucesso!"
        except Error:
            return "Não houve resultados na busca."
