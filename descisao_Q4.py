#Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

letra = input("Digite uma letra do alfabeto: ")

if(letra.lower() == "a" or letra.lower()=="e" or letra.lower()=="i" or letra.lower()=="o" or letra.lower()=="u"):
    print("A letra digitada é uma vogal")
else:
    print("A letra digitada é uma consoante")