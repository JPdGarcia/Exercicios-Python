#Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:

n1 = float(input("Digite sua primeira nota: "))
n2 = float(input("Digite sua segunda nota:"))

media = (n1+n2)/2

if(media<4):
    print("Sua nota foi:",media,"conceio E REPROVADO")
elif(media<6):
    print("Sua nota foi:",media,"conceio D REPROVADO")
elif(media<7.5):
    print("Sua nota foi:",media,"conceio C APROVADO")
elif(media<9):
    print("Sua nota foi:",media,"conceio B APROVADO")
elif(media<10):
    print("Sua nota foi:",media,"conceio A APROVADO")