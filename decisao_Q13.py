#Faça um Programa que leia um número e exiba o dia correspondente da semana. (1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.

n=int(input("Digite um numero: "))

if(n==2):
    print("2-segunda")
elif(n==3):
    print("3-terça")
elif(n==4):
    print("4-quarta")
elif(n==5):
    print("5-quinta")
elif(n==6):
    print("6-sexta")
elif(n==7):
    print("7-sabado")

else:
    print("valor invalido")
