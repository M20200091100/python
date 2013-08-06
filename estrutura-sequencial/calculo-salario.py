# -*- coding: latin1 -*-
#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.
salario_hora = raw_input("Digite o quanto voce ganha por hora: ")
horas_mensais = raw_input("Digite a quantidade de horas que voce trabalha por mes: ")

salario = float(salario_hora) * float(horas_mensais)

print("Voce ganha R$ %.2f por mes" % salario)

