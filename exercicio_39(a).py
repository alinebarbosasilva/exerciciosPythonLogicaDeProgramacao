tabuada_escolhida = int(input("Informe o numero para ser a tabuada: "))

for contador in range(1, 11, 1):
    print(contador)
    resultado = tabuada_escolhida * contador
    print(f"{tabuada_escolhida} x {contador} = {tabuada_escolhida * contador}")

