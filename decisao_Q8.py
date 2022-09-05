#Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.

p1 = float(input("digite o primeiro produto: "))
p2 = float(input("digite o segundo produto: "))
p3 = float(input("digite o terceiro produto: "))

if(p1<p2 and p1<p3):
    print("O primeiro produto que custa: R$", p1,"é o mais barato")
elif(p2<p1 and p2<p3):
    print("O segundo produto que custa: R$", p2,"é o mais barato")
elif(p3<p1 and p3<p2):
    print("O terceiro produto que custa: R$", p3,"é o mais barato")
else:
    print("erro: o seu maior numero é igual a outro")
