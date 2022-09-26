#Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais. Valide a entrada e permita repetir a operação.


pA= int(input("Digite a população do primeiro pais: "))
pB= int(input("Digite a população do segundo pais: "))
tA = float(input("Digite a tacha de crecimento do primeiro pais em porcentagem: "))
tB = float(input("Digite a tacha de crecimento do segundo pais em porcentagem: "))

tA= tA/100
tB= tB/100
ano=0

while not pA>=pB:
    pA = pA+pA*tA
    pB = pB+pB*tB
    ano =ano+1

print(pA)
print(pB)
print(ano)