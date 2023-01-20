
from pymongo import MongoClient
from pprint import pprint
import pandas as pd

cliente = MongoClient('mongodb+srv://gama:gama1234@cluster0.rn9t8ag.mongodb.net/gama')
db = cliente['gama']

# Consulta
cursor = db.alunos.find({})
resultado = list(cursor)
pprint(resultado)

# pandas 
df = pd.DataFrame(resultado).set_index('_id')
print(df)

#arquivo
df.to_json('mongo.json', orient='records')