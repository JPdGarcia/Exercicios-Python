#Faça um programa que peça dois números, base e expoente, calcule e mostre o primeiro número elevado ao segundo número. Não utilize a função de potência da linguagem.


b=int(input("Digite a base desejada: "))
e=int(input("Digite o espoente desejado: "))
c= 1
p=1
while c<=e:
    p=p*b
    c=c+1
print("resultado da base elevado ao espoente é:",p)
