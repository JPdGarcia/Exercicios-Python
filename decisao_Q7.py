#Faça um Programa que leia três números e mostre o maior e o menor deles.

n1 = float(input("digite o primeiro numero: "))
n2 = float(input("digite o segundo numero: "))
n3 = float(input("digite o terceiro numero: "))

if(n1>n2 and n1>n3 and n2<n3):
    print("O numero", n1,"foi o maior numero digitado e ", n2, "foi o menor " "esses foram o primeiro e o segundo numeros digitados")
elif(n1>n2 and n1>n3 and n3<n2):
    print("O numero", n1,"foi o maior numero digitado e ", n3, "foi o menor " "esses foram o primeiro e o terceiro numeros digitados")

elif(n2>n1 and n2>n3 and n1<n3):
    print("O numero", n2,"foi o maior numero digitado e ", n1, "foi o menor " "esses foram o segundo e o primeiro numeros digitados")
elif(n2>n1 and n2>n3 and n3<n1):
    print("O numero", n2,"foi o maior numero digitado e ", n3, "foi o menor " "esses foram o segundo e o terceiro numeros digitados")

elif(n3>n1 and n3>n2 and n1<n2):
    print("O numero", n3,"foi o maior numero digitado e ", n1, "foi o menor " "esses foram o terceiro e o primeiro numeros digitados")
elif(n3>n1 and n3>n2 and n2<n1):
    print("O numero", n3,"foi o maior numero digitado e ", n2, "foi o menor " "esses foram o terceiro e o segundo numeros digitados")

else:
    print("erro: o seu maior numero é igual a outro")
