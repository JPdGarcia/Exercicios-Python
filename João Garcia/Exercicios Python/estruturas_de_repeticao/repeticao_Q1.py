#Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.

n=1
while 0<=n<=10:
    n = float(input("digite uma nota entre 0 e 10: "))

    if(0<=n<=10):
        print("Valor valido")
    else:
        print("Valor invalido")
print("fim de programa")