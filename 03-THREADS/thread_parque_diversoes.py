import threading
import time
from os import system

# Função para simular uma atração
def atracao(nome, tempo_espera):
    for i in range(3):  # Cada atração tem 3 etapas
        print(f"{nome} está na etapa {i+1} da atração.")
        time.sleep(tempo_espera)  # Espera para simular a execução da atração
    print(f"{nome} terminou a atração!\n")

# Limpa a tela do terminal
system('clear')

# Mostra o número de threads ativas antes de criar as threads para as atrações
print(f"🎢 Threads ativas antes: {threading.active_count()}")

# Criando 3 threads para simular atrações no parque de diversões
montanha_russa = threading.Thread(target=atracao, args=("Montanha Russa", 10))  # 2 segundos por etapa
roda_gigante = threading.Thread(target=atracao, args=("Roda Gigante", 10))  # 3 segundos por etapa
carrossel = threading.Thread(target=atracao, args=("Carrossel", 10))  # 1 segundo por etapa

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
