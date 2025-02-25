import numpy as np

array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Shape
print(array.shape) # Retorna a quantidade de linhas e colunas

# Reshape
array_reshape = array.reshape(9, 1) # Altera a quantidade de linhas e colunas
print(array_reshape)

# Ndim
print(array.ndim) # Retorna a quantidade de dimensões

# Size
print(array.size) # Retorna a quantidade de elementos

# Dtype
print(array.dtype)

# Slicing
arr = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
array_slicing = arr[0:2]
print(array_slicing)

# Sum
array_sum = arr.sum()
print(array_sum)

# Média aritmética
array_mean = arr.mean()
print(array_mean)

# Mediana
array_median = np.median(arr)
print(array_median)

# Valor máximo
array_max = arr.max()
print(array_max)

# Valor mínimo
array_min = arr.min()
print(array_min)

# Índice do maior valor
array_argmax = arr.argmax()
print(array_argmax)

# Índice do menor valor
array_argmin = arr.argmin()
print(array_argmin)
