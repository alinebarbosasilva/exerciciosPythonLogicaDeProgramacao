escolha = int(input("Informe o código do produto escolhido: número  [1 = Pizza] [2 = Pão de Queijo] [3 = Macarrão]"))
valor_pago = int(input("Informe o valor pago: "))

if escolha == 1:
    if valor_pago < 12.00:
        print("Seu pagamento é insuficiente para realizar a compra")
    else:
        troco = valor_pago - 12.00
        print(f"Esse é o seu troco: {troco}")

elif escolha == 2:
    if valor_pago < 4.00:
        print("Seu pagamento é insuficiente para realizar a compra")
    else:
        troco = valor_pago - 4.00
        print(f"Esse é o seu troco: {troco}")
elif escolha == 3:
    if valor_pago < 16.00:
        print("Seu pagamento é insuficiente para realizar a compra")
    else:
        troco = valor_pago - 16.00
        print(f"Esse é o seu troco: {troco}")
else:
    print("Produto não existe.")



