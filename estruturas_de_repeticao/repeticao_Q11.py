#Altere o programa anterior para mostrar no final a soma dos números.


n1= int(input("Digite o primeiro numero: "))
n2= int(input("Digite o segundo numero: "))

n1 = n1+1
soma = 0
while n1<n2:
    print(n1)
    soma=soma+n1
    n1=n1+1
print(soma)