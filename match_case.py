dia = int(input('Digite o dia da semana em números (1-7): '))

match dia:
  case 1:
    print('Segunda-feira')
  case 2:
    print('Terça-feira')
  case 3:
    print('Quarta-feira')
  case 4:
    print('Quinta-feira')
  case 5:
    print('Sexta-feira')
  case 6:
    print('Sábado')
  case 7:
    print('Domingo')
  case _:
    print('Digite entre 1 e 7')

print('-------------------------------------')


# EXERCÍCIO:
# Escreva um programa que recebe uma nota (0 a 10) e use match case para imprimir:
# “Aprovado” (7 a 10);
# “Reprovado” (0 a 4);
# “Recuperação” (5 a 6);
# Caso o número seja inválido, imprimir “Nota inválida”

nota = float(input('Digite uma nota de 0 a 10: '))

match nota:
  case 0 | 1 | 2 | 3 | 4:
    print('Reprovado')
  case 5 | 6:
    print('Recuperação')
  case 7 | 8 | 9 | 10:
    print('Aprovado')
  case _:
    print('Nota inválida')

print('-------------------------------------')


# Outro exemplo:

pessoa = {
  'nome': 'João',
  'idade': 25
}

match pessoa:
  case {'nome': nome, 'idade': idade}:
    print(f'{nome} tem {idade} anos')
  case {'nome': nome}:
    print(f'{nome} tem idade desconhecida')
  case _:
    print('Pessoa desconhecida')

print('-------------------------------------')


# Exercício:
# Faça um menu usando match case:

print('1. Cadastro')
print('2. Login')
print('3. Entrar')
print('4. Sair')

opcao = int(input('Digite a opção desejada: '))

match opcao:
  case 1:
    print('Cadastro')
  case 2:
    print('Login')
  case 3:
    print('Entrar')
  case 4:
    print('Sair')
  case _:
    print('Valor inválido!')
