# -*- coding: latin1 -*-
"""Tendo como dados de entrada a altura e o sexo de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
        1. Para homens: (72.7*h) - 58
        2. Para mulheres: (62.1*h) - 44.7 (h = altura)
        3. Peça o peso da pessoa e informe se ela está dentro, acima ou abaixo do peso."""

sexo = raw_input("Qual teu sexo? Masculino (M) ou Feminino (F)? ")
altura = raw_input("Digite tua altura: ")

peso_ideal_m = (72.7 * float(altura)) - 58
peso_ideal_f = (62.1 * float(altura)) - 44.7

if sexo == "M":
    print("Teu peso ideal eh %.2f: " % peso_ideal_m)
elif sexo == "F":
    print("Teu peso ideal eh %.2f: " % peso_ideal_f)
else:
    print("Sexo invalido!")

