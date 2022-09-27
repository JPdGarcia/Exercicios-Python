#Faça um programa que leia 5 números e informe a soma e a média dos números.

soma=0
c=1
while c<=5:
    n = float(input("Digite um numero: "))
    soma = soma+n
    c=c+1

media = soma/5

print("A soma dos numeros digitados é: ", soma)
print("A media dos numeros digitados é: ", media)