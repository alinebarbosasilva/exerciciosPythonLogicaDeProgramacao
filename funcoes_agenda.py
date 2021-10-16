def cadastrar():
    novo_cadastro = []

    nome = input("Informe o nome do novo usuário: ")
    email = input("Informe o email do novo usuário: ")
    idade = input("Informe o idade do novo usuário: ")
    cidade = input("Informe o cidade do novo usuário: ")

    novo_cadastro.append(nome)
    novo_cadastro.append(email)
    novo_cadastro.append(idade)
    novo_cadastro.append(cidade)

    return novo_cadastro

def alterar(lista_contatos):
    nome = input("Informe o nome do usuário que deseja alterar informações: ")
    for index in range(0, len(lista_contatos), 1):
        if lista_contatos[index][0] == nome:
            lista_contatos[index][0] = input("Informe o novo nome do usuário: ")
            lista_contatos[index][1] = input("Informe o novo email do usuário: ")
            lista_contatos[index][2] = input("Informe o novo idade do usuário: ")
            lista_contatos[index][3] = input("Informe o novo cidade do usuário: ")

    return lista_contatos

def selecionar(lista_contatos):
    for index_linha in range(0, len(lista_contatos), 1):
        print(lista_contatos[index_linha][0], lista_contatos[index_linha][1],
              lista_contatos[index_linha][2], lista_contatos[index_linha][3])

def excluir(lista_contatos):
    nome = input("Informe o nome do usuário que deseja deletar informações: ")
    for index in range(0, len(lista_contatos), 1):
        if lista_contatos[index][0] == nome:
            lista_contatos.pop(index)

    return lista_contatos