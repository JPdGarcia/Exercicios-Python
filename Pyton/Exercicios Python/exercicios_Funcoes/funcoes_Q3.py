#Faça um programa, com uma função que necessite de três argumentos, e que forneça a soma desses três argumentos.


def questao3(n1,n2,n3):
    soma = n1+n2+n3
    return(soma)

numero1 = int(input("Digite um numero: "))
numero2 = int(input("Digite um numero: "))
numero3 = int(input("Digite um numero: "))

resultado = questao3(numero1,numero2,numero3)
print(resultado)