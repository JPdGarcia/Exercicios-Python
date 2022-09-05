#Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.


usuario = "A"
senha = "A"

while usuario == senha:
    usuario = input("Digite seu usuario: ")
    senha = input("Digite sua senha: ")

    print("Erro!!! sua senha não pode ser igual ao seu usuario")
print("usuario e senhas validos!")
