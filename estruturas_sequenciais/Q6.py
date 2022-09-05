#Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.

import math


print("Vamos calcular a area de um circulo")
raioStr = input("Informe o raio do circulo desejado ")

raio = float(raioStr)
pi = math.pi
area = (pi*(raio**2))

print("A area do circulo desejado é: ", area,"m")