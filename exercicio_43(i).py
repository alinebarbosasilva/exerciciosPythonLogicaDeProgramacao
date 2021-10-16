# Desenvolva um sistema para gerenciar cursos, as funcionalidades pedidas são:
# 1) Cadastrar curso - Pede o nome do novo curso
# 2) Selecionar cursos - Exibe todos os cursos
# 3) Remover curso - Pede o nome do curso e realiza a exclusão
# 4) Sair do sistema - Finaliza o laço

lista_de_cursos = []

while True:
    opcao = int(input("Informe a opão que deseja realizar \n"
                      "1 - Cadastrar novo curso \n"
                      "2 - Selecionar curso \n"
                      "3 - Remover curso \n"
                      "4 - Sair do sistema \n"
                      "Digite aqui: "))
    if opcao == 1:
        lista_de_cursos.append(input("Informe o nome do novo curso: "))
    elif opcao == 2:
        print("Os cursos disponíveis são: ")
        for index in range(0, len(lista_de_cursos), 1):
            print(lista_de_cursos[index])
    elif opcao == 3:
        for index in range(0, len(lista_de_cursos), 1):
            print(lista_de_cursos[index])
        curso_a_remover = input("Informe o curso que deseja remover: ")
        for index in range(0, len(lista_de_cursos), 1):
            if lista_de_cursos[index] == curso_a_remover:
                lista_de_cursos.pop(index)
                print(f"Curso {curso_a_remover} foi removido com sucesso...")
    elif opcao == 4:
        print("Sistema finalizado...")
        break
    else:
        "A opção informada não existe..."
