#1. Crie um array 6x6 preenchido com zero
#   2. Preencha o centro desse array com um array 4x4 preenchido com uns
#   3. Preencha o centro desse array com um array 2x2 preenchido com dois
#   4. Gere um segundo array 6x6 com números inteiros aleatórios entre 0 e 2.
#   5. Subtraia o primeiro array pelo segundo

import numpy as np

tabela = np.zeros([6,6])
print(tabela)
print('_____________________')
tabela[1:5,1:5] = 1
print(tabela)
print('_____________________')
tabela[2:4,2:4] = 2
print(tabela)
print('_____________________')
tabela2 = np.random.randint(0,3,[6,6])
print(tabela2)
print('_____________________')
print(tabela-tabela2)

tabela3=np.arange(1,29). reshape([4,7])
print(tabela3)