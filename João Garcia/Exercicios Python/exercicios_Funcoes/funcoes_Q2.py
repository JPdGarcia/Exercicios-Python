#Faça um programa para imprimir:
#    1
#    1   2
#    1   2   3
#    .....
#    n   n   n   n   n   n  ... n
#para um n informado pelo usuário. Use uma função que receba um valor n inteiro e imprima até a n-ésima linha.

def questao2(numero,linha):
    for contador in range(1,numero +1):
        linha = linha + str(contador) + ' '
        print(linha)


linha = str()
numero = int(input("Digite um numero: "))
questao2(numero,linha)