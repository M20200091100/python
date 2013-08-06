# -*- coding: latin1 -*-
#Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal, usando a seguinte fórmula: (72.7*altura) - 58

altura = raw_input("Digite tua altura: ")

peso_ideal = (72.7 * float(altura)) - 58

print("Teu peso ideal eh %.2f kg" % peso_ideal)

