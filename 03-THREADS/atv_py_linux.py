import threading,time
from os import system

def tarefa(msg,t):
    for i in range(5):
        print (msg)
        time.sleep(5)
        
system('clear')
print("\nThreads ativas antes: ", threading.active_count())
# Crie duas threads
r = threading.Thread(target=tarefa, args=('\nThread R sendo executada',4))
t = threading.Thread(target=tarefa, args=('\nThread T sendo executada',4))
# Inicie as threads
r.start()
t.start()
print("\nThreads ativas após Start: ", threading.active_count())
# Aguarde até que ambas as threads terminem
r.join()
t.join()
print("\nThreads ativas após Join: ", threading.active_count())
print("\nPrograma principal concluído.")