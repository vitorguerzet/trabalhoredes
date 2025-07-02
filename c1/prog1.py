  GNU nano 4.8                        prog1.py                                  
import socket
import time
import numpy as np
import pickle

HOST = '192.168.124.2'
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

print('fim.')








