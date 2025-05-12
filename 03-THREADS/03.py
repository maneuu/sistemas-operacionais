import threading
import time

# Função a ser executada pela thread
def tarefa(nome):
    for i in range(3):
        print(f"{nome} executando passo {i + 1}")
        time.sleep(1)

# Criar threads
t1 = threading.Thread(target=tarefa, args=("Thread 1",))
t2 = threading.Thread(target=tarefa, args=("Thread 2",))

# Iniciar as threads
t1.start()  # Chama start(), isso começa a execução da thread
t2.start()  # Chama start(), isso também começa a execução da segunda thread

# O programa principal continuará rodando ao mesmo tempo que as threads
print("Programa principal continua rodando...")

# Aguardar as threads terminarem
t1.join()
t2.join()

print("Todas as threads terminaram.")
