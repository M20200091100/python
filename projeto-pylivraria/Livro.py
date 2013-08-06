# -*- coding: latin1 -*-
from Banco import Banco
import traceback


class Livro:

    def __init__(self):
        self.b = Banco()

    def insert(self, titulo="", genero="", preco=0.0, autor="", qtde_paginas=0):
        self.titulo = titulo
        self.genero = genero
        self.preco = preco
        self.autor = autor
        self.qtde_paginas = qtde_paginas

        try:
            cursor = self.b.conn.cursor()

            if self.titulo != "" and self.genero != "" and self.preco > 0 and self.autor != "" and self.qtde_paginas > 0:
                query = "insert into livro values\
                (NULL, '" + self.titulo + "', '" + self.genero + "', %f, '" + self.autor + "', %d)"

                cursor.execute(query % (self.preco, self.qtde_paginas))

                self.b.conn.commit()
                print("Livro inserido com sucesso.")
                cursor.close()
            else:
                print("Insira os dados corretamente")
        except:
            trace = traceback.format_exc()
            self.b.conn.rollback()
            print("Nao foi possivel inserir o livro no banco, ocorreu o seguinte erro: ", trace)
            cursor.close()

    def delete(self, id=0):
        self.id = id

        try:
            cursor = self.b.conn.cursor()
            query = "delete from livro where id = %d"

            cursor.execute(query % self.id)
            self.b.conn.commit()
            print("Livro excluido com sucesso.")
            cursor.close()
        except:
            trace = traceback.format_exc()
            self.b.conn.rollback()
            cursor.close()
            print("Nao foi possivel excluir o livro, ocorreu o seguinte erro: ", trace)

    def select_by_titulo(self, titulo=""):
        self.titulo = titulo

        try:
            cursor = self.b.conn.cursor()

            query = "select * from livro where titulo like '%" + self.titulo + "%'"

            cursor.execute(query)

            for dado in cursor:
                self.id = dado[0]
                self.titulo = dado[1]
                self.genero = dado[2]
                self.preco = dado[3]
                self.autor = dado[4]
                self.qtde_paginas = dado[5]
                print(self.id)

            print("Consulta por titulo realizada com sucesso.")
            cursor.close()
        except:
            trace = traceback.format_exc()
            cursor.close()
            print("Nao foi possivel consultar o livro no banco, ocorreu o seguinte erro: ", trace)

    def select_by_id(self, id=0):
        self.id = id

        try:
            cursor = self.b.conn.cursor()

            query = "select * from livro where id = %d"

            cursor.execute(query % self.id)
            for dado in cursor:
                self.id = dado[0]
                self.titulo = dado[1]
                self.genero = dado[2]
                self.preco = dado[3]
                self.autor = dado[4]
                self.qtde_paginas = dado[5]

            print("Consulta por id realizada com sucesso.")
            cursor.close()
        except:
            trace = traceback.format_exc()
            cursor.close()
            print("Nao foi possivel consultar o livro no banco, ocorreu o seguinte erro: ", trace)

    def update(self, id=0):
        self.id = id

        self.select_by_id(self.id)

        try:
            cursor = self.b.conn.cursor()

            query = "update livro set titulo = '" + self.titulo + "', genero = '" + self.genero + "', \
                preco = %f, autor = '" + self.autor + "', qtde_paginas = %d where id = %d"

            print(self.titulo, self.autor)

            cursor.execute(query % (self.preco, self.qtde_paginas, self.id))
            self.b.conn.commit()
            print("Livro atualizado com sucesso.")
        except:
            trace = traceback.format_exc()
            self.b.conn.rollback()
            cursor.close()
            print("Nao foi possivel atualizar o livro, ocorreu o seguinte erro: ", trace)
