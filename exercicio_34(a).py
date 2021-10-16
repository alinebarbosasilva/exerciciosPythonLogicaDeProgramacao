# 0 °C = 32 °F
# 1 °C = 33,8 °F 
# 5 °C = 41 °F
# 10 °C = 50 °F
# 15 °C = 59 °F
# 20 °C = 68 °F
# 25 °C = 77 °F
# 30 °C = 86 °F
# 35 °C = 95 °F
# 40 °C = 104 °F

selecione_conversão = float(input("Selecione o tipo de conversão: [1 = Fahrenheit ] e [2 = Celsius] "))
valor_temperatura = float(input("Informe a temperatura que você gostaria de converter: "))

if selecione_conversão == 1:
    temperatura = (valor_temperatura * 1.8) + 32
    print(f"A temperatura em Fahrenheit é: {temperatura}")

elif selecione_conversão == 2:
    temperatura = (valor_temperatura - 32) / 1.8
    print(f"A temperatura em Celsius é: {temperatura}")

else:
    print("Inválido")


