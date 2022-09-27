#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.

print("Vamos calcumar o seu salario mensal ")
porHora = input("Quanto você ganha por hora trabalhada? ")
horas = input("Quantas horas você trabalha por mês? ")

valorPorHora = float(porHora)
horasTrabalhadas = float(horas)

salario = valorPorHora*horasTrabalhadas

print("O seu salario é: ", salario)