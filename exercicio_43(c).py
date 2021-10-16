# Crie um laço que peça nomes, poderão ser armazenados vários nomes, não há uma
# quantidade mínima nem máxima. Quando informada a palavra sair, exiba todos os
# nomes e informe a quantidade de nomes cadastrados.

lista_nomes = []
contador = 0

while True:
    resultado = input("Informe um nome ou a palavra Sair para finalizar o código: ")
    if resultado == "Sair":
        break
    lista_nomes.append(resultado)
    contador += 1

for index in range(0, len(lista_nomes), 1):
    print(lista_nomes[index])

print(f"A quantidade de nomes cadastrados é {contador}")