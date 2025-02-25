import numpy as np

print(np.__version__)

lista = [1, 2, 3, 4, 5, 6, 7]
array = np.array(lista)
print(f'Lista: {lista}\nArray: {array}')

# Matrizes:
matriz = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(matriz)

# Arrays com valores inicializados:
array_zeros = np.zeros(5)
print(array_zeros)

array_ones = np.ones(5)
print(array_ones)

array_vazios = np.empty(5)
print(array_vazios)

array_aleatorios = np.random.rand(5)
print(array_aleatorios)

# Preenchendo matrizes:
matriz_uns = np.ones((3, 2))
print(matriz_uns)

matriz_zeros = np.zeros((2, 3), dtype=int)
print(matriz_zeros)

matriz_aleatoria = np.random.rand(2, 3)
print(matriz_aleatoria)

# Matriz aleatória com valores inteiros:
matriz_inteiros = np.random.randint(0, 10, (2, 3))
print(matriz_inteiros)

matriz_inteiros2 = np.random.randint(0, 100, (2, 3))
print(matriz_inteiros)

# Arrays com valores sequenciais:
sequencia = np.arange(0, 10, 2) # 0 a 9, pulando de 2 em 2
print(sequencia)

# Arrays com valores espaçados igualmente:
array_espacado = np.linspace(0, 1, 5)
print(array_espacado)
