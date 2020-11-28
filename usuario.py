from Banco import Banco
class usuarios(object):


    def __init__(self, idusuario= "", nome = "", telefone = "", email = "", usuario = "", senha= ""):
        self.info = {}
        self.idusuario = idusuario
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.usuario = usuario
        self.senha = senha

#  Insert User code
    def insertUser(self):
        banco = Banco()
        try:

            c = banco.conexao.cursor()

            c.execute("insert into usuarios (nome, telefone, email, usuario, senha) Values"
                      " ('" + self.nome + "', '" + self.telefone + "', '" + self.email + "', '" +
                      self.usuario + "', '" + self.senha + "' )'")
            banco.conexao.commit()
            c.close()
            return "Usuário cadastrado com sucesso!"
        except:
            return "Ocorreu um erro no processo de inscrição"

#  Update User code
    def updateuser(self):
        banco = Banco()
        try:

            c = banco.conexao.cursor()

            c.execute("update usuarios set nome = '" + self.nome + "',telefone = '" + self.telefone +
                      "', email = '" + self.email + "', usuario = '" + self.usuario + "', senha = '" + self.senha +
                      "' where idusuario = " + self.idusuario + " ")


            banco.conexao.commit()
            c.close()
            return "Cadastro de usuário atualizado com sucesso!"
        except:
            return "Houve um erro ao atualizar o seu cadastro."

    def deleteuser(self):

        banco = Banco()
        try:

            c = banco.conexao.cursor()
            c.execute("delete from usuarios where idusuario = " + self.idusuario + " ")
            banco.conexao.commit()
            c.close()

            return "Cadastro excluído com sucesso."
        except:
            return "Houve um erro ao excuír seu cadastro na MarqueCom."

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
        except:
            return "Não houve resultados na busca."