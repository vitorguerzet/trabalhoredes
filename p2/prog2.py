import socket
import pickle
import numpy as np

HOST = ''
PORT = 6000

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp.bind((HOST, PORT))
tcp.listen(1)
i=0
h=input("digite o ip de p3: ")
while True:
    i=i+1
    print("p2 aguardando matriz...")

    con, addr = tcp.accept()
    packet=[]
    while True:
        parte = con.recv(4096)
        if not parte: break
        packet.append(parte)
    data=pickle.loads(b"".join(packet))
    matriz = data['matriz']
    start_time = data['start']
    con.close()

    matriz_invertida = np.transpose(matriz)
    det=np.linalg.det(matriz_invertida)
    data2 = {
        'matriz': matriz_invertida,
        'start': start_time,
        'k' : data['k'],
        'det' : det
    }

#    print(data2['det'])
    tcp2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp2.connect((h, 6001))
    tcp2.send(pickle.dumps(data2))
    tcp2.close()
    k = data['k']
    if k==i: break
print('Determinantes encontradas. Fim.')




