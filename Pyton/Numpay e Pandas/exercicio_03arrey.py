#Crie um array com três dimensões, onde a primeira dimensão são os dias da semana (seg a dom), a segunda dimensão são as semanas do mês (considere apenas 4 para todos os meses), e a terceira são os meses do ano (Jan a dezembro).
#  1. Marque os finais de semana com a letra W
#  2. Marque o começo do mês com a letra S
#  3. Marque o final do mês com a letra E
#  4. Marque os demais dias com a letra D
#  5. Marque os feriados nacionais com a letra F
#    - 01/01 - Ano novo
#    - 15/04 - Paixão de Cris
#    - 21/04 - Tiradentes
#    - 01/05 - Dia do Trabalho
#    - 07/09 - Independência do Brasil
#    - 12/10 - Nossa Senhora Aparecida
#    - 02/11 - Finados
#    - 15/11 - Proclamação da República
#    - 25/12 - Natal
#PS: o enunciado está com a dimensões invertidas. ;D


import numpy as np


tabela = np.full([12,4,7], "A")
print(tabela)
print('__________________________________________________')

tabela[:,:,0] = "W"
tabela[:,:,6] = "W"
print(tabela)
print('__________________________________________________')

tabela[:,0,0] = "S"
print(tabela)
print('__________________________________________________')

tabela[:,-1,-1] = "E"
print(tabela)
print('__________________________________________________')

tabela[:,:,1] = "D"
tabela[:,:,2] = "D"
tabela[:,:,3] = "D"
tabela[:,:,4] = "D"
tabela[:,:,5] = "D"
print(tabela)
print('__________________________________________________')

tabela[0,0,0] = "F" #- 01/01 - Ano novo
tabela[3,2,0] = "F" #    - 15/04 - Paixão de Cris
tabela[3,2,6] = "F" #    - 21/04 - Tiradentes
tabela[4,0,0] = "F" #    - 01/05 - Dia do Trabalho
tabela[8,0,6] = "F" #    - 07/09 - Independência do Brasil
tabela[9,1,4] = "F" #    - 12/10 - Nossa Senhora Aparecida
tabela[10,0,1] = "F" #    - 02/11 - Finados
tabela[10,2,0] = "F" #    - 15/11 - Proclamação da República
tabela[11,3,2] = "F" #    - 25/12 - Natal

print(tabela)
print('__________________________________________________')
