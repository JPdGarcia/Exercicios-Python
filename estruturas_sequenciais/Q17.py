#Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
#Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
#comprar apenas latas de 18 litros;
#comprar apenas galões de 3,6 litros;
#misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.


import math


print("Bem vindo a loja de tinta online do senhor Zé!")
metrosStr = input("Qual a area a ser pintada? ")
metros= float(metrosStr)

litros = metros/6
latas = litros/18
latasReal = math.ceil(latas)
pLatas = latasReal*80

galoes = litros/3.6
galoesReal = math.ceil(galoes)
pGaloes = galoesReal*25

litrosFolga = litros* 1.1
latasFinal = litrosFolga//18
resto = litrosFolga%18
galoesMaior = resto/3.6
galoesFinal = math.ceil(galoesMaior)

precoFinal = latasFinal*80 + galoesFinal*25

print("______________________________________________________________________________________________________________")
print("Comprando apenas latas de tinda de 18L você precisara de ", latasReal, "latas ","e isso vai custar: R$", pLatas)
print("______________________________________________________________________________________________________________")
print("Comprando apenas galões de 3,6L você precisara de ", galoesReal,"galões", "e isso vai custar: R$", pGaloes )
print("______________________________________________________________________________________________________________")
print("Comprando latas e galões a melhor composição é: ", latasFinal, "latas e ", galoesFinal, "galões e isso vai custar R$", precoFinal)