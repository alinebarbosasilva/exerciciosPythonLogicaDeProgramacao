# Crie um formulário, onde o usuário irá informar dois valores e uma operação
# de soma, subtração, multiplicação ou divisão.
# Haverá as seguintes funções:
# 1) Ação - Responsável por obter os dados informados, selecionar um cálculo e exibir
# 2) Soma - Haverá dois parâmetros que retornará a soma dos valores
# 3) Subtração - Haverá dois parâmetros que retornará a subtração dos valores
# 4) Multiplicação - Haverá dois parâmetros que retornará a multiplicação dos valores
# 5) Divisão - Haverá dois parâmetros que retornará a divisão dos valores

def calculadora1(numero1, numero2):
    soma = numero1 + numero2
    return soma

def calculadora2(numero1, numero2):
    subtracao = numero1 - numero2
    return subtracao


def calculadora3(numero1, numero2):
    multiplicacao = numero1 * numero2
    return multiplicacao


def calculadora4(numero1, numero2):
    divisao = numero1 / numero2
    return divisao


while True:
    opcoes = input("Escolha qual operação você gostaria de realizar: [SOMA], [SUBTRACAO], [MULTIPLICACAO], [DIVISAO]: ")

    if opcoes == "SOMA":
        valor1 = int(input("Informe um valor: "))
        valor2 = int(input("Informe um valor: "))
        resultado = calculadora1(valor1,valor2)
        print(f"O resultado da soma é  {resultado}")

    elif opcoes == "SUBTRACAO":
        valor1 = int(input("Informe um valor: "))
        valor2 = int(input("Informe um valor: "))
        resultado = calculadora2(valor1, valor2)
        print(f"O resultado da subtração é  {resultado}")

    elif opcoes == "MULTIPLICACAO":
        valor1 = int(input("Informe um valor: "))
        valor2 = int(input("Informe um valor: "))
        resultado = calculadora3(valor1, valor2)
        print(f"O resultado da multiplicação é  {resultado}")

    elif opcoes == "DIVISAO":
        valor1 = int(input("Informe um valor: "))
        valor2 = int(input("Informe um valor: "))
        resultado = calculadora4(valor1, valor2)
        print(f"O resultado da soma é  {resultado}")

    else:
        print("Informação inválida")
    break
