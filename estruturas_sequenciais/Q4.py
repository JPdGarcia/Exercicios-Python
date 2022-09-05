#Faça um Programa que peça as 4 notas bimestrais e mostre a média.

print("Vamos calcular sua media anual")
n1 = input("Digite sua primeira nota ")
n2 = input("Digite sua segunda nota ")
n3 = input("Digite sua terceira nota ")
n4 = input("Digite sua quarta nota ")

numero1 = float(n1)
numero2 = float(n2)
numero3 = float(n3)
numero4 = float(n4)

media = ((numero1 + numero2 + numero3 + numero4)/4)

print("***************************")
print("Sua media anual é: ", media)
print("***************************")
