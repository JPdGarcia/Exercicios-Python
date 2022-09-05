#Faça um programa que leia e valide as seguintes informações:
#Nome: maior que 3 caracteres;
#Idade: entre 0 e 150;
#Salário: maior que zero;
#Sexo: 'f' ou 'm';
#Estado Civil: 's', 'c', 'v', 'd';


from re import S


nome = input("Digite seu nome:")
while len(nome) <=3 :
    print("Nome invalido")
    nome = input("Digite seu nome com mais de 3 caracteres:")
    

idade = int(input("digite sua idade: "))
while not 0<idade<150:
    print("Numero invalido!")
    idade = int(input("Digite sua idade: "))

salario= float(input("Digite seu salario: "))
while not salario>0:
    print("Salario invalido")
    salario = float(input("Digite seu salario: "))

sexo= input("Digite seu sexo, M para masculido e F para feminino: ")
while not sexo.upper() in "MF":
    print("Sexo ivalido!")
    sexo= input("Digite seu sexo, M para masculido e F para feminino: ")

estado = input("Digite seu estado civil S para solteiro, C para casado, V para viuvo, D para divorciado: ")
while not estado.upper() in "SCVD":
    print("Estado civil não valido!")
    estado = input("Digite seu estado civil S para solteiro, C para casado, V para viuvo, D para divorciado: ")

print("fim do programa!")