#Faça um Programa que leia três números e mostre-os em ordem decrescente.

n1 = float(input("digite o primeiro numero: "))
n2 = float(input("digite o segundo numero: "))
n3 = float(input("digite o terceiro numero: "))

if(n1>n2 and n1>n3 and n2>n3):
    print("a orden decrecente é", n1,n2,n3)
elif(n1>n2 and n1>n3 and n3>n2):
    print("a orden decrecente é", n1,n3,n2)

elif(n2>n1 and n2>n3 and n1>n3):
    print("a orden decrecente é", n2,n1,n3)
elif(n2>n1 and n2>n3 and n3>n1):
    print("a orden decrecente é", n2,n3,n1)

elif(n3>n1 and n3>n2 and n1>n2):
    print("a orden decrecente é", n3,n1,n2)
elif(n3>n1 and n3>n2 and n2>n1):
    print("a orden decrecente é", n3,n2,n1)

else:
    print("erro: o seu maior numero é igual a outro")
