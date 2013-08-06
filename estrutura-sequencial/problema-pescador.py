# -*- coding: latin1 -*-
"""João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho. 
Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) 
deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça um programa que leia a variável 
peso (peso de peixes) e verifique se há excesso. Se houver, gravar na variável excesso e na variável multa o valor 
da multa que João deverá pagar. Caso contrário mostrar tais variáveis com o conteúdo ZERO."""

LIMITE = 50
MULTA = 4.0

excesso = 0.0
peso = raw_input("Digite o peso dos peixes: ")

if float(peso) > LIMITE:
    excesso = (float(peso) - LIMITE) * MULTA
    print("O valor da multa eh de R$ %.2f " % excesso)
else:
    excesso = 0
    print("Excesso: %.2f" % excesso)

