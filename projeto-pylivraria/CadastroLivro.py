# -*- coding: latin1 -*-
from Livro import Livro
import pygtk
import gtk

pygtk.require('2.0')


class CadastroLivro:

    def __init__(self):
        self.livro = Livro()
        self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        self.vbox = gtk.VBox()
        self.hbox_label_cadastrar = gtk.HBox()
        self.hbox_titulo = gtk.HBox()
        self.hbox_genero = gtk.HBox()
        self.hbox_preco = gtk.HBox()
        self.hbox_autor = gtk.HBox()
        self.hbox_qtde_paginas = gtk.HBox()
        self.hbox_buttons = gtk.HBox()
        self.label_cadastrar = gtk.Label("Cadastrar livro:")
        self.label_titulo = gtk.Label("Título: ")
        self.label_genero = gtk.Label("Gênero: ")
        self.label_preco = gtk.Label("Preço: ")
        self.label_autor = gtk.Label("Autor: ")
        self.label_qtde_paginas = gtk.Label("Qtde. Páginas: ")
        self.text_titulo = gtk.Entry()
        self.text_genero = gtk.Entry()
        self.text_preco = gtk.Entry()
        self.text_autor = gtk.Entry()
        self.text_qtde_paginas = gtk.Entry()
        self.button_salvar = gtk.Button("Salvar")
        self.button_cancelar = gtk.Button("Cancelar")

    def salvar(self, widget):
        self.livro.insert(self.text_titulo.get_text(), self.text_genero.get_text(),
            float(self.text_preco.get_text()), self.text_autor.get_text(),
            int(self.text_qtde_paginas.get_text()))

        self.text_titulo.set_text("")
        self.text_genero.set_text("")
        self.text_preco.set_text("")
        self.text_autor.set_text("")
        self.text_qtde_paginas.set_text("")

    def cancelar(self, widget):
        self.text_titulo.set_text("")
        self.text_genero.set_text("")
        self.text_preco.set_text("")
        self.text_autor.set_text("")
        self.text_qtde_paginas.set_text("")
        print("Operacao cancelada.")

    def monta_interface(self):
        self.hbox_label_cadastrar.pack_start(self.label_cadastrar,
            expand=False, fill=True)

        self.hbox_titulo.pack_start(self.label_titulo, expand=False, fill=True)
        self.hbox_titulo.pack_start(self.text_titulo, expand=False, fill=True)

        self.hbox_genero.pack_start(self.label_genero, expand=False, fill=True)
        self.hbox_genero.pack_start(self.text_genero, expand=False, fill=True)

        self.hbox_preco.pack_start(self.label_preco, expand=False, fill=True)
        self.hbox_preco.pack_start(self.text_preco, expand=False, fill=True)

        self.hbox_autor.pack_start(self.label_autor, expand=False, fill=True)
        self.hbox_autor.pack_start(self.text_autor, expand=False, fill=True)

        self.hbox_qtde_paginas.pack_start(self.label_qtde_paginas,
            expand=False, fill=True)
        self.hbox_qtde_paginas.pack_start(self.text_qtde_paginas,
            expand=False, fill=True)

        self.hbox_buttons.pack_start(self.button_salvar,
            expand=False, fill=True)
        self.hbox_buttons.pack_start(self.button_cancelar,
            expand=False, fill=True)

        self.button_salvar.connect('clicked', self.salvar)
        self.button_cancelar.connect('clicked', self.cancelar)

        self.hbox_label_cadastrar.set_homogeneous(True)
        self.hbox_titulo.set_homogeneous(True)
        self.hbox_genero.set_homogeneous(True)
        self.hbox_preco.set_homogeneous(True)
        self.hbox_autor.set_homogeneous(True)
        self.hbox_qtde_paginas.set_homogeneous(True)
        self.hbox_buttons.set_homogeneous(True)

        self.vbox.pack_start(self.hbox_label_cadastrar,
            expand=False, fill=True)
        self.vbox.pack_start(self.hbox_titulo, expand=False, fill=True)
        self.vbox.pack_start(self.hbox_genero, expand=False, fill=True)
        self.vbox.pack_start(self.hbox_preco, expand=False, fill=True)
        self.vbox.pack_start(self.hbox_autor, expand=False, fill=True)
        self.vbox.pack_start(self.hbox_qtde_paginas, expand=False, fill=True)
        self.vbox.pack_start(self.hbox_buttons, expand=False, fill=True)

        self.window.add(self.vbox)

        # Define o titulo da janela
        self.window.set_title("PyLivraria - Cadastro")

        # Define o icone da aplicacao
        #self.window.set_icon_from_file("img/library.png")

        # Define a posicao da aplicacao na tela
        self.window.set_position(gtk.WIN_POS_CENTER_ALWAYS)

        # Alinha os componentes
        self.vbox.set_homogeneous(True)

        self.window.show_all()

    def start(self):
        self.monta_interface()

        gtk.main()
