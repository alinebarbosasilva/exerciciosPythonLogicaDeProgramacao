# Crie um vetor contendo cinco cidades, em seguida exiba seus valores

# lista_cidades = ["Blumenau", "Joinville", "Pomerode", "Indaial", "Ilhota"]
#
# for index in range(0, 5, 1):
#     print(lista_cidades[index])


# Desenvolva um sistema que o usuário informa cinco números através do comando
# prompt, em seguida exiba os valores informados e mostre a soma desses valores.

# lista_valores = []
#
# for contador in range(1, 6, 1):
#     lista_valores.append(int(input("Informe um valor: ")))
#
# soma = 0
#
# for index in range(0, 5, 1):
#     print(lista_valores[index])
#     soma += lista_valores[index]
#
# print(f"A soma dos valores é {soma}")


# Crie um laço que peça nomes, poderão ser armazenados vários nomes, não há uma
# quantidade mínima nem máxima. Quando informada a palavra sair, exiba todos os
# nomes e informe a quantidade de nomes cadastrados.

# lista_nomes = []
# contador = 0
#
# while True:
#     resultado = input("Informe um nome ou a palavra Sair para finalizar o código: ")
#     if resultado == "Sair":
#         break
#     lista_nomes.append(resultado)
#     contador += 1
#
# for index in range(0, len(lista_nomes), 1):
#     print(lista_nomes[index])
#
# print(f"A quantidade de nomes cadastrados é {contador}")



# O usuário informa cinco números, em seguida exiba na ordem contrário que foram
# informados.

# lista_de_numeros = []
#
# for contador in range(0, 5, 1):
#     lista_de_numeros.append(int(input("Informe um numero: ")))
#
# for index in range(4, -1, -1):
#     print(lista_de_numeros[index])


# Faça com que sejam pedidos e armazenados cinco números. Informe quantos
# números dez foram informados pelo usuário

# lista_de_numeros = []
#
# for contador in range(0, 5, 1):
#     lista_de_numeros.append(int(input("Informe um número: ")))
#
# contador_de_dez = 0
#
# for index in range(0, 5, 1):
#     if lista_de_numeros[index] == 10:
#         contador_de_dez += 1
#
# print(contador_de_dez)


# Peça sete números, em seguida exiba a soma desses valores, a média e quantos
# números são maiores ou iguais a média.

# lista_de_numeros = []
#
# for contador in range(0, 7, 1):
#     lista_de_numeros.append(int(input("Informe um número: ")))
#
# soma = 0
#
# for index in range(0, 7, 1):
#     soma += lista_de_numeros[index]
#
# media = soma / 7
#
# contador_numeros_maior_igual_media = 0
#
# for index in range(0, 7, 1):
#     if lista_de_numeros[index] >= media:
#         contador_numeros_maior_igual_media += 1
#
# print(f"A soma dos sete números é {soma}, a média é {media} e a quantidade "
#       f"de números maior ou igual a média é {contador_numeros_maior_igual_media}")


# Haverá um cardápio contendo dez itens (você define o nome e o valor de cada item),
# cada item terá um código de 1 a 10, além do número 11 que finaliza o sistema.
# Enquanto não for digitado o número 11 será contabilizado em uma lista, quando
# digitado o número 11 exiba os produtos adquiridos e o total dessa compra.


# nome_cardapio = ["Pizza", "Pão de Queijo", "Torta de limão", "Pão de batata", "Coxinha",
#                  "Café", "Beringela Assada", "Batata doce", "Whey", "Energético"]
#
# valor_cardapio = [50.00, 2.50, 10.00, 5.00, 7.00, 2.00, 8.00, 2.00, 100.00, 8.00]
#
# lista_de_produtos = []
# valor_total = 0
#
# while True:
#     opcao = int(input(f"Informe o item do cardápio que deseja consumir: \n"
#                       f"1 - {nome_cardapio[0]} - {valor_cardapio[0]} \n"
#                       f"2 - {nome_cardapio[1]} - {valor_cardapio[1]} \n"
#                       f"3 - {nome_cardapio[2]} - {valor_cardapio[2]} \n"
#                       f"4 - {nome_cardapio[3]} - {valor_cardapio[3]} \n"
#                       f"5 - {nome_cardapio[4]} - {valor_cardapio[4]} \n"
#                       f"6 - {nome_cardapio[5]} - {valor_cardapio[5]} \n"
#                       f"7 - {nome_cardapio[6]} - {valor_cardapio[6]} \n"
#                       f"8 - {nome_cardapio[7]} - {valor_cardapio[7]} \n"
#                       f"9 - {nome_cardapio[8]} - {valor_cardapio[8]} \n"
#                       f"10 - {nome_cardapio[9]} - {valor_cardapio[9]} \n"
#                       f"11 - Finalizar a compra. \n"
#                       f"Digite aqui: "))
#
#     if opcao == 11:
#         break
#     lista_de_produtos.append(nome_cardapio[opcao - 1])
#     valor_total += valor_cardapio[opcao - 1]
#
#
# for index in range(0, len(lista_de_produtos), 1):
#     print(lista_de_produtos[index])
#
# print(f"O valor total da compra é {valor_total}")


# Crie um vetor que peça cinco números, em seguida exiba os cinco números
# informados e mostre qual é o menor número e o maior número

# lista_de_numeros = []
#
# for contador in range(0, 5, 1):
#     lista_de_numeros.append(int(input("Informe um número: ")))
#
# maior_numero = -9999999999999999999999
# menor_numero = 9999999999999999999999
#
# for index in range(0, 5, 1):
#     print(lista_de_numeros[index])
#
#     if lista_de_numeros[index] > maior_numero:
#         maior_numero = lista_de_numeros[index]
#
#     if lista_de_numeros[index] < menor_numero:
#         menor_numero = lista_de_numeros[index]
#
# print(f"O maior valor é {maior_numero} e o menor valor é {menor_numero}")


# Desenvolva um sistema para gerenciar cursos, as funcionalidades pedidas são:
# 1) Cadastrar curso - Pede o nome do novo curso
# 2) Selecionar cursos - Exibe todos os cursos
# 3) Remover curso - Pede o nome do curso e realiza a exclusão
# 4) Sair do sistema - Finaliza o laço

# lista_de_cursos = []
#
# while True:
#     opcao = int(input("Informe a opão que deseja realizar \n"
#                       "1 - Cadastrar novo curso \n"
#                       "2 - Selecionar curso \n"
#                       "3 - Remover curso \n"
#                       "4 - Sair do sistema \n"
#                       "Digite aqui: "))
#     if opcao == 1:
#         lista_de_cursos.append(input("Informe o nome do novo curso: "))
#     elif opcao == 2:
#         print("Os cursos disponíveis são: ")
#         for index in range(0, len(lista_de_cursos), 1):
#             print(lista_de_cursos[index])
#     elif opcao == 3:
#         for index in range(0, len(lista_de_cursos), 1):
#             print(lista_de_cursos[index])
#         curso_a_remover = input("Informe o curso que deseja remover: ")
#         for index in range(0, len(lista_de_cursos), 1):
#             if lista_de_cursos[index] == curso_a_remover:
#                 lista_de_cursos.pop(index)
#                 print(f"Curso {curso_a_remover} foi removido com sucesso...")
#     elif opcao == 4:
#         print("Sistema finalizado...")
#         break
#     else:
#         "A opção informada não existe..."


# Crie uma matriz 3x3, onde a primeira coluna terá o nome de um produto, a segunda
# coluna a marca e a terceira o valor. Esses dados não precisam ser informados pelo
# usuário, essas informações podem ser pré-definidas como no exemplo de contatos,
# assim que desenvolver a matriz, exiba os dados utilizando laços de repetição.


# matriz = [["Pepsi", "Pão de Queijo", "Torta"],
#           ["Pepsi", "Padaria", "Padaria"],
#           [10.00, 2.00, 5.00]
# ]
#
# for index_linha in range(0, len(matriz), 1):
#     for index_coluna in range(0, len(matriz[index_linha]), 1):
#         print(matriz[index_linha][index_coluna])