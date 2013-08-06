# -*- coding: latin1 -*-
from CadastroLivro import CadastroLivro
import pygtk
import gtk

pygtk.require('2.0')


class Home:

    def __init__(self):
        self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        self.vbox = gtk.VBox()
        self.hbox = gtk.HBox()
        self.button_cadastro = gtk.Button("Cadastro")

    def chama_cadastro(self, widget):
        self.window.destroy()
        cadastro_livro = CadastroLivro()
        print("Tela Cadastro de Livros.")
        cadastro_livro.start()

    def monta_interface(self):
        self.hbox.pack_start(self.button_cadastro, expand=False, fill=True)

        self.vbox.pack_start(self.hbox, expand=False, fill=True)

        self.window.add(self.vbox)

        self.button_cadastro.connect('clicked', self.chama_cadastro)

        # Define o titulo da janela
        self.window.set_title("PyLivraria - Home")

        # Define o icone da aplicacao
        self.window.set_icon_from_file("img/library.png")

        # Define a posicao da aplicacao na tela
        self.window.set_position(gtk.WIN_POS_CENTER_ALWAYS)

        # Alinha os componentes
        self.vbox.set_homogeneous(True)

        self.window.show_all()

    def start(self):
        self.monta_interface()

        gtk.main()
