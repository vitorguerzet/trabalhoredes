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

instrução:
primeira vez:

na maquina de ip 192.168.124.66(g2):
docker pull vitorguerzet/trabredes:ptres
docker run -p 6001:6001 -it --rm --name bazinga vitorguerzet/trabredes:ptres

na maquina de ip 192.168.124.2(g1):
docker pull vitorguerzet/trabredes:pdois
docker run -p 6000:6000 -p 6001:6001 -it --rm --name bazinga vitorguerzet/trabredes:pdois

na maquina de ip 192.168.124.1(c1):
docker pull vitorguerzet/trabredes:pum
docker run -p 6000:6000 -it --rm --name bazinga vitorguerzet/trabredes:pum

insira os valores desejados em c1.
os resultados estarao em g2.

para rodar novamente:

na maquina de ip 192.168.124.66(g2):

docker run -p 6001:6001 -it --rm --name bazinga vitorguerzet/trabredes:ptres

na maquina de ip 192.168.124.2(g1):

docker run -p 6000:6000 -p 6001:6001 -it --rm --name bazinga vitorguerzet/trabredes:pdois

na maquina de ip 192.168.124.1(c1):

docker run -p 6000:6000 -it --rm --name bazinga vitorguerzet/trabredes:pum
