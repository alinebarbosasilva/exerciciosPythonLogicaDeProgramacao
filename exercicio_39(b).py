
numero_inicial = int(input("Informe o número inicial: "))
numero_final = int(input("Informe o número final: "))

for index in range(numero_inicial, numero_final + 1, 1):
    if index % 2 == 0:
        print(f"O número {index} é par")
    else:
        print(f"O número {index} é impar")

# O usuário informa um número inicial e um número final, em seguida retorne a
# quantidade de pares e ímpares daquela cadeia de valores.
# Vamos supor que os números informados foram: 6 e 12, sendo assim serão 4
# pares (6, 8, 10 e 12) e 3 ímpares (7, 9 e 11).
