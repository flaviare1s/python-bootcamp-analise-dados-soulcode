class aniversariante:
  def __init__(self, nome, idade):
    self.nome = nome
    self.idade = idade

  def apresentar(self):
    return f"Olá, meu nome é {self.nome} e tenho {self.idade} anos."

  def aniversario(self):
    self.idade += 1
    return f"Parabéns, {self.nome}! Hoje vocé tem {self.idade} anos."
  

pessoa = aniversariante("Ana Clara", 20)

print(pessoa.apresentar())
print(pessoa.aniversario())

# Outro exemplo:

class carro:
  def __init__(self, cor, modelo, placa):
    self.cor = cor
    self.modelo = modelo
    self.placa = placa

  def acelerar(self):
    return f'O {self.modelo} acelerou!'
  
carro_1 = carro('preto', 'Celta', 'OPQ-1344')
print(carro_1.acelerar())


# Mais um exemplo:

class animal:
  def __init__(self, nome, tipo, especie, idade, raca, class_alimentacao, peso):
    self.nome = nome
    self.tipo = tipo
    self.especie = especie
    self.idade = idade
    self.raca = raca
    self.class_alimentacao = class_alimentacao
    self.peso = peso

  def emitir_som(self):
    return f'{self.nome} emite sons!'
  
  def movimentacao(self):
    if self.tipo == 'ave':
      return f'{self.nome} que é {self.tipo} voa!'
    elif self.tipo == 'réptil':
      return f'{self.nome} que é {self.tipo} rasteja!'
    elif self.tipo == 'peixe':
      return f'{self.nome} que é {self.tipo} nada!'
    else:
      return f'{self.nome} que é {self.tipo} é provável que ande!'
    
animal_1 = animal('Tito', 'ave', 'papagaio', 2, 'papagaio', 'carnivoro', 0.5)
print(animal_1.movimentacao())

# Exercício:

class produto:
  def __init__(self, nome, categoria, preco, quantidade, codigo_barra):
    self.nome = nome
    self.categoria = categoria
    self.preco = preco
    self.quantidade = quantidade
    self.codigo_barra = codigo_barra

  def informacoes(self):
    return f'Informações do produto: \nNome: {self.nome} \nCategoria: {self.categoria} \nPreço: {self.preco} \nQuantidade: {self.quantidade} \nCódigo de barra: {self.codigo_barra}'
  
  def atualizar_preco(self, novo_preco):
    self.preco = novo_preco

produto_1 = produto('Notebook', 'Eletrônico', 5000, 1, '123456789')
print(produto_1.informacoes())
produto_1.atualizar_preco(6000)
print(produto_1.informacoes())
