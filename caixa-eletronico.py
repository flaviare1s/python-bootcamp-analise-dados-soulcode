# Desenvolvimento de um Simulador de Caixa Eletrônico em Python
# Contexto
# Em um mundo onde a digitalização dos serviços bancários é cada vez mais essencial, a necessidade de proporcionar uma experiência prática e segura para os usuários é uma prioridade. Bancos e instituições financeiras buscam maneiras eficientes de educar seus clientes sobre o uso de caixas eletrônicos e aplicativos bancários. Pensando nisso, um Simulador de Caixa Eletrônico pode ajudar tanto na educação financeira quanto na prática de programação.
# Desafio
# Desenvolver um Simulador de Caixa Eletrônico utilizando a linguagem de programação Python, capaz de realizar operações bancárias simples como consulta de saldo, depósitos, saques e verificação de extrato. O sistema deve garantir a segurança do usuário através da implementação de uma senha de acesso e limitar a quantidade de saques diários.

# Requisitos Funcionais
# O sistema deverá ter as seguintes funcionalidades:
# Ver o saldo da conta:
# O usuário poderá consultar o saldo atual de sua conta a qualquer momento.
# O saldo inicial deve ser definido ao iniciar o programa e atualizado conforme transações realizadas.
# Depositar um valor:
# O usuário poderá adicionar um valor à sua conta, aumentando o saldo disponível.
# Deve haver validação para garantir que o valor informado seja positivo.
# Sacar um valor:
# O usuário poderá retirar um valor de sua conta, desde que haja saldo suficiente.
# O sistema deve verificar se o valor do saque não excede o saldo disponível.
# Ver o extrato das últimas transações:
# O usuário poderá visualizar um histórico das transações realizadas (depósitos e saques).
# O extrato deve mostrar o tipo de transação, o valor e a data/hora em que foi realizada.
# Sair do sistema:
# Finalizar a execução do programa de forma segura, salvando o histórico de transações para consultas futuras.
# Desafios Extras
# Para tornar o sistema mais robusto e funcional, implemente as seguintes melhorias:
# Impedir saques acima do limite diário:
# Definir um limite máximo de saques por dia (ex: R$ 1.000,00).
# O sistema deve rastrear o total sacado no dia e impedir que o usuário exceda o limite definido.
# Implementar uma senha de acesso ao sistema:
# Solicitar uma senha ao iniciar o programa para garantir a segurança do usuário.
# Permitir um número limitado de tentativas (ex: 3 tentativas) antes de bloquear o acesso.
# Utilizar uma senha padrão (ex: 1234) que pode ser alterada pelo usuário após o primeiro acesso.

import datetime

class CaixaEletronico:
    def __init__(self, saldo_inicial=0, senha_padrao="1234", limite_saque=1000):
        self.saldo = saldo_inicial
        self.senha = senha_padrao
        self.limite_saque = limite_saque
        self.saques_hoje = 0
        self.transacoes = []
        self.autenticado = False
        
    def autenticar(self):
        tentativas = 3
        while tentativas > 0:
            senha = input("Digite sua senha: ")
            if senha == self.senha:
                self.autenticado = True
                print("Acesso autorizado!")
                return True
            else:
                tentativas -= 1
                print(f"Senha incorreta! Tentativas restantes: {tentativas}")
        print("Acesso bloqueado!")
        return False
    
    def alterar_senha(self):
        nova_senha = input("Digite a nova senha: ")
        self.senha = nova_senha
        print("Senha alterada com sucesso!")
    
    def ver_saldo(self):
        print(f"Saldo atual: R$ {self.saldo:.2f}")
    
    def depositar(self):
        valor = float(input("Digite o valor para depósito: "))
        if valor > 0:
            self.saldo += valor
            self.transacoes.append(("Depósito", valor, datetime.datetime.now()))
            print("Depósito realizado com sucesso!")
        else:
            print("Valor inválido para depósito.")
    
    def sacar(self):
        if self.saques_hoje >= self.limite_saque:
            print("Limite de saque diário atingido!")
            return
        
        valor = float(input("Digite o valor para saque: "))
        if valor > 0 and valor <= self.saldo:
            if self.saques_hoje + valor <= self.limite_saque:
                self.saldo -= valor
                self.saques_hoje += valor
                self.transacoes.append(("Saque", -valor, datetime.datetime.now()))
                print("Saque realizado com sucesso!")
            else:
                print("Saque excede o limite diário!")
        else:
            print("Saldo insuficiente ou valor inválido.")
    
    def ver_extrato(self):
        print("Extrato de transações:")
        for transacao in self.transacoes:
            tipo, valor, data = transacao
            print(f"{data.strftime('%d/%m/%Y %H:%M:%S')} - {tipo}: R$ {valor:.2f}")
    
    def executar(self):
        if not self.autenticar():
            return
        while True:
            print("\n1. Ver saldo\n2. Depositar\n3. Sacar\n4. Ver extrato\n5. Alterar senha\n6. Sair")
            opcao = input("Escolha uma opção: ")
            
            if opcao == "1":
                self.ver_saldo()
            elif opcao == "2":
                self.depositar()
            elif opcao == "3":
                self.sacar()
            elif opcao == "4":
                self.ver_extrato()
            elif opcao == "5":
                self.alterar_senha()
            elif opcao == "6":
                print("Saindo do sistema. Até mais!")
                break
            else:
                print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    caixa = CaixaEletronico(saldo_inicial=500)
    caixa.executar()
