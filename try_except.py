try:
  num = int(input('Digite um número: '))
  print(f'Número digitado: {num}')
except:
  print('Erro ao digitar o número')

print('-------------------------------')

# Outro exemplo:

try:
  num1 = int(input('Digite um número: '))
  num2 = int(input('Digite outro número: '))
  resultado = num1 / num2
  print(f'Resultado: {resultado}')
except ValueError:
  print('Erro ao digitar o número')
except ZeroDivisionError:
  print('Não é possivel dividir por zero')
finally:
  print('Fim do programa')

print('-------------------------------')

# Mais um exemplo:
numeros = [1, 2, 3, 4, 5]

try:
  num = int(input('Digite o índice do número da lista: '))
  print(f'Número digitado: {num}')
  print(numeros[num])
except ValueError:
  print('Erro ao digitar o número')
except IndexError:
  print('Indice inválido')
else:
  print('Não houve erro')
finally:
  print('Fim do programa')

# Tipos de erros:
# ValueError
# TypeError
# ZeroDivisionError
# IndexError
# KeyError
# AttributeError

print('-------------------------------')
