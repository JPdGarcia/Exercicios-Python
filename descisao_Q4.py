#Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

letra = input("Digite uma letra do alfabeto: ")

if(letra in "aeiou"):
    print("A letra digitada é uma vogal")
else:
    print("A letra digitada é uma consoante")