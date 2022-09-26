#Faça um programa, com uma função que necessite de um argumento. A função retorna o valor de caractere ‘P’, se seu argumento for positivo, e ‘N’, se seu argumento for zero ou negativo.



def questao4(n):
    if n>0:
        return("P")
    else:
        return("N")

n = float(input("Digite um numero: "))
resultado = questao4(n)
print(resultado)
