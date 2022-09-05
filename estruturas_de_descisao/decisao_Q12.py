#Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto, mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto menos os descontos. O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
#Desconto do IR:
#Salário Bruto até 900 (inclusive) - isento
#Salário Bruto até 1500 (inclusive) - desconto de 5%
#Salário Bruto até 2500 (inclusive) - desconto de 10%
#Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações, dispostas conforme o exemplo abaixo. No exemplo o valor da hora é 5 e a quantidade de hora é 220.


print("Vamos calcumar o seu salario mensal ")
porHora = float(input("Quanto você ganha por hora trabalhada? "))
horas = float(input("Quantas horas você trabalha por mês? "))

salario = porHora*horas

if(salario<900):
    ir = "Isento"
    inss = salario*0.10
    sindicato = salario*0.03
    fgts = salario*0.11
    liquido = salario-inss-sindicato
    
    print("------------------------------------------------")
    print("Salário Bruto: (",porHora,"*",horas,"):",salario)
    print("(-) IR (Isento): R$",ir)
    print("(-) INSS ( 10%): R$",inss)
    print("FGTS (11%): R$",fgts)
    print("Total de descontos: R$:",inss+sindicato)
    print("Salário Liquido: R$",liquido)

elif(salario<1500):
    ir = salario*0.05
    inss = salario*0.10
    sindicato = salario*0.03
    fgts = salario*0.11
    liquido = salario-ir-inss-sindicato
    
    print("------------------------------------------------")
    print("Salário Bruto: (",porHora,"*",horas,"):",salario)
    print("(-) IR (Isento): R$",ir)
    print("(-) INSS ( 10%): R$",inss)
    print("FGTS (11%): R$",fgts)
    print("Total de descontos: R$:",ir+inss+sindicato)
    print("Salário Liquido: R$",liquido)

elif(salario<2500):
    ir = salario*0.1
    inss = salario*0.10
    sindicato = salario*0.03
    fgts = salario*0.11
    liquido = salario-ir-inss-sindicato
    
    print("------------------------------------------------")
    print("Salário Bruto: (",porHora,"*",horas,"):",salario)
    print("(-) IR (Isento): R$",ir)
    print("(-) INSS ( 10%): R$",inss)
    print("FGTS (11%): R$",fgts)
    print("Total de descontos: R$:",ir+inss+sindicato)
    print("Salário Liquido: R$",liquido)

elif(salario>2500):
    ir = salario*0.2
    inss = salario*0.10
    sindicato = salario*0.03
    fgts = salario*0.11
    liquido = salario-ir-inss-sindicato
    
    print("------------------------------------------------")
    print("Salário Bruto: (",porHora,"*",horas,"):",salario)
    print("(-) IR (Isento): R$",ir)
    print("(-) INSS ( 10%): R$",inss)
    print("FGTS (11%): R$",fgts)
    print("Total de descontos: R$:",ir+inss+sindicato)
    print("Salário Liquido: R$",liquido)