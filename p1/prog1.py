import socket
import time
import numpy as np
import pickle
h=input("digite o ip de p2:")
HOST = h
PORT = 6000
k = int(input("Digite o numero de matrizes:"))

n = int(input("Digite o tamanho da matriz quadrada: "))

start_time = time.time()
for i in range (k):

    matriz = np.random.randint(1, 10, (n, n))

    data = {
        'matriz': matriz,
        'start': start_time,
        'k' : k
    }

    tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp.connect((HOST, PORT))
    tcp.send(pickle.dumps(data))
    tcp.close()

print('Matrizes enviadas. Fim.')








