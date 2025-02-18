print('Hello World')

# Condicionais:

if 2 > 7:
  print('É maior!')
elif 2 == 7:
  print('É igual')
else:
  print('Não é maior!')

  # ---------------------------

if False:
  print('É verdadeiro')
else:
  print('É falso!')

# -----------------------

# Short Hand If... Else

a = 2
b = 300

print('A') if a < b else print('B')

# ---------------------------

n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor diferente do primeiro: '))

if n1 > n2:
  print(f'{n1} é maior que {n2}')
else:
  print(f'{n1} é menor que {n2}')

  
# Crie um programa que pede a idade do usuário e classifica:

idade = int(input('Qual a sua idade? '))

if idade <= 12:
  print('Você é criança')
elif idade > 12 and idade < 18:
  print('Você é adolecente')
elif idade >= 18 and idade < 60:
  print('Você é adulto!')
else:
  print('Você é idoso!')

# -------------------------

# IN

listaFrutas = 'Uva, Morango, Melancia, Mamão, Banana'

fruta_1 = 'Pera'

fruta_2 = 'Uva'

if fruta_1 in listaFrutas:
  print(f'{fruta_1} está na lista')
else: 
  print(f'{fruta_1} não está na lista')

if fruta_2 in listaFrutas:
  print(f'{fruta_2} está na lista')
else: 
  print(f'{fruta_2} não está na lista')
