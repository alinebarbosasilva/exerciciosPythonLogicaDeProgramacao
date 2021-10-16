# 1º passo: Valor * % = ValorDividido/100 = ValorDesconto
# 2º passo: Valor – ValorDesconto = Vfinal

segmentos_produtos = int(input("Informe qual é o tipo de segmento [1 = Vestuário] [2 = Eletrônico] [3 = Alimentício]: "))
produto_selecionado = (input("Qual o nome do produto: "))
valor_produto = float(input("Informe o valor do produto: "))

if segmentos_produtos == 1:
    desconto_valor = (valor_produto * 5 ) / 100
    resultado_desconto =  valor_produto - desconto_valor 
    print(f"O produto com 5% de desconto custa : {resultado_desconto}") 

elif segmentos_produtos == 2:
    desconto_valor = (valor_produto * 8 ) / 100
    resultado_desconto =   valor_produto - desconto_valor
    print(f"O produto com 8% de desconto custa : {resultado_desconto}") 

elif segmentos_produtos == 3:
    desconto_valor = (valor_produto * 10 ) / 100
    resultado_desconto =  valor_produto - desconto_valor 
    print(f"O produto com 10% de desconto custa : {resultado_desconto}") 
else:
    print("Inválido")       