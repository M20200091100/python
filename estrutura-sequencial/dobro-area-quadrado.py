# -*- coding: latin1 -*-
#Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.
lado = raw_input("Digite o tamanho do lado do quadrado: ")

area = float(lado) * float(lado)

print("O dobro da area do quadrado eh: %.2f " % float(area * 2))

