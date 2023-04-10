# pessoa = {
#     'nome': 'Gustavo',
#     'sexo': 'M',
#     'idade': 37
# }

# print(f'O {pessoa["nome"]} tem {pessoa["idade"]} anos.')
estado = {}
brasil = []
for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy())
print(brasil)

for est in brasil:
    for k, v in est.items():
        print(f'o campo {k} tem valor {v}')

