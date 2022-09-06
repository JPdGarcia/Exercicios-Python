#Faça um programa que, dado um conjunto de N números, determine o menor valor, o maior valor e a soma dos valores.


n= int(input("Digite o tamanho do seu conjunto de numeros: "))
maior = 0
c=1
while c<=n:
    numero = int(input("Digite um numero: "))
    if numero>maior:
        maior = numero
    c=c+1
print("O maior numero da sequencia é: ",maior)