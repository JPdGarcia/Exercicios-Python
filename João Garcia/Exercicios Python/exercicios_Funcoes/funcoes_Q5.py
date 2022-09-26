#Faça um programa com uma função chamada somaImposto. A função possui dois parâmetros formais: taxaImposto, que é a quantia de imposto sobre vendas expressa em porcentagem e custo, que é o custo de um item antes do imposto. A função “altera” o valor de custo para incluir o imposto sobre vendas.


def somaImporto(taxaImposto,custo):
    taxaImposto = taxaImposto/100 + 1
    valorFinal = taxaImposto * custo
    return(valorFinal)

n1 = float(input('digite a taxa de imposto do produto em porcentagem: '))
n2 = float(input('Digite o custo do produto: '))

resultado = somaImporto(n1,n2)
print(f'O valor final do produto é: R${resultado}')