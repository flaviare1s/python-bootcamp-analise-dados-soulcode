while True:
    print('1 - Soma\n2 - Subtração\n3 - Multiplicação\n4 - Divisão\n5 - Sair')
    opcao = int(input('Digite a opção desejada: '))

    if opcao == 5:
        print("Saindo do programa...")
        break

    if opcao in [1, 2, 3, 4]:
        n1 = float(input('Digite o primeiro número: '))
        n2 = float(input('Digite o segundo número: '))

        if opcao == 1:
            print(f'{n1} + {n2} = {n1 + n2}')
        elif opcao == 2:
            print(f'{n1} - {n2} = {n1 - n2}')
        elif opcao == 3:
            print(f'{n1} * {n2} = {n1 * n2}')
        elif opcao == 4:
            if n2 == 0:
                print("Erro: divisão por zero!")
            else:
                print(f'{n1} / {n2} = {n1 / n2}')
    else:
        print("Opção inválida! Escolha um número entre 1 e 5.")

    print()

print("Fim do programa.")