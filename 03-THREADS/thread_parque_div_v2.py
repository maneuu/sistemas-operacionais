import threading
import time
from os import system

# Criando um lock para controlar o acesso à impressão
lock = threading.Lock()

# Função para simular uma atração
def atracao(nome, tempo_espera):
    for i in range(3):  # Cada atração tem 3 etapas
        with lock:  # Garantir que apenas uma thread imprima de cada vez
            print(f"{nome} está na etapa {i+1} da atração.")
        time.sleep(tempo_espera)  # Espera para simular a execução da atração
    with lock:  # Garantir que a mensagem final seja impressa de forma controlada
        print(f"{nome} terminou a atração!\n")

# Limpa a tela do terminal
system('clear')

# Mostra o número de threads ativas antes de criar as threads para as atrações
print(f"🎢 Threads ativas antes: {threading.active_count()}")

# Criando 3 threads para simular atrações no parque de diversões
montanha_russa = threading.Thread(target=atracao, args=("Montanha Russa", 2))  # 2 segundos por etapa
roda_gigante = threading.Thread(target=atracao, args=("Roda Gigante", 3))  # 3 segundos por etapa
carrossel = threading.Thread(target=atracao, args=("Carrossel", 1))  # 1 segundo por etapa

# Inicia as atrações
montanha_russa.start()
roda_gigante.start()
carrossel.start()

# Mostra quantas threads estão ativas após iniciar as atrações
print(f"🎡 Threads ativas após Start: {threading.active_count()}")

# O programa principal espera todas as atrações terminarem antes de continuar
montanha_russa.join()
roda_gigante.join()
carrossel.join()

# Após todas as atrações terminarem
print(f"🎢 Threads ativas após Join: {threading.active_count()}")

# Mensagem final
print("\n🏰 Parque de Diversões fechado! Obrigado por visitarem!")
