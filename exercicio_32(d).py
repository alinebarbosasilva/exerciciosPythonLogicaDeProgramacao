numero_1 = int(input("Informe o primeiro número: "))
numero_2 = int(input("Informe o segundo número: "))
numero_3 = int(input("Informe o terceiro número: "))

if numero_1 < numero_2:
    if numero_1 < numero_3:
        print(numero_1)
    else:
        print(numero_3)

elif numero_2 < numero_1:
    if numero_2 < numero_3:
        print(numero_2)
    else:
        print(numero_3)

elif numero_3 < numero_1:
    if numero_3 < numero_2:
        print(numero_3)
    else:
        print(numero_2)
