# Desenvolvimento de uma Agenda de Contatos em Python
# Contexto
# Uma pequena empresa está em processo de digitalização de suas operações e deseja substituir sua antiga agenda de contatos em papel por um sistema digital eficiente e fácil de usar. O objetivo é organizar as informações de clientes e fornecedores, facilitando a busca e atualização dos contatos. A empresa procura uma solução que permita adicionar, buscar, editar e remover contatos, além de listar todos em ordem alfabética para facilitar o acesso.
# Desafio
# Desenvolver um sistema de Agenda de Contatos utilizando a linguagem de programação Python. O sistema deve ser capaz de armazenar e gerenciar informações de forma prática e eficiente, garantindo a integridade e a organização dos dados.

# Requisitos Funcionais
# O sistema deverá possuir as seguintes funcionalidades:
# Adicionar um novo contato:
# O usuário poderá inserir o nome completo e o número de telefone do contato.
# O sistema deve verificar se o contato já existe na agenda para evitar duplicidade.
# Desafio Extra: Validar o formato do número de telefone para garantir consistência e evitar erros.
# Buscar um contato pelo nome:
# O usuário poderá procurar um contato digitando parte do nome.
# O sistema deverá listar todos os contatos que contenham o termo buscado, mostrando o nome completo e o número de telefone.
# Listar todos os contatos em ordem alfabética:
# Exibir a lista de contatos ordenada de forma crescente.
# Desafio Extra: Ordenar por sobrenome (última palavra do nome) para facilitar a organização.
# Editar um contato existente:
# O usuário poderá alterar o nome e/ou o número de telefone de um contato.
# O sistema deve permitir manter as informações atuais caso o usuário não queira alterá-las.
# Remover um contato:
# O usuário poderá excluir um contato da agenda.
# O sistema deve solicitar uma confirmação antes de realizar a exclusão definitiva.
# Sair do sistema:
# Finalizar a execução do programa de forma segura
# Desafios Extras
# Para aumentar a robustez e a utilidade do sistema, implemente as seguintes melhorias:
# Validação do número de telefone:
# Utilize expressões regulares (Regex) para validar o formato do telefone.
# Aceitar apenas os formatos: (XX) XXXXX-XXXX ou (XX) XXXX-XXXX.
# Ordenação por sobrenome:
# Ordene a lista de contatos utilizando o sobrenome (última palavra do nome).
# Garanta que a ordenação desconsidere letras maiúsculas e minúsculas.


import re

class AgendaContatos:
    def __init__(self):
        self.contatos = []
    
    def validar_telefone(self, telefone):
        padrao = re.compile(r"^\(\d{2}\) \d{4,5}-\d{4}$")
        return bool(padrao.match(telefone))
    
    def adicionar_contato(self):
        nome = input("Digite o nome completo: ")
        telefone = input("Digite o número de telefone ((XX) XXXXX-XXXX ou (XX) XXXX-XXXX): ")
        
        if not self.validar_telefone(telefone):
            print("Formato de telefone inválido!")
            return
        
        for contato in self.contatos:
            if contato["nome"].lower() == nome.lower():
                print("Contato já existe!")
                return
        
        self.contatos.append({"nome": nome, "telefone": telefone})
        print("Contato adicionado com sucesso!")
    
    def buscar_contato(self):
        termo = input("Digite parte do nome para buscar: ").lower()
        resultados = [c for c in self.contatos if termo in c["nome"].lower()]
        
        if resultados:
            for contato in resultados:
                print(f"{contato['nome']}: {contato['telefone']}")
        else:
            print("Nenhum contato encontrado.")
    
    def listar_contatos(self):
        self.contatos.sort(key=lambda c: c["nome"].split()[-1].lower())
        for contato in self.contatos:
            print(f"{contato['nome']}: {contato['telefone']}")
    
    def editar_contato(self):
        nome = input("Digite o nome do contato a ser editado: ")
        for contato in self.contatos:
            if contato["nome"].lower() == nome.lower():
                novo_nome = input("Novo nome (deixe em branco para manter): ") or contato["nome"]
                novo_telefone = input("Novo telefone (deixe em branco para manter): ") or contato["telefone"]
                
                if novo_telefone and not self.validar_telefone(novo_telefone):
                    print("Formato de telefone inválido!")
                    return
                
                contato["nome"], contato["telefone"] = novo_nome, novo_telefone
                print("Contato atualizado com sucesso!")
                return
        print("Contato não encontrado.")
    
    def remover_contato(self):
        nome = input("Digite o nome do contato a ser removido: ")
        for contato in self.contatos:
            if contato["nome"].lower() == nome.lower():
                confirmacao = input("Tem certeza que deseja remover? (S/N): ").strip().lower()
                if confirmacao == "s":
                    self.contatos.remove(contato)
                    print("Contato removido com sucesso!")
                return
        print("Contato não encontrado.")
    
    def executar(self):
        while True:
            print("\n1. Adicionar Contato\n2. Buscar Contato\n3. Listar Contatos\n4. Editar Contato\n5. Remover Contato\n6. Sair")
            opcao = input("Escolha uma opção: ")
            
            if opcao == "1":
                self.adicionar_contato()
            elif opcao == "2":
                self.buscar_contato()
            elif opcao == "3":
                self.listar_contatos()
            elif opcao == "4":
                self.editar_contato()
            elif opcao == "5":
                self.remover_contato()
            elif opcao == "6":
                print("Saindo do sistema. Até mais!")
                break
            else:
                print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    agenda = AgendaContatos()
    agenda.executar()
