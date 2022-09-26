#Faça um Programa que leia um vetor de 5 números inteiros e mostre-os.


lista = []

c = 1
while c<=5:
    n = int(input("Digite um valor: "))
    lista.append(n)
    c= c+1

print(lista)
