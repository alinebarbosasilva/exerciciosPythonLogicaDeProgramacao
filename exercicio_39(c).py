alessandra = 0
caio = 0
geraldo = 0
talita = 0

while True:
    opcoes = int(input("Informe qual o seu candidato: [1] Alessandra, [2] Caio, [3] Geraldo, [4] Talita, [5] Sair: "))
    if opcoes == 1:
        alessandra += 1
    elif opcoes == 2:
        caio += 1
    elif opcoes == 3:
        geraldo += 1
    elif opcoes == 4:
        talita += 1
    elif opcoes == 5:
        break

print(f"O candidadto Alessandra teve {alessandra} votos")
print(f"O candidadto Caio teve {caio} votos")
print(f"O candidadto Geraldo teve {geraldo} votos")
print(f"O candidadto Talita teve {talita} votos")

# Crie um pequeno sistema de votação, exiba em um prompt() as opções:
# # 1 - Alessandra
# # 2 - Caio
# # 3 - Geraldo
# # 4 - Talita
# # 5 - Sair
# # Enquanto não for digitado o número 5 o laço deverá realizar a ação de
# # prompt() para pedir o voto e contabilizar para o candidato. Quando
# # informado o número 5 retorne a quantidade de votos que cada candidato
# # obteve.