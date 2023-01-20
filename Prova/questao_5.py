# 5. Escreva a função obter_colecao_mongodb(url_conexao, colecao) que irá se
# conectar no MogodDB utilizando alguma biblioteca do Python. Ela possui os
# seguintes parâmetros:
# ○ url_conexao: URI de conexão com banco de dados MongoDB, que também
# informa a base de dados (database). Por exemplo: a URI
# `mongodb://localhost/bancoexemplo', é a string de conexão para o banco
# "bancoexemplo" da minha máquina local ("localhost").
# ○ colecao: É o nome da coleção (collection) do MongoDB que estaremos
# acessando com esta função.



from pymongo import MongoClient

url_connection = "mongodb://localhost/bancoexemplo"
collection = "bancoexemplo"

def obter_colecao_mongodb(url_connection, collection):
    client = MongoClient(url_connection)
    db = client.get_default_database()
    return db[collection]

obter_colecao_mongodb()