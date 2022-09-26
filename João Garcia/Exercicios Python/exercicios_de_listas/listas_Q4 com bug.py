#Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as consoantes.

lista = []
for c in range(3):
    letra = input("Digite um caracter: ")
    lista.append(letra)

n=0
for i in range(3):
    if not lista[n] in "aeiou":
        print(lista[n])
        n=n+1
