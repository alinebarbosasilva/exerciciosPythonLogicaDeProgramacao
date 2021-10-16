# Crie uma matriz 3x3, onde a primeira coluna terá o nome de um produto, a segunda
# coluna a marca e a terceira o valor. Esses dados não precisam ser informados pelo
# usuário, essas informações podem ser pré-definidas como no exemplo de contatos,
# # assim que desenvolver a matriz, exiba os dados utilizando laços de repetiçã


matriz = [["Pepsi", "Pão de Queijo", "Torta"],
          ["Pepsi", "Padaria", "Padaria"],
          [10.00, 2.00, 5.00]
]

for index_linha in range(0, len(matriz), 1):
    for index_coluna in range(0, len(matriz[index_linha]), 1):
        print(matriz[index_linha][index_coluna])