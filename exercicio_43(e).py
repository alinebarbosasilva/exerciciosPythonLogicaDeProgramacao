# Faça com que sejam pedidos e armazenados cinco números. Informe quantos
# números dez foram informados pelo usuário

lista_de_numeros = []

for contador in range(0, 5, 1):
    lista_de_numeros.append(int(input("Informe um número: ")))

contador_de_dez = 0

for index in range(0, 5, 1):
    if lista_de_numeros[index] == 10:
        contador_de_dez += 1

print(contador_de_dez)