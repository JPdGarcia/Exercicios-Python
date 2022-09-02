#Faça um Programa que leia três números e mostre o maior deles.

numero1 = float(input("digite o primeiro numero: "))
numero2 = float(input("digite o segundo numero: "))
numero3 = float(input("digite o terceiro numero: "))

if(numero1>numero2 and numero1>numero3):
    print("O numero", numero1,"foi o maior numero digitado, esse foi o primeiro numero digitado")
elif(numero2>numero1 and numero2>numero3):
    print("O numero", numero2,"foi o maior numero digitado, esse foi o segundo numero digitado")
elif(numero3>numero1 and numero3>numero2):
    print("O numero", numero3,"foi o maior numero digitado, esse foi o terceiro numero digitado")
else:
    print("erro: o seu maior numero é igual a outro")
