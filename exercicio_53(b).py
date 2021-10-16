# Criar uma agenda para manipular os dados: nome, e-mail, idade e cidade,
# essa agenda terá opções para cadastrar, alterar, selecionar e excluir
# contatos. Cada ação da agenda deverá estar em uma função.


from funcoes_agenda import cadastrar, alterar, selecionar, excluir

lista_contatos = []

while True:
    opcao = input("Informe uma das opções abaixo: \n"
                  "1 - cadastrar novos dados de contato. \n"
                  "2 - alterar dados de um contato existente. \n"
                  "3 - selecionar dados existentes. \n"
                  "4 - excluir um dado existente. \n"
                  "5 - finalizar o programa \n"
                  "DIGITE AQUI: ")

    if opcao == "1":
        novo_cadastrado = cadastrar()
        lista_contatos.append(novo_cadastrado)
    elif opcao == "2":
        lista_contatos = alterar(lista_contatos)
    elif opcao == "3":
        selecionar(lista_contatos)
    elif opcao == "4":
        lista_contatos = excluir(lista_contatos)
    elif opcao == "5":
        break
    else:
        print("Opção informada está inválida...")