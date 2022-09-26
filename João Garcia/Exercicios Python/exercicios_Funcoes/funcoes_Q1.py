#Faça um programa para imprimir:
#    1
#    2   2
#    3   3   3
#    .....
#    n   n   n   n   n   n  ... n
#para um n informado pelo usuário. Use uma função que receba um valor n inteiro e imprima até a n-ésima linha.

def questao1(numero):
    for contador in range(1,numero +1):
        print((str(contador)+' ')* contador)

numero = int(input("Digite um numero: "))
questao1(numero)

