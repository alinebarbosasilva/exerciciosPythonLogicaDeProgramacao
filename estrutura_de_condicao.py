# idade = int(input("Informe sua idade: "))
# possui_cnh = input("Você possui CNH... Informe [S] para sim ou [N] para não: ")
#
# if idade >= 18:
#     if possui_cnh == "S":
#         print("Você é maior de idade e possui CNH, pode dirigir.")
#     else:
#         print("Você é maior de idade mas não possui CNH, portanto não pode dirigir.")
# else:
#     print("Você é menor de idade e ainda não pode dirigir.")

valor_1 = int(input("Informe o primeiro valor: "))
valor_2 = int(input("Informe o segundo valor: "))
operacao = input("Informe a operação matemática que deseja realizar [+][-][*][/]: ")

if operacao == "+":
    resultado = valor_1 + valor_2
    print(f"O resultado da soma é: {resultado}")
elif operacao == "-":
    resultado = valor_1 - valor_2
    print(f"O resultado da subtração é {resultado}")
elif operacao == "*":
    resultado = valor_1 * valor_2
    print(f"O resultado da multiplicação é {resultado}")
else:
    print("A operação informada está inválida.")

