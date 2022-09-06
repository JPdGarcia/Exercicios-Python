#A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,... Faça um programa capaz de gerar a série até o n−ésimo termo.

n= int(input("Digite o ponto de parada da sequencia de Fibonacci: "))

n1 = 1
n2 = 0
c = 1
print(n2)
print(n1)

while c<=n:
    n1=n1+n2
    print(n1)
    c=c+1
    n2=n1-n2