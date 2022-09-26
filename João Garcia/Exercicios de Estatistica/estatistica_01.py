#Calcule:

#Dados Numéricos
#A Moda
#A Mediana
#A média
#Os Quartis
#Os 10% maiores
#Os 5 % Menores
#O valor máximo
#O valor mínimo

import pandas as pd

df = pd.read_csv('João Garcia\Exercicios de Estatistica\Estatistica_gama.csv', decimal=",")


print(f'''
A moda é: 
    Nome: {df['Nome'].mode()[0]}
    Idade: {df['Idade'].mode()[0]}
    Filhos: {df['Filhos'].mode()[0]}
    Estado: {df['Estado'].mode()[0]}
    Altura: {df['Altura'].mode()[0]}
    Formação: {df['Formacao'].mode()[0]}
''')


print(f'''
A mediana é: 
    Idade: {df['Idade'].median()}
    Filhos: {df['Filhos'].median()}
    Altura: {df['Altura'].median()}
''')

print(f'''
A media é: 
    Idade: {df['Idade'].mean()}
    Filhos: {df['Filhos'].mean()}
    Altura: {df['Altura'].mean()}
''')

print(f'''
os quartis de 25% são: 
    Idade: {df['Idade'].quantile(.25)}
    Filhos: {df['Filhos'].quantile(.25)}
    Altura: {df['Altura'].quantile(.25)}
''')

print(f'''
os quartis de 50% são: 
    Idade: {df['Idade'].quantile(.5)}
    Filhos: {df['Filhos'].quantile(.5)}
    Altura: {df['Altura'].quantile(.5)}
''')

print(f'''
os quartis de 75% são: 
    Idade: {df['Idade'].quantile(.75)}
    Filhos: {df['Filhos'].quantile(.75)}
    Altura: {df['Altura'].quantile(.75)}
''')

print(f'''
os 10 maiores valores são: 
    Idade: {df['Idade'].nlargest(11)}
    Filhos: {df['Filhos'].nlargest(11)}
    Altura: {df['Altura'].nlargest(11)}
''')

print(f'''
os 5 menores valores são: 
    Idade: {df['Idade'].nsmallest(6)}
    Filhos: {df['Filhos'].nsmallest(6)}
    Altura: {df['Altura'].nsmallest(6)}
''')

print(f'''
o Maior valor é: 
    Idade: {df['Idade'].max()}
    Filhos: {df['Filhos'].max()}
    Altura: {df['Altura'].max()}
''')

print(f'''
o Menor valor é: 
    Idade: {df['Idade'].min()}
    Filhos: {df['Filhos'].min()}
    Altura: {df['Altura'].min()}
''')

#Dados de Texto
#A frequência absoluta
#A frequência relativa
#A Moda
#Qual o tipo de Moda?
#O valor máximo (ordem alfabética)
#O valor mínimo (ordem alfabética)

print(f'''
A frequencia Absoluta é:
    Nomes: {df['Nome'].value_counts()}
    Estado: {df['Estado'].value_counts()}
    Formação: {df['Formacao'].value_counts()}
''')

print(f'''
A frequencia Relativa é:
    Nomes: {(df['Nome'].value_counts())/len(df)}
    Estado: {(df['Estado'].value_counts())/len(df)}
    Formação: {(df['Formacao'].value_counts())/len(df)}
''')

print(f'''
A ordem Alfabetica é:
    Nomes: {df['Nome'].sort_values()}
    Estado: {df['Estado'].sort_values()}
    Formação: {df['Formacao'].sort_values()}
''')