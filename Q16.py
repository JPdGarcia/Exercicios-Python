#Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.


import math


print("Bem vindo a loja de tinta online do senhor Zé!")
metrosStr = input("Qual a area a ser pintada? ")
metros= float(metrosStr)

litros = metros/3
latas = litros/18
latasReal = math.ceil(latas)
preco = latasReal*80

print("A quantidade de latas que você precisa é: ", latasReal)
print("Isso vai custar: ", preco)
