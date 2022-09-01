#Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal, usando a seguinte fórmula: (72.7*altura) - 58


print("Vamos calcular o seu peso ideal usando a sua altura")
alturaStr = input("Qual a sua altura?")

altura = float(alturaStr)

peso = (72.7*altura) - 58

print("O seu peso ideal é: ", peso)