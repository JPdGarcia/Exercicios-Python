#Faça um programa que converta da notação de 24 horas para a notação de 12 horas. Por exemplo, o programa deve converter 14:25 em 2:25 P.M. A entrada é dada em dois inteiros. Deve haver pelo menos duas funções: uma para fazer a conversão e uma para a saída. Registre a informação A.M./P.M. como um valor ‘A’ para A.M. e ‘P’ para P.M. Assim, a função para efetuar as conversões terá um parâmetro formal para registrar se é A.M. ou P.M. Inclua um loop que permita que o usuário repita esse cálculo para novos valores de entrada todas as vezes que desejar.



turno = ' '


def converter(hora,minutos):
    if hora <=12:
        return str(hora) + ':' + str(minutos)
    elif hora == 0:
        return str(12) + ':' + str(minutos)
    else:
        return str(hora-12) + ':' + str(minutos)

def converteTurno(hora):
    if hora >= 12:
        return 'P'
    else:
        return 'A'

def saida(turno):
    if turno == 'A':
        return 'A.M.'
    else:
        return 'P.M.'

opcao = ' '
while opcao != 's':
    