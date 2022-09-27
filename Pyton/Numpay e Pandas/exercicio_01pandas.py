#1. Crie um data frame pandas com 1000 amostras em cada uma das seguintes colunas:
   # - Idade: números inteiros aleatórios entre 0 e 100 (inclusos).
   # - Nota: Números decimais entre 0 e 1000.
   # -  Sexo: Valores aleatórios de M ou F
   # -  Estado: Valores aleatórios entre os estados do Brasil.


from secrets import choice
import numpy as np
import random
import pandas as pd

estado = [
    'AC','AL','AP','AM','BA','CE',
    'ES','GO','MA','MT','MS','MG',
    'PA','PB','PR','PE','PI','RJ',
    'RN','RS','RO','RR','SC','SP',
    'SE','TO','DF'
]

tabela = pd.DataFrame({
    'idade': np.random.randint(0,101,1000),
    'nota': np.random.rand(1000) * 1000,
    'sexo': np.random.choice(['M', 'F'],1000),
    'estado': np.random.choice(estado,1000)
})
print(tabela)


 #2. Utilizando pandas, realize as seguintes alterações no dataset:
   # - Transforme 20% das notas em valores nulos(None), simulando alunos que não compareceram à prova.
   # -  Preencha as notas nulas com valor 0, simulando uma atribuição automática do sistema.
    #df = df.fillna(0)


alunosFaltantes = tabela.sample(frac=.2, random_state=0).index
tabela.loc[alunosFaltantes, 'nota'] = None
tabela = tabela.fillna(0)
print(tabela)



#3. Remova alunos com idades inferiores a 18 e superiores a 80, simulando uma filtragem automática do sistema para alunos com idades incosistentes.'''

removidosIdade18 = tabela['idade'] < 18
removidosIdade80 = tabela['idade'] > 80
filtro = ~(removidosIdade18 | removidosIdade80)
tabela = tabela[filtro]
print(tabela)


#4. Crie um novo campo de aprovado para os alunos restantes que obtiveram nota igual ou superior a 600, com o valor 'Aprovado'. Simulando uma correção automática.

aprovados = tabela['nota'] >600

tabela['aprovados'] = None
tabela.loc[aprovados, 'aprovados'] = 'Aprovado'

print(tabela)

#5. Preencha o resto do campo de aprovado com 'Reprovado' para os demais alunos (preenchimento de nulo).
   #df = df[coluna].fillna('Reprovado')

tabela['aprovados'] = tabela['aprovados'].fillna('Reprovados')

print(tabela)

#6. Mostre a quantidade de alunos aprovados e reprovados.
#quantAprovados = tabela.loc['Aprovados','aprovados']
#quantReprovados = tabela.loc['Reprovados' , 'aprovados']

print(tabela['aprovados'].value_counts())

tabela.to_csv('resultado_enem.csv')
