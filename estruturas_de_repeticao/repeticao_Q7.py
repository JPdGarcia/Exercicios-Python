#Faça um programa que leia 5 números e informe o maior número.


c = 1
maior = 0
while c<=5:
    n = int(input("Digite um numero: "))
    if(n>maior):
        maior = n
    c=c+1
print("o maior numero digitado foi:",maior)