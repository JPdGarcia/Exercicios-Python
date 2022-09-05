#Faça um programa que receba dois números inteiros e gere os números inteiros que estão no intervalo compreendido por eles.


n1= int(input("Digite o primeiro numero: "))
n2= int(input("Digite o segundo numero: "))

n1 = n1+1
while n1<n2:
    print(n1)
    n1=n1+1