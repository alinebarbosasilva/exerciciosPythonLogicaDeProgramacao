contador = 0

while True:
    contador += 1
    print(contador)

    opcao = input("Deseja parar o laço:\n"
          "1 - Sim\n"
          "2 - Nao\n"
          "DIGITE AQUI: ")

    if opcao == "1":
        break

print("Acabou meu código")

