# While
bolacha = 5

while bolacha > 0:
  print(f'Tenho {bolacha} bolacha(s)')
  print('Comi uma bolacha')
  bolacha -= 1
print('Acabaram as bolachas')

# EXERCÍCIO:
# Você foi contratado para desenvolver um pequeno sistema que auxilie professores no cálculo da média de notas dos alunos. O objetivo do programa é solicitar duas notas de um aluno, calcular a média e exibir o resultado. Esse processo deve ser repetido três vezes, pois será aplicado a três alunos diferentes.
# Regras do programa:
# O programa deve pedir duas notas para cada aluno.
# Após receber as notas, ele deve calcular e exibir a média aritmética.
# O procedimento deve se repetir para três alunos diferentes.

total_alunos = int(input('Digite o total de alunos: '))
aluno_atual = 1

while aluno_atual <= total_alunos:
    nota1 = float(input(f'Digite a primeira nota do {aluno_atual}º aluno: '))
    nota2 = float(input(f'Digite a segunda nota do {aluno_atual}º aluno: '))

    media = (nota1 + nota2) / 2
    print(f'A média do {aluno_atual}º aluno é: {media}\n')

    aluno_atual += 1

# EXERCÍCIO 2 - Adivinhando o Número Secreto

# Imagine que você está desenvolvendo um jogo de adivinhação simples. O programa deve escolher um número secreto (por exemplo, 7), e o usuário deve tentar adivinhá-lo.
# Regras do programa:
# O programa deve solicitar um palpite ao usuário.
# Se o número digitado for diferente do número secreto, o programa deve exibir "Errado! Tente novamente:" e pedir um novo palpite.
# O loop deve continuar até que o usuário acerte o número.
# Quando o usuário acertar, o programa deve exibir "Parabéns! Você acertou!" e encerrar.

numero_secreto = 14

while True:
  palpite = int(input('Digite um número: '))
  if palpite == numero_secreto:
    print('Parabéns! Vocé acertou!')
    break
  else:
    print('Errado! Tente novamente:')
