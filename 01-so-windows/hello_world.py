import os
import socket
username = os.getlogin()
hostname = socket.gethostname()
print(f"Olá, {username}! Seja bem-vindo ao sistema {hostname}.")


"""
Explicação:
o os.getlogin(): Obtém o nome do usuário logado atualmente.
o socket.gethostname(): Obtém o nome do host (nome do
computador).
o A mensagem de saudação é personalizada com essas
informações, mostrando automaticamente ao usuário com o qual
o programa está interagindo.
"""