# Dicionário

agenda = {
  'nome': 'Ana',
  'idade': 44,
  'telefone': '9999-9999',
  'lista': [1, 2, 3]
}

agenda1 = dict(nome='Flávia', idade=42, telefone='9999-9999', lista=[1, 2, 3])

print(agenda)

print(agenda1)

# Acessando valores
print(agenda['nome'])

# Alterando valores
agenda['nome'] = 'Ana Cristina'
print(agenda['nome'])

# Adicionando valores
agenda['endereco'] = 'Rua dos Bobos'
print(agenda)

# Removendo valores
del agenda['endereco']
print(agenda)

# Deletando um dicionário
del agenda1

# Pop
lista = agenda.pop('lista')
print(agenda)
print(lista)

# Iterando um dicionário
# Iterando as chaves
for key in agenda.keys():
  print(key)

# Iterando os valores
for value in agenda.values():
  print(value)

# Iterando as chaves e os valores
for key, value in agenda.items():
  print(key, value)

# Copiando um dicionário
agenda2 = agenda.copy()
print(agenda2)

# Limpar um dicionário
agenda.clear()
print(agenda)

# Update()
carro = {
  'marca': 'Fiat',
  'modelo': 'Fiorino',
  'ano': 2015
}

carro.update(ano=2018)
print(carro)

atualizacao = {
  'modelo': 'Palio',
  'ano': 2019
}

carro.update(atualizacao)
print(carro)
