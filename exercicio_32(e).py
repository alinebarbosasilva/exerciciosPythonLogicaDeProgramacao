
#Equilátero = todos os lados iguais
#Escaleno = todos os lados diferentes
#Isosceles = dois lados iguais e um diferente 


largura_1 = int(input("Informe a largura direita do triângulo: "))
largura_2 = int(input("Informe a largura inferior do triângulo: ")) 
largura_3 = int(input("Informe a largura esquerda do triângulo: "))

if largura_1 == largura_2 == largura_3:
    print("Seu tipo de triângulo é Equilátero")
elif largura_1  != largura_2 != largura_3: 
    print("Seu tipo de triângulo é Escaleno")
elif largura_1 == largura_2 != largura_3 or largura_3 == largura_2 != largura_1:
    print("Seu tipo de triângulo é Isósceles")
else: 
    print("Inválido")
