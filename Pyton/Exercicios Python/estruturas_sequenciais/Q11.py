#Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
#o produto do dobro do primeiro com metade do segundo .
#a soma do triplo do primeiro com o terceiro.
#o terceiro elevado ao cubo.


int1 = input("Digite o primeiro numero inteiro: ")
int2 = input("Digite o segundo numero inteiro: ")
realStr = input("Digite um numero real: ")

inteiro1 = int(int1)
inteiro2 = int(int2)
real = float(realStr)

p1 = (2*inteiro1)*(inteiro2/2)
p2 = (3*inteiro1)+ real
p3 = real**3

print("O produto do dobro do primeiro com metade do segundo é: ", p1)
print("A soma do triplo do primeiro com o terceiro é: ", p2)
print("o terceiro elevado ao cubo é: ", p3)