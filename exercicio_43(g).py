# Haverá um cardápio contendo dez itens (você define o nome e o valor de cada item),
# cada item terá um código de 1 a 10, além do número 11 que finaliza o sistema.
# Enquanto não for digitado o número 11 será contabilizado em uma lista, quando
# digitado o número 11 exiba os produtos adquiridos e o total dessa compra.


nome_cardapio = ["Pizza", "Pão de Queijo", "Torta de limão", "Pão de batata", "Coxinha",
                 "Café", "Beringela Assada", "Batata doce", "Whey", "Energético"]

valor_cardapio = [50.00, 2.50, 10.00, 5.00, 7.00, 2.00, 8.00, 2.00, 100.00, 8.00]

lista_de_produtos = []
valor_total = 0

while True:
    opcao = int(input(f"Informe o item do cardápio que deseja consumir: \n"
                      f"1 - {nome_cardapio[0]} - {valor_cardapio[0]} \n"
                      f"2 - {nome_cardapio[1]} - {valor_cardapio[1]} \n"
                      f"3 - {nome_cardapio[2]} - {valor_cardapio[2]} \n"
                      f"4 - {nome_cardapio[3]} - {valor_cardapio[3]} \n"
                      f"5 - {nome_cardapio[4]} - {valor_cardapio[4]} \n"
                      f"6 - {nome_cardapio[5]} - {valor_cardapio[5]} \n"
                      f"7 - {nome_cardapio[6]} - {valor_cardapio[6]} \n"
                      f"8 - {nome_cardapio[7]} - {valor_cardapio[7]} \n"
                      f"9 - {nome_cardapio[8]} - {valor_cardapio[8]} \n"
                      f"10 - {nome_cardapio[9]} - {valor_cardapio[9]} \n"
                      f"11 - Finalizar a compra. \n"
                      f"Digite aqui: "))

    if opcao == 11:
        break
    lista_de_produtos.append(nome_cardapio[opcao - 1])
    valor_total += valor_cardapio[opcao - 1]


for index in range(0, len(lista_de_produtos), 1):
    print(lista_de_produtos[index])

print(f"O valor total da compra é {valor_total}")