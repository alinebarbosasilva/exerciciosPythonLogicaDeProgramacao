horario_brasil = int(input("Informe a hora atual no Brasil: "))
selecao_paises = input("Infome o país que gostaria de saber o horário: [1 = Japao ] [2 = Portugal] [3 = Russia] ")

diferenca_japao = 12
diferenca_portugal = 4
diferenca_russia = 6 

if selecao_paises == "1":
    hora_japao = horario_brasil + diferenca_japao
    if hora_japao > 24:
        hora_japao = hora_japao - 24
    print(f"A hora atual no Brasil é {horario_brasil} e no Japão é: {hora_japao}")    

elif selecao_paises == "2":
    hora_portugal = horario_brasil + diferenca_portugal
    if hora_portugal > 24:
        hora_portugal = hora_portugal - 24
    print(f"A hora atual no Brasil é {horario_brasil} e em Portugal é: {hora_portugal}")

elif selecao_paises == "3":
    hora_russia = horario_brasil + diferenca_russia
    if hora_russia > 24:
        hora_russia = hora_russia - 24 
    print(f"A hora atual no Brasil é {horario_brasil} e na Russia é: {hora_russia}")

else: 
    print("A opção informada está Inválida.")



# O usuário informa o horário atual no Brasil (apenas hora), em seguida
# informa um país. Retorne o horário daquele país se baseando pela hora
# informada.