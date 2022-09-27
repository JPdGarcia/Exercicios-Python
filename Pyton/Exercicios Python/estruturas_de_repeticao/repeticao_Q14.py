#Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números pares e a quantidade de números impares.


c=1
while c<=10:
    n = int(input("Digite um numero:"))
    if n%2==0 :
        print("par")
    else:
        print("impar")
    c=c+1
print("fim")
