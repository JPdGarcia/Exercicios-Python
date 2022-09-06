#A série de Fibonacci é formada pela seqüência 0,1,1,2,3,5,8,13,21,34,55,... Faça um programa que gere a série até que o valor seja maior que 500.


n1 = 1
n2 = 0
c = 1
print(n2)
print(n1)

while n1<500:
    n1=n1+n2
    print(n1)
    c=c+1
    n2=n1-n2