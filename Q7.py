#Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.

print("Vamos calcular o dobro da area de um quadrado")
bStri = input("Digite a base desse quadrado em metros ")
hStri = input("Digite a altura desse quadrado em metros ")

base = float(bStri)
altura = float(hStri)

area = base * altura
dobroArea = area*2

print("O dobro da area do quadrado desejado é:", dobroArea)