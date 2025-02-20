# Funções

def saudacao():
  print('Hello, World!')

saudacao()

def area(l, c):
  area = l * c
  return area

print(area(10, 20))

comprimento = 15
largura = 30
print(area(comprimento, largura))

lista = ['Ana', 'Flávia', 'João', 'Flávio']

def saudar(nome):
  print(f'Olá {nome}')

for i in lista:
  saudar(i)

def soma(n1, n2):
  return n1 + n2

print(soma(1, 4))
