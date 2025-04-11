import os

while True:
    opcoes = """
    Menu de Comandos CMD:
    1 - Ver data atual
    2 - Ver hora atual
    3 - Mostrar nome do computador
    4 - Mostrar lista de arquivos do diretório atual
    5 - Limpar a tela
    6 - Sair
    """
    print(opcoes)
    
    try:
        comando_escolhido = int(input("Escolha uma opção: "))
        os.system("cls")
        if comando_escolhido == 1:
            print("Exibindo a data atual do sistema...\n")
            os.system("date")
        elif comando_escolhido == 2:
            print("Exibindo a hora atual do sistema...\n")
            os.system("time")
        elif comando_escolhido == 3:
            print("Exibindo o nome do computador...\n")
            os.system("hostname")
        elif comando_escolhido == 4:
            print("Listando os arquivos do diretório atual...\n")
            os.system("dir")
        elif comando_escolhido == 5:
            print("Limpando a tela...\n")
            os.system("cls")
        elif comando_escolhido == 6:
            print("Encerrando o programa. Até mais!")
            break
        else:
            print("Opção inválida. Tente novamente.\n")
    except ValueError:
        print("Por favor, digite apenas números.\n")

    print()
    print("=" * 50)
    print()