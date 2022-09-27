#Faça um Programa que leia 4 notas, mostre as notas e a média na tela.

lista=[]
'''c=1
while c<=4:
    n = int(input("Digite um numero: "))
    lista.append(n)
    c=c+1'''

for c in range(4):
    n = int(input("Digite um numero: "))
    lista.append(n)


soma = sum(lista)
media = soma/len(lista)

print(lista)
print(f'A media das notas é {media}')