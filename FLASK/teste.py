import pandas as pd

parar = 's'
df = pd.read_csv('C:/Users/jop_garcia/Documents/Gama/FLASK/teste.csv', index_col=['produtos'])
print(df)
while parar == 's':
    produto = input('Digite o nome do produto: ')
    quantidade = input('Digite a quantida: ')
    preço = input('Digite o preço do produto: ')

    df.loc[produto] = [quantidade,preço]

    print(df)
    df.to_csv('C:/Users/jop_garcia/Documents/Gama/FLASK/teste.csv')
    parar = input('continuar? ')