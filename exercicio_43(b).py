# Desenvolva um sistema que o usuário informa cinco números através do comando
# prompt, em seguida exiba os valores informados e mostre a soma desses valores.

lista_valores = []

for contador in range(1, 6, 1):
    lista_valores.append(int(input("Informe um valor: ")))

soma = 0

for index in range(0, 5, 1):
    print(lista_valores[index])
    soma += lista_valores[index]

print(f"A soma dos valores é {soma}")