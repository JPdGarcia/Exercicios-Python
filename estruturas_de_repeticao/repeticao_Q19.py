#Altere o programa anterior para que ele aceite apenas números entre 0 e 1000.


n= int(input("Digite o tamanho do seu conjunto de numeros: "))
maior = 0
c=1
while c<=n:
    numero = int(input("Digite um numero: "))
    while not 0< numero <1000:
        print("Numero invalido, digite um numero entre 0 e 1000")
        numero = int(input("Digite um numero: "))
        

    if numero>maior:
        maior = numero
    c=c+1
print("O maior numero da sequencia é: ",maior)