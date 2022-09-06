#Altere o programa de cálculo do fatorial, permitindo ao usuário calcular o fatorial várias vezes e limitando o fatorial a números inteiros positivos e menores que 16.



repetir = "S"
while repetir.upper() == "S":

    n= int(input("Digite qual numero você quer saber o fatorial: "))
    while not (n >0 and n <16):
        print("numero invalido, digite um numero entre 0 e 16")
        n= int(input("Digite qual numero você quer saber o fatorial: "))

    n1 = 1
    n2 = 1
    c = 1
    while c<=n:
        n1=n1*n2
        c=c+1
        n2=n2+1
    print("o resultado de",n,"! é:",n1)

    repetir = input("Quer fazer o fatorial de outro numero? S para sim, N para não: ")
print("Fim de programa!")
