# 4. Crie duas funções:
# ○ A primeira função receberá dois parâmetros e retornará como resultado uma
# concatenação de texto colocando uma vírgula entre os dois parâmetros ao
# uní-los.
# ○ A segunda função não receberá parâmetros; será feito a leitura de duas
# entradas que o usuário digitar; irá chamar a primeira função passando como
# argumento os dois textos lidos; por fim esta segunda função irá imprimir para
# o usuário informando qual foi o resultado que se obteve na chamada à
# primeira função.
# ○ Exemplo da primeira entrada: “Olá”. Exemplo da segunda entrada: “Mundo”.
# Exemplo da saída do sistema: “Olá,Mundo”.


def funcao1(parametro1, parametro2):
    return print(f'{parametro1}, {parametro2}')

def funcao2():
    parametro1 = input('Digite o primeiro parametro: ')
    parametro2 = input('Digite o segundo parametro: ')
    concatenação = funcao1(parametro1, parametro2)

    return concatenação

funcao2()

