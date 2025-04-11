import os

diretorio = input("Digite o caminho completo de um diretório: ")
try:
    arquivos = os.listdir(diretorio)
    print(f"\nArquivos encontrados em {diretorio}:")
    for arquivo in arquivos:
        print(arquivo)
except FileNotFoundError:
    print("Diretório não encontrado.")
except PermissionError:
    print("Você não tem permissão para acessar este diretório.")
    print ("\n Fim de Programa")


# exemplo de input : Z:\20242370034\Desktop 