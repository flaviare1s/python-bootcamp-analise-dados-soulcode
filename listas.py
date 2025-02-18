lista = ['Fabrício', 37, True, 'amarelo', 1.75, 'amanhã']

print(type(lista))

print(lista)

print(lista[0])

# Quantidade de elementos:
print(len(lista))

# Manipulação de listas:
# Partição
print(lista[1:3])

# Append
lista.append('pets')

print(lista)

# Extend
lista.extend(['gatos', 'cachorros'])
print(lista)

# Remove
lista.remove('amanhã')
print(lista)

# Del
del lista[0:2]
print(lista)

# Pop
lista.pop(2)
print(lista)

# Index
print(lista.index('pets'))

# Clear
lista.clear()
print(lista)

# Reverse
nomes = ['Larissa', 'Maria', 'Ana', 'Marcos', 'Zé', 'João']
nomes.reverse()
print(nomes)

# Sort
nomes.sort()
print(nomes)

# Count - mostra a quantidade que o elemento selecionado aparece na lista.
valores = [1, 2, 2, 3, 5, 7, 1, 2]
print(valores.count(2))

# Lista de listas:
numeros = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(numeros[2])
