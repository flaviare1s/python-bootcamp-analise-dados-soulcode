import time

saldo = 1000.0
limite_saque_diario = 1000.0
saques_realizados = 0
extrato = []
senha = "1234"
tentativas = 3

# Autenticação
while tentativas > 0:
    tentativa = input("Digite a senha para acessar o caixa eletrônico: ")
    if tentativa == senha:
        print("Acesso permitido!\n")
        break
    else:
        tentativas -= 1
        print(f"Senha incorreta! Tentativas restantes: {tentativas}")
        if tentativas == 0:
            print("Acesso bloqueado. Tente novamente mais tarde.")
            exit()

# Menu principal
def menu():
    print("\n=== Caixa Eletrônico ===")
    print("1. Ver Saldo")
    print("2. Depositar")
    print("3. Sacar")
    print("4. Ver Extrato")
    print("5. Sair")

while True:
    menu()
    opcao = input("Escolha uma opção: ")
    
    if opcao == "1":
        print(f"\nSaldo atual: R$ {saldo:.2f}")
    
    elif opcao == "2":
        valor = float(input("Digite o valor para depósito: "))
        if valor > 0:
            saldo += valor
            extrato.append(f"Depósito de R$ {valor:.2f} em {time.strftime('%d/%m/%Y %H:%M:%S')}")
            print("Depósito realizado com sucesso!")
        else:
            print("Valor inválido!")
    
    elif opcao == "3":
        valor = float(input("Digite o valor para saque: "))
        if valor > saldo:
            print("Saldo insuficiente!")
        elif valor > limite_saque_diario - saques_realizados:
            print("Limite de saque diário excedido!")
        elif valor > 0:
            saldo -= valor
            saques_realizados += valor
            extrato.append(f"Saque de R$ {valor:.2f} em {time.strftime('%d/%m/%Y %H:%M:%S')}")
            print("Saque realizado com sucesso!")
        else:
            print("Valor inválido!")
    
    elif opcao == "4":
        print("\n=== Extrato ===")
        if not extrato:
            print("Nenhuma transação realizada.")
        else:
            for transacao in extrato:
                print(transacao)
    
    elif opcao == "5":
        print("Saindo... Obrigado por usar o caixa eletrônico!")
        break
    
    else:
        print("Opção inválida! Tente novamente.")
