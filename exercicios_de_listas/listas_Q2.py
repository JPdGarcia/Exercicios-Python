#Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.

lista = []

c = 1
while c<=10:
    n = int(input("Digite um valor: "))
    lista.append(n)
    c= c+1
lista.reverse()
print(lista)