import pandas as pd
from pandasgui import show

# Criando DataFrames

dados = {
  'Nome': ['Ana', 'Bia', 'Carlos'],
  'Carro': ['Fiat', 'Chevrolet', 'Ford'],
  'Cidade': ['Santos', 'São Paulo', 'Rio de Janeiro'],
  'Salário': [1000, 2000, 3000]
}

funcionarios = pd.DataFrame(dados)

show(funcionarios)

funcionarios.to_csv('funcionarios.csv', index=False)
