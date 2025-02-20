# Tupla

tupla = (3, 'Python', True)
print(tupla[1])

# Fatiando uma tupla
print(tupla[0:2])

# Iteração em uma tupla
for i in tupla:
  print(i)

# Métodos Básicos

# Count - conta quantas vezes um elemento aparece
print(tupla.count(True))

# Index - retorna o index de um elemento
print(tupla.index(True))

# Type
print(type(tupla))
print(type(tupla[0]))

# Sum
tupla_int = (1, 2, 3, 4, 5)
print(sum(tupla_int))

# Len
print(len(tupla))

# Convertendo lista em tupla
lista = [1, 2, 3, 4, 5]
tupla2 = tuple(lista)

print(tupla2)

# Exercício:
# Faça um algoritmo que peça para o usuário colocar quatro notas. Armazene-as em uma tupla e calcule a média utilizando sum() e len().
# Se o aluno tiver média menor que 7 está reprovado.

notas = ()

for i in range(4):
  nota = float(input(f'Digite a {i + 1}ª nota: '))
  notas += (nota,)

media = sum(notas) / len(notas)

if media < 7:
  print('Reprovado!')
else:
  print('Aprovado!')

print(f'Média: {media}')

# Fazendo com lista de depois transformando em tupla

valores = []

for i in range(4):
  nota = float(input(f'Digite a {i + 1}ª nota: '))
  valores.append(nota)

valores = tuple(valores)

media = sum(valores) / len(valores)

if media < 7:
  print('Reprovado!')
else:
  print('Aprovado!')

print(f'Média: {media}')
