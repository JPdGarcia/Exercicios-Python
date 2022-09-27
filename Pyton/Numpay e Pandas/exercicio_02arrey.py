#Crie um array de duas dimensões, no formato 9x9, com números de 0 a 80 ordenados de modo crescente e selecione:
#  1. Os números ímpares
#  2. Os números pares
#  3. Os múltiplos de sete
#  4. Os múltiplos de 10
#  5. Os números 32,33,42,43

import numpy as np

tabela = np.arange(0,81).reshape([9,9])
print(tabela)
print('__________________________________________')

filtroImpar = tabela %2 == 1
print(tabela[filtroImpar])
print('__________________________________________')

filtroPar = tabela %2 == 0 
print(tabela[filtroPar])
print('__________________________________________')

filtro7 = tabela %7 == 0 
print(tabela[filtro7])
print('__________________________________________')

filtro10 = tabela %10 == 0 
print(tabela[filtro10])
print('__________________________________________')

print (tabela[3,5],tabela[3,6],tabela[4,6],tabela[4,7])