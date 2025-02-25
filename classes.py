class Aniversariante:
  def __init__(self, nome, idade):
    self.nome = nome
    self.idade = idade

  def apresentar(self):
    return f"Olá, meu nome é {self.nome} e tenho {self.idade} anos."

  def aniversario(self):
    self.idade += 1
    return f"Parabéns, {self.nome}! Hoje vocé tem {self.idade} anos."
  

pessoa = Aniversariante("Ana Clara", 20)

print(pessoa.apresentar())
print(pessoa.aniversario())

# Outro exemplo:

class Carro:
  def __init__(self, cor, modelo, placa):
    self.cor = cor
    self.modelo = modelo
    self.placa = placa

  def acelerar(self):
    return f'O {self.modelo} acelerou!'
  
carro_1 = Carro('preto', 'Celta', 'OPQ-1344')
print(carro_1.acelerar())


# Mais um exemplo:

class Animal:
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
    
animal_1 = Animal('Tito', 'ave', 'papagaio', 2, 'papagaio', 'carnivoro', 0.5)
print(animal_1.movimentacao())

# Exercício:

class Produto:
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

  def adicionar_estoque(self, quantidade):
    self.quantidade += quantidade

  def verificar_disponibilidade(self):
    if self.quantidade > 0:
      return f'{self.nome} está disponível'
    else:
      return f'Produto indisponível'
    
  def remover_produto(self):
    self.quantidade = 0
    

produto_1 = Produto('Notebook', 'Eletrônico', 5000, 1, '123456789')
print(produto_1.informacoes())
produto_1.atualizar_preco(6000)
print(produto_1.informacoes())
produto_1.adicionar_estoque(10)
print(produto_1.informacoes())
print(produto_1.verificar_disponibilidade())
produto_1.remover_produto()
print(produto_1.verificar_disponibilidade())
