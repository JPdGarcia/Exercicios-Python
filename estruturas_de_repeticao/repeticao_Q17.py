#Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120

n= int(input("Digite qual numero você quer saber o fatorial: "))

n1 = 1
n2 = 1
c = 1
while c<=n:
    n1=n1*n2
    c=c+1
    n2=n2+1
print("o resultado de",n,"! é:",n1)