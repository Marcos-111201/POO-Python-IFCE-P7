#importando módulo do SQlite
import sqlite3

class Banco():
    def __init__(self):
        self.conexao = sqlite3.connect('cadastroFilmes.db')
        self.createTable()

    def createTable(self):
        c = self.conexao.cursor()

        c.execute("""create table if not exists Filmes (
                    idFilme integer primary key autoincrement ,
                    titulo text,
                    genero text,
                    duracao text,
                    clasIndic text,
                    nota text)""")
        self.conexao.commit()
        c.close()