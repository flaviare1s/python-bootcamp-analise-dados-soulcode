# For
# for elemento in conjunto
# range(inicio, fim, passo)

# for i in range(2, 10, 2):
#   print(i)

pratos = 5

for prato in range(pratos):
  print(f'Lavou o prato {prato + 1}')

print('---------------------------')


# Exercício 1: Imprima do 0 ao 4:
for i in range(5):
  print(i)

print('---------------------------')


# Exercício 1: Imprima do 2 ao 5:
for i in range(2, 6):
  print(i)

print('---------------------------')


# Exercício 1: Imprima do 1 ao 9, pulando de 2 em 2:
for i in range(1, 10, 2):
  print(i)

print('---------------------------')

# Exercício 1: Imprima do 
for i in range(10, 2, -2):
  print(i)

print('---------------------------')

# Percorrendo uma lista com for:
frutas = ['banana', 'maca', 'laranja', 'uva', 'abacaxi', 'melancia']

for fruta in frutas:
  print(fruta)

print('---------------------------')

# Modificando elementos de umas lista
numeros = [1, 2, 3, 4, 5]

for numero in range(len(numeros)):
  numeros[numero] *= 2
print(numeros)

print('---------------------------')

# Filtrando elementos de uma lista
valores = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares = []

for valor in valores:
  if valor % 2 == 0:
    pares.append(valor)

print(pares)

print('---------------------------')

# Removendo elementos de uma lista
elementos = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for elemento in elementos:
  if elemento % 2 == 0:
    elementos.remove(elemento)

print(elementos)

print('---------------------------')
