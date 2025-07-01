# trabalhoredes
trabalho de redes 

c1:
pergunta quantas matrizes e em seguida o tamanho das matrizes.
o tempo começa a contar logo depois do tamanho ser informado.
A matriz é criada e enviada junto com o tempo e o numero de matrizes via tcp para 192.168.124.2 porta 6000.
A criação e envio é repetido baseado no numero de matrizes.

g1:
recebe pela porta 6000.
calcula a matriz inversa e envia para 192.168.124.66 porta 6001.
repete baseado no numero de matrizes.

g2:
recebe pela porta 6001.
calcula o determinante da matriz invertida.
repete baseado no numero de matrizes.
calcula o tempo total.

