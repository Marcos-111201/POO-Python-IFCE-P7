from Banco import Banco

class Filmes(object):
    def __init__(self, idFilme = 0, titulo = "", genero = "", duracao = "", clasIndic = "", nota = ""):
        self.info = {}
        self.idFilme = idFilme
        self.titulo = titulo
        self.genero = genero
        self.duracao = duracao
        self.clasIndic = clasIndic
        self.nota = nota


    def insertFilme(self):
        banco = Banco()
        try:
            c = banco.conexao.cursor()

            c.execute("insert into Filmes (titulo, genero, duracao, clasIndic, nota) values ('" + self.titulo + "', '" + self.genero + "', '" + self.duracao + "', '" + self.clasIndic + "', '" + self.nota + "' )")

            banco.conexao.commit()
            c.close()

            return "Filme cadastrado com sucesso!"
        except:
            return "Ocorreu um erro na inserção do Filme"

    def updateFilme(self):
        banco = Banco()
        try:
            c = banco.conexao.cursor()

            c.execute("update Filmes set titulo = '" + self.titulo + "', genero = '" + self.genero + "', duracao = '" + self.duracao + "', clasIndic = '" + self.clasIndic + "', nota = '" + self.nota + "' where idFilme = " + self.idFilme + " ")

            banco.conexao.commit()
            c.close()

            return "Filme atualizado com sucesso!"
        except:
            return "Ocorreu um erro na alteração do Filme"

    def deleteFilme(self):
        banco = Banco()
        try:
            c = banco.conexao.cursor()

            c.execute("delete from Filmes where idFilme = " + self.idFilme + " ")

            banco.conexao.commit()
            c.close()

            return "Filme excluído com sucesso!"
        except:
            return "Ocorreu um erro na exclusão do Filme"

    def selectFilme(self, idFilme):
        banco = Banco()
        try:
            c = banco.conexao.cursor()

            c.execute("select * from Filmes where idFilme = " + idFilme + "  ")

            for linha in c:
                self.idFilme = linha[0]
                self.titulo = linha[1]
                self.genero = linha[2]
                self.duracao = linha[3]
                self.clasIndic = linha[4]
                self.nota = linha[5]

            c.close()

            return "Busca feita com sucesso!"
        except:
            return "Ocorreu um erro na busca do Filme"