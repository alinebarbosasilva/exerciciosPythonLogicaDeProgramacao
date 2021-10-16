#Cotações do dia 05/10/21

opcoes_conversor = float(input("Informe qual conversão você gostaria de realizar: [1 = Real para Dólar] [2 = Dólar para Real] [3 = Real para Euro] [4 = Euro para Real]: "))
valor_converta = float(input("Insira o valor: "))

if opcoes_conversor == 1:
    resultado_conversao = valor_converta * 0.18 
    print(f"O valor de Real para Dolár é {resultado_conversao} ")

elif opcoes_conversor == 2: 
    resultado_conversao = valor_converta * 5.46
    print(f"O valor em Dolar para Real é {resultado_conversao} ")

elif opcoes_conversor == 3:
    resultado_conversao = valor_converta * 0.16
    print(f"O valor em Real para Euro é {resultado_conversao}")

elif opcoes_conversor == 4:
    resultado_conversao = valor_converta * 6.33
    print(f"O valor em Euro para Real é {resultado_conversao}")
else:
    print("Inválido")    