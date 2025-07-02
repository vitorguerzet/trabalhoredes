import socket
import pickle
import numpy as np
import time

HOST = ''
PORT = 6001

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp.bind((HOST, PORT))
tcp.listen(1)
i=0
while True:
    i=i+1
    print("p3 aguardando matriz invertida...")

    con, addr = tcp.accept()
    packet=[]
    while True:
        parte = con.recv(4096)
        if not parte: break
        packet.append(parte)
    data=pickle.loads(b"".join(packet))

    matriz = data['matriz']
    start_time = data['start']
    k=data['k']
    det=data['det']
    con.close()

    #det = np.linalg.det(matriz)
    print("Matriz invertida:", matriz)
    print("Determinante:", det)
    if k==i: break
end_time = time.time()
tempo_total = end_time - start_time

print("Tempo total (s):", tempo_total)




