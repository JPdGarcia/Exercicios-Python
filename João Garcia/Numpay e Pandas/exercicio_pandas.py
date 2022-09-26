import pandas as pd

ingredientes = [
    'maisena',
    'farinha',
    'açucar',
    'ovos',
    'manteiga',
    'castanhas'
]

serie = pd.Series(ingredientes, name='ingredientes', dtype=object)
serie

# %% Criação da série de quantidades
qtd = [
    200,
    250,
    100,
    2,
    150,
    180
]






'''1. Crie um data frame pandas com 1000 amostras em cada uma das seguintes colunas:
   1. Idade: números inteiros aleatórios entre 0 e 100 (inclusos).
   2. Nota: Números decimais entre 0 e 1000.
   3. Sexo: Valores aleatórios de M ou F
   4. Estado: Valores aleatórios entre os estados do Brasil.'''




''' 2. Utilizando pandas, realize as seguintes alterações no dataset:
   1. Transforme 20% das notas em valores nulos(None), simulando alunos que não compareceram à prova.
   2. Preencha as notas nulas com valor 0, simulando uma atribuição automática do sistema.
     `df = df.fillna(0)`
3. Remova alunos com idades inferiores a 18 e superiores a 80, simulando uma filtragem automática do sistema para alunos com idades incosistentes.'''



''' 4. Crie um novo campo de aprovado para os alunos restantes que obtiveram nota igual ou superior a 600, com o valor 'Aprovado'. Simulando uma correção automática.
   5. Preencha o resto do campo de aprovado com 'Reprovado' para os demais alunos (preenchimento de nulo).
   `df = df[coluna].fillna('Reprovado')`
   6. Mostre a quantidade de alunos aprovados e reprovados.'''




# %%
