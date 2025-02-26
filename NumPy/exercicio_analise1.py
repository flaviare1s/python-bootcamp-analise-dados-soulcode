import numpy as np

# Você é um analista de dados em uma empresa de vendas e foi solicitado analisar o desempenho das vendas em duas regiões. **Região X** e a **Região Y**. O objetivo da análise é entender como as vendas estão distribuídas em cada região e avaliar a consitência dos resultados.

# A empresa quer entender se precisa criar abordagens diferentes de vendas para as duas regiões.

# Dados das Vendas
vendas_regiao_X = [150, 160, 155, 158, 165, 162, 155, 160, 157, 159, 160, 163, 158, 160, 161, 159, 157, 162, 164, 161, 160, 160, 158, 157, 163, 161, 159, 160, 165, 157]
vendas_regiao_Y = [100, 150, 80, 200, 120, 90, 170, 180, 140, 130, 110, 160, 210, 140, 130, 150, 190, 110, 120, 150, 160, 200, 180, 170, 120, 150, 100, 180, 150, 170]

soma_vendas_regiao_X = np.sum(vendas_regiao_X)
soma_vendas_regiao_Y = np.sum(vendas_regiao_Y)

print('\n----- Soma -----\n')
print(f'Região X: {soma_vendas_regiao_X}')
print(f'Região Y: {soma_vendas_regiao_Y}')

media_vendas_regiao_X = np.mean(vendas_regiao_X)
media_vendas_regiao_Y = np.mean(vendas_regiao_Y)

print('\n----- Média -----\n')
print(f'Região X: {media_vendas_regiao_X}')
print(f'Região Y: {media_vendas_regiao_Y}')

variancia_vendas_regiao_X = np.var(vendas_regiao_X)
variancia_vendas_regiao_Y = np.var(vendas_regiao_Y)

print('\n----- Variância -----\n')
print(f'Região X: {variancia_vendas_regiao_X}')
print(f'Região Y: {variancia_vendas_regiao_Y}')

desvio_padrao_vendas_regiao_X = np.std(vendas_regiao_X)
desvio_padrao_vendas_regiao_Y = np.std(vendas_regiao_Y)

print('\n----- Desvio Padrão -----\n')
print(f'Região X: {desvio_padrao_vendas_regiao_X}')
print(f'Região Y: {desvio_padrao_vendas_regiao_Y}')

# Máximo e mínimo
max_vendas_regiao_X = np.max(vendas_regiao_X)
max_vendas_regiao_Y = np.max(vendas_regiao_Y)

print('\n----- Máximo -----\n')
print(f'Região X: {max_vendas_regiao_X}')
print(f'Região Y: {max_vendas_regiao_Y}')

min_vendas_regiao_X = np.min(vendas_regiao_X)
min_vendas_regiao_Y = np.min(vendas_regiao_Y)

print('\n----- Mínimo -----\n')
print(f'Região X: {min_vendas_regiao_X}')
print(f'Região Y: {min_vendas_regiao_Y}')

# Conclusão: De acordo com a análise dos dados, apesar de terem médias bem parecidas, as vendas na região X são mais homogêneas e consistentes.
# A região Y apresenta mais variabilidade e dispersão. Uma medida cabível seria adotar estratégias personalizadas para a Região Y, uma vez que suas vendas apresentam maior variação e imprevisibilidade.
