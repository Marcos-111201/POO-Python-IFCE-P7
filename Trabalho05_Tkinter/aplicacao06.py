from Filmes import Filmes
from tkinter import *
from PIL import ImageTk, Image
import os

class Interface:
    def __init__(self, master=None):
        self.fonte = ("Verdana", "8")

        self.container1 = Frame(master)
        self.container1["pady"] = 10
        self.container1.pack()

        self.container2 = Frame(master)
        self.container2["padx"] = 20
        self.container2["pady"] = 5
        self.container2.pack()

        self.container3 = Frame(master)
        self.container3["padx"] = 20
        self.container3["pady"] = 5
        self.container3.pack()

        self.container4 = Frame(master)
        self.container4["padx"] = 20
        self.container4["pady"] = 5
        self.container4.pack()

        self.container5 = Frame(master)
        self.container5["padx"] = 20
        self.container5["pady"] = 5
        self.container5.pack()

        self.container6 = Frame(master)
        self.container6["padx"] = 20
        self.container6["pady"] = 5
        self.container6.pack()

        self.container7 = Frame(master)
        self.container7["padx"] = 20
        self.container7["pady"] = 5
        self.container7.pack()

        self.container8 = Frame(master)
        self.container8["padx"] = 20
        self.container8["pady"] = 10
        self.container8.pack()

        self.container9 = Frame(master)
        self.container9["pady"] = 15
        self.container9.pack()

        self.titulo = Label(self.container1, text="SEJA BEM-VINDO(A) AO CADASTRO\n\nInsirira os dados do filme:")
        self.titulo["font"] = ("Calibri", "15", "bold")
        self.titulo.pack ()

        self.lblidFilme = Label(self.container2, text="idFilme:", font=self.fonte, width=10)
        self.lblidFilme.pack(side=LEFT)

        self.txtidFilme = Entry(self.container2)
        self.txtidFilme["width"] = 25
        self.txtidFilme["font"] = self.fonte
        self.txtidFilme.pack(side=LEFT)

        self.lbltitulo = Label(self.container3, text="Titulo:", font=self.fonte, width=10)
        self.lbltitulo.pack(side=LEFT)

        self.txttitulo = Entry(self.container3)
        self.txttitulo["width"] = 25
        self.txttitulo["font"] = self.fonte
        self.txttitulo.pack(side=LEFT)

        self.lblgenero = Label(self.container4, text="Genero:", font=self.fonte, width=10)
        self.lblgenero.pack(side=LEFT)

        self.txtgenero = Entry(self.container4)
        self.txtgenero["width"] = 25
        self.txtgenero["font"] = self.fonte
        self.txtgenero.pack(side=LEFT)

        self.lblduracao= Label(self.container5, text="Duração:", font=self.fonte, width=10)
        self.lblduracao.pack(side=LEFT)

        self.txtduracao = Entry(self.container5)
        self.txtduracao["width"] = 25
        self.txtduracao["font"] = self.fonte
        self.txtduracao.pack(side=LEFT)

        self.lblclasIndic= Label(self.container6, text="ClassIndicat:", font=self.fonte, width=10)
        self.lblclasIndic.pack(side=LEFT)

        self.txtclasIndic = Entry(self.container6)
        self.txtclasIndic["width"] = 25
        self.txtclasIndic["font"] = self.fonte
        self.txtclasIndic.pack(side=LEFT)

        self.lblnota= Label(self.container7, text="Nota:", font=self.fonte, width=10)
        self.lblnota.pack(side=LEFT)

        self.txtnota = Entry(self.container7)
        self.txtnota["width"] = 25
        self.txtnota["font"] = self.fonte
        self.txtnota.pack(side=LEFT)

        self.bntInsert = Button(self.container8, text="Inserir", font=self.fonte, width=12)
        self.bntInsert["command"] = self.inserirFilme
        self.bntInsert.pack (side=LEFT)

        self.bntAlterar = Button(self.container8, text="Alterar", font=self.fonte, width=12)
        self.bntAlterar["command"] = self.alterarFilme
        self.bntAlterar.pack (side=LEFT)

        self.bntExcluir = Button(self.container8, text="Excluir", font=self.fonte, width=12)
        self.bntExcluir["command"] = self.excluirFilme
        self.bntExcluir.pack(side=LEFT)

        self.btnBuscar = Button(self.container8, text="Buscar", font=self.fonte, width=12)
        self.btnBuscar["command"] = self.buscarFilme
        self.btnBuscar.pack(side=BOTTOM)

        self.lblmsg = Label(self.container9, text="")
        self.lblmsg["font"] = ("Verdana", "9", "italic")
        self.lblmsg.pack()


    def inserirFilme(self):
        filme = Filmes()

        filme.titulo = self.txttitulo.get()
        filme.genero = self.txtgenero.get()
        filme.duracao = self.txtduracao.get()
        filme.clasIndic = self.txtclasIndic.get()
        filme.nota = self.txtnota.get()

        self.lblmsg["text"] = filme.insertFilme()

        self.txtidFilme.delete(0, END)
        self.txttitulo.delete(0, END)
        self.txtgenero.delete(0, END)
        self.txtduracao.delete(0, END)
        self.txtclasIndic.delete(0, END)
        self.txtnota.delete(0, END)



    def alterarFilme(self):
        filme = Filmes()

        filme.idFilme = self.txtidFilme.get()
        filme.titulo = self.txttitulo.get()
        filme.genero = self.txtgenero.get()
        filme.duracao = self.txtduracao.get()
        filme.clasIndic = self.txtclasIndic.get()
        filme.nota = self.txtnota.get()

        self.lblmsg["text"] = filme.updateFilme()

        self.txtidFilme.delete(0, END)
        self.txttitulo.delete(0, END)
        self.txtgenero.delete(0, END)
        self.txtduracao.delete(0, END)
        self.txtclasIndic.delete(0, END)
        self.txtnota.delete(0, END)



    def excluirFilme(self):
        filme = Filmes()

        filme.idFilme = self.txtidFilme.get()

        self.lblmsg["text"] = filme.deleteFilme()

        self.txtidFilme.delete(0, END)
        self.txttitulo.delete(0, END)
        self.txtgenero.delete(0, END)
        self.txtduracao.delete(0, END)
        self.txtclasIndic.delete(0, END)
        self.txtnota.delete(0, END)


    def buscarFilme(self):
        filme = Filmes()

        idFilme = self.txtidFilme.get()

        self.lblmsg["text"] = filme.selectFilme(idFilme)

        self.txtidFilme.delete(0, END)
        self.txtidFilme.insert(INSERT, filme.idFilme)

        self.txttitulo.delete(0, END)
        self.txttitulo.insert(INSERT, filme.titulo)

        self.txtgenero.delete(0, END)
        self.txtgenero.insert(INSERT,filme.genero)

        self.txtduracao.delete(0, END)
        self.txtduracao.insert(INSERT, filme.duracao)

        self.txtclasIndic.delete(0, END)
        self.txtclasIndic.insert(INSERT, filme.clasIndic)

        self.txtnota.delete(0, END)
        self.txtnota.insert(INSERT,filme.nota)


root = Tk()
img = ImageTk.PhotoImage(Image.open("C:\\Users\\amaur\\OneDrive\\Imagens\\Saved Pictures\\cinema.jpg"))
panel = Label(root, image = img)
panel.pack()
Interface(root)
root.mainloop()
