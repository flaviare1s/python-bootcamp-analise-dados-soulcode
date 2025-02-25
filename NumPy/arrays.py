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
