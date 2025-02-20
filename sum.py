# Sum()

lista = [1, 2, 3, 4, 5]

print(sum(lista))


# Camila está organizando um projeto e precisa calcular o tempo total necessário para concluir três atividades: A, B e C. No entanto, se alguma atividade tiver um número de dias negativo, o código deve avisar que os valores inseridos são inválidos e não calcular o total.

# Escreva um programa que receba o número de dias de três atividades e exiba o tempo total do projeto. Se algum valor for negativo, mostre uma mensagem informando o erro.

# atividade_a = int(input('Digite o número de dias da primeira atividade: '))
# atividade_b = int(input('Digite o número de dias da segunda atividade: '))
# atividade_c = int(input('Digite o número de dias da terceira atividade: '))

# atividades = []

# if atividade_a < 0 or atividade_b < 0 or atividade_c < 0:
#   print('Os valores inseridos são inválidos')
# else:
#   atividades.append(atividade_a)
#   atividades.append(atividade_b)
#   atividades.append(atividade_c)

#   total = sum(atividades)
#   print(f'Tempo total do projeto: {total} dias')

# Outra maneira de fazer:

atividades = []

for i in range(3):
  valor = int(input(f'Digite o número de dias da atividade {i + 1}: '))

  if valor < 0:
    print('Os valores inseridos são inválidos')
  else:
    atividades.append(valor)

total = sum(atividades)
print(f'Tempo total do projeto: {total} dias')
