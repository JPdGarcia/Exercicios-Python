#Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene num vetor a média de cada aluno, imprima o número de alunos com média maior ou igual a 7.0.

soma = 0
n = 0
aprovados = 0

lista = []

for i in range(10):
    for c in range(4):
        nota = float(input("Digite uma nota: "))
        soma = soma + nota
    media = soma/4
    lista.append(media)
    soma = 0
    print(lista)

print("media dos alunos é: ",lista)


for contador in range(10):
    if lista[n] >=7:
        aprovados = aprovados + 1
        n = n+1

print(aprovados, "Alunos foram aprovados!")