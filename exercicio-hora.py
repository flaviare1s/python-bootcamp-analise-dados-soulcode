# Faça um programa que converta da notação de 24 horas para a notação de 12 horas. Por exemplo, o programa deve converter 14:25 em 2:25 P.M. A entrada é dada em dois inteiros. Deve haver pelo menos duas funções: uma para fazer a conversão e uma para a saída. Registre a informação A.M./P.M. como um valor ‘A’ para A.M. e ‘P’ para P.M. Assim, a função para efetuar as conversões terá um parâmetro formal para registrar se é A.M. ou P.M. Inclua um loop que permita que o usuário repita esse cálculo para novos valores de entrada todas as vezes que desejar.

def converter_horas():
  horas = int(input("Digite as horas(0-23): "))
  minutos = int(input("Digite os minutos(0-59): "))
  if horas > 12:
    horas -= 12
    print(f'São {horas}:{minutos} PM')
  else:
    print(f'São {horas}:{minutos} AM')
while True:
  converter_horas()
  continuar = input("Deseja continuar? (s/n): ").strip().lower()
  if continuar != 's':
    break


# Outra maneira de fazer

def convert(h, m):
  if h < 0 or h > 23 or m < 0 or m > 59:
    print('Hora inválida')
    return
  if h >= 12:
    print(f'{h - 12}:{m} PM')
  else:
    print(f'{h}:{m} AM')
  
  print(f'{h}:{m} AM')

hora = int(input('Digite a hora: '))
minuto = int(input('Digite os minutos: '))

convert(hora, minuto)
