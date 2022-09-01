#Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
#Para homens: (72.7*h) - 58
#Para mulheres: (62.1*h) - 44.7


print("Vamos calcular o seu peso ideal usando a sua altura")
genero = input("digite h se você for homem e m se você mulher ")

alturaStr = input("Qual a sua altura em metros? ")

altura = float(alturaStr)

if(genero == "h" ):
    peso = (72.7*altura) - 58
    print("Seu peso ideal é: ", peso)
else:
    peso = (62.1*altura) - 44.7
    print("Seu peso ideal é: ", peso)
