#Faça um Programa que leia 20 números inteiros e armazene-os num vetor. Armazene os números pares no vetor PAR e os números IMPARES no vetor impar. Imprima os três vetores.

lista = []
for c in range(20):
    n = int(input("Digite um numero: "))
    lista.append(n)


par = []
impar = []
n=0

for i in range(20):
    if (lista[n]%2 == 0):
        itempar = lista.pop(n)
        par.append(itempar)
        lista.append(itempar)

    elif (lista[n]%2 != 0):
        itemimpar = lista.pop(n)
        impar.append(itemimpar)
        lista.append(itemimpar)


print(lista)
print(par)
print(impar)