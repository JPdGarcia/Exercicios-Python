# 3. Na programação é comum relacionar dados usando um campo que identifica
# registros (id). Elabore uma modelagem de dados em que os registros estão
# relacionados através de um campo identificador (o id), atendendo as seguintes
# afirmações:

# ○ O bairro Betânia é da cidade Diamantina.
# ○ Os bairros Agostinho e Natal são da cidade Noronha.
# ○ A cidade Diamantina é do estado Goiás.
# ○ A cidade Noronha é do estado Paraná.

import random


# id estados
id_goias = random.randint(0, 99)
id_parana = random.randint(0, 99)

#id cidades
id_diamantina = random.randint(0, 99)
id_noronha = random.randint(0, 99)

#id bairros
id_betania = random.randint(0, 99)
id_agostinho = random.randint(0, 99)
id_natal = random.randint(0, 99)

estados = [{'id':id_goias, 'Nome':'Goiás'},
{'id':id_parana, 'Nome':'Parana'}]

cidades = [{'id':id_diamantina, 'Nome':'Diamantina', 'Estado_id': id_goias},
{'id':id_parana, 'Nome':'Norinha', 'Estado_id': id_parana }]

bairros = [{'id':id_betania, 'Nome':'Betânia', 'Cidade_id': id_diamantina, 'Estado_id': id_goias},
{'id':id_agostinho, 'Nome':'Agostinho','Cidade_id': id_noronha, 'Estado_id': id_parana },
{'id':id_natal, 'Nome':'Natal','Cidade_id': id_noronha, 'Estado_id': id_parana }]


print(f'Estados: {estados}')
print('---------------------')
print(f'Cidades: {cidades}')
print('---------------------')
print(f'Bairros: {bairros}')



