#As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver o programa que calculará os reajustes.
#Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
#salários até R$ 280,00 (incluindo) : aumento de 20%
#salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
#salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
#salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
#o salário antes do reajuste;
#o percentual de aumento aplicado;
#o valor do aumento;
#o novo salário, após o aumento.


salario = float(input("Digite seu salario por favor: "))

if(salario<=280):
    nS = salario*1.20
    aumento= nS - salario
    print("seu salario era de:",salario,"teve um aumento de:", aumento, "que é 20% do seu salario anterior. Seu novo salario é:", nS)

elif(280<salario<700):
    nS = salario*1.15
    aumento= nS - salario
    print("seu salario era de:",salario,"teve um aumento de:", aumento, "que é 15% do seu salario anterior. Seu novo salario é:", nS)
    
elif(700<salario<1500):
    nS = salario*1.1
    aumento= nS - salario
    print("seu salario era de:",salario,"teve um aumento de:", aumento, "que é 10% do seu salario anterior. Seu novo salario é:", nS)

elif(salario>1500):
    nS = salario*1.05
    aumento= nS - salario
    print("seu salario era de:",salario,"teve um aumento de:", aumento, "que é 5% do seu salario anterior. Seu novo salario é:", nS)
else:
    print("Valor invalido")