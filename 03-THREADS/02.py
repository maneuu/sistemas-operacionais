import threading
import time

# Função que será executada por cada thread
def tarefa(nome):
    for i in range(3):
        print(f"[{nome}] executando passo {i + 1}")
        time.sleep(2)  # Pausa de 2 segundos

# Mostrar quantas threads estão ativas no começo
print("Threads ativas no início:", threading.active_count())

# Criar duas threads
thread1 = threading.Thread(target=tarefa, args=("Thread 1",))
thread2 = threading.Thread(target=tarefa, args=("Thread 2",))

# Iniciar as threads
thread1.start()
thread2.start()

print("Threads ativas após iniciar:", threading.active_count())

# Esperar as threads terminarem
thread1.join()
thread2.join()

print("Todas as threads terminaram.")
print("Threads ativas no final:", threading.active_count())
