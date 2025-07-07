# trabalhoredes
trabalho de redes 

p1:
pergunta o ip da maquina de p2, quantas matrizes e em seguida o tamanho das matrizes.
o tempo começa a contar logo depois do tamanho ser informado.
A matriz é criada e enviada junto com o tempo e o numero de matrizes via tcp para 192.168.124.2 porta 6000.
A criação e envio é repetido baseado no numero de matrizes.

p2:
pergunta o ip da maquina de p3.
recebe pela porta 6000.
calcula a matriz inversa 
calcula o determinante da matriz invertida
envia para p3 porta 6001.
repete baseado no numero de matrizes.

p3:
recebe pela porta 6001.
repete baseado no numero de matrizes.
calcula o tempo total.

instrução:
primeira vez:

na maquina de p3:
```
docker pull vitorguerzet/trabredes:ptres
```
```
docker run -p 6001:6001 -it --rm --name bazinga vitorguerzet/trabredes:ptres
```
na maquina de p2:
```
docker pull vitorguerzet/trabredes:pdois
```
```
docker run -p 6000:6000 -p 6001:6001 -it --rm --name bazinga vitorguerzet/trabredes:pdois
```
na maquina de p1:
```
docker pull vitorguerzet/trabredes:pum
```
```
docker run -p 6000:6000 -it --rm --name bazinga vitorguerzet/trabredes:pum
```
insira os valores desejados em p1 e p2.
os resultados estarao em p3.

para rodar novamente:

na maquina de p3:
```
docker run -p 6001:6001 -it --rm --name bazinga vitorguerzet/trabredes:ptres
```
na maquina de p2:
```
docker run -p 6000:6000 -p 6001:6001 -it --rm --name bazinga vitorguerzet/trabredes:pdois
```
na maquina de p1:
```
docker run -p 6000:6000 -it --rm --name bazinga vitorguerzet/trabredes:pum
```
Para criar novas imagens a partir do codigo:
Com os arquivos do diretório p1:
```
docker build -t pum .
```
Com os arquivos do diretório p2:
```
docker build -t pdois .
```
Com os arquivos do diretório p3:
```
docker build -t ptres .
```
Para mandar para o docker hub:
logar na maquina:
```
docker login <usuáro>
```
adicionar tag na imagem para o diretório no docker hub
```
docker tag <usuario>/<diretorio>:<imagem>
```
```
docker tag vitorguerzet/trabredes:pum
```
```
docker tag vitorguerzet/trabredes:pdois
```
```
docker tag vitorguerzet/trabredes:ptres
```
fazer push para o diretorio no docker hub
```
docker push <usuario>/<diretorio>:<imagem>
```
```
docker push vitorguerzet/trabredes:pum
```
```
docker push vitorguerzet/trabredes:pdois
```
```
docker push vitorguerzet/trabredes:ptres
```


