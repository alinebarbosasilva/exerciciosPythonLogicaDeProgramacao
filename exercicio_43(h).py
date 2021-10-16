# Crie um vetor que peça cinco números, em seguida exiba os cinco números
# informados e mostre qual é o menor número e o maior número.

lista_de_numeros = []

for contador in range(0, 5, 1):
    lista_de_numeros.append(int(input("Informe um número: ")))

maior_numero = -9999999999999999999999
menor_numero = 9999999999999999999999

for index in range(0, 5, 1):
    print(lista_de_numeros[index])

    if lista_de_numeros[index] > maior_numero:
        maior_numero = lista_de_numeros[index]

    if lista_de_numeros[index] < menor_numero:
        menor_numero = lista_de_numeros[index]

print(f"O maior valor é {maior_numero} e o menor valor é {menor_numero}")