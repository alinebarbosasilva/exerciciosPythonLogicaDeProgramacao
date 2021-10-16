# Peça sete números, em seguida exiba a soma desses valores, a média e quantos
# números são maiores ou iguais a média.

lista_de_numeros = []

for contador in range(0, 7, 1):
    lista_de_numeros.append(int(input("Informe um número: ")))

soma = 0

for index in range(0, 7, 1):
    soma += lista_de_numeros[index]

media = soma / 7

contador_numeros_maior_igual_media = 0

for index in range(0, 7, 1):
    if lista_de_numeros[index] >= media:
        contador_numeros_maior_igual_media += 1

print(f"A soma dos sete números é {soma}, a média é {media} e a quantidade "
      f"de números maior ou igual a média é {contador_numeros_maior_igual_media}")