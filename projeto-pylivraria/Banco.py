# -*- coding: latin1 -*-
import MySQLdb
import traceback


class Banco:

    def __init__(self):
        try:
            self.conn = MySQLdb.connect("localhost", "root", "rootpass", "pylivraria")
            print("Conexao realizada com sucesso.")
        except:
            trace = traceback.format_exc()
            print("Nao foi possivel conectar-se ao banco, ocorreu o erro: ", trace)
