import numpy as np

# Medidas de dispersão
lojaA_idade = [65, 70, 63, 72]
lojaB_idade = [39, 100, 46, 85]

media_lojaA = np.mean(lojaA_idade)
media_lojaB = np.mean(lojaB_idade)

print(media_lojaA)
print(media_lojaB)

variancia_lojaA = np.var(lojaA_idade)
variancia_lojaB = np.var(lojaB_idade)

print(variancia_lojaA)
print(variancia_lojaB)

desvio_padrao_lojaA = np.std(lojaA_idade)
desvio_padrao_lojaB = np.std(lojaB_idade)

print(desvio_padrao_lojaA)
print(desvio_padrao_lojaB)
