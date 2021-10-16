# O usuário informa cinco números, em seguida exiba na ordem contrário que foram
# informados.

lista_de_numeros = []

for contador in range(0, 5, 1):
    lista_de_numeros.append(int(input("Informe um numero: ")))

for index in range(4, -1, -1):
    print(lista_de_numeros[index])