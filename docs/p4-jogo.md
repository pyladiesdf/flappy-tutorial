## Jogo

Até agora conseguimos desenhar algumas coisas na tela, fazer animações simples e ler entradas do usuário. São elementos básicos de um jogo, mas ainda faltam alguns detalhes importantes. Primeiramente, o nosso método de animação usando o laço for é bastante rudimentar: ele não dá controle total para o Pyxel fazer todas as tarefas necessárias para executar um jogo, como controle da taxa de atualização, tocar sons, entrada do usuário, etc. Além disso, nosso código está bastante desorganizado e sem estrutura, o que pode crescer para uma macarronada incompreensível de linhas de código na medida que acrescentamos novas funcionalidades.

O Pyxel organiza um jogo de forma bastante simples. Primeiro inicializamos os parâmetros e damos valores iniciais às variáveis. Depois, temos que orientar o Pyxel sobre como ele deve atualizar as variáveis de jogo e de como deve desenhar na tela dado o valor destas variáveis. Isto é feito definido duas funções chamadas "update" e "draw". Toda lógica do jogo fica portanto codificada dentro destas duas funções: "update" lê as entradas do usuário e atualiza o estado do jogo de acordo e a função "draw" desenha uma determinada configuração na tela.

### Criando funções

Na nossa jornada até agora apenas utilizamos funções definidas por outras pessoas. Vamos dar um passo importante e aprender a criar nossas próprias funções. Organizar o código em funções é uma das habilidades mais importantes da programação. É o que permite seu código ser compreensível, reutilizável, adaptável e com menos defeitos. Uma função, em Python, basicamente agrega um conjunto de instruções. O código abaixo desenha uma casa, e corresponde a uma sequência simples de comandos:

```python
pyxel.rect(90, 90, 70, 35, 15)   # parede
pyxel.rect(97, 100, 15, 25, 2)   # porta
pyxel.rect(117, 100, 15, 15, 2)  # janela 1
pyxel.rect(137, 100, 15, 15, 2)  # janela 2
pyxel.rect(85, 70, 80, 20, 4)    # telhado
```

Isto não é uma função e toda vez que precisarmos utilizar este código seria necessário copiar e colar esta sequência de instruções. A função que desenha uma casa seria muito parecida, mas colocamos todas as instruções dentro de um bloco "def":

```python
def desenhar_casa():
    pyxel.rect(90, 90, 70, 35, 15)   # parede
    pyxel.rect(97, 100, 15, 25, 2)   # porta
    pyxel.rect(117, 100, 15, 15, 2)  # janela 1
    pyxel.rect(137, 100, 15, 15, 2)  # janela 2
    pyxel.rect(85, 70, 80, 20, 4)    # telhado
```

Apesar da lista de comandos ser basicamente idêntica, existe uma diferença grande entre o primeiro caso e o segundo: no primeiro, cada comando é executado imediatamente e portanto já influencia no resultado que seria mostrado na tela. No segundo caso, apenas criamos uma **definição** ou **especificação** de como se desenha uma casa, mas nenhum comando é, de fato, executado. É necessário invocar a função `desenhar_casa()` em algum ponto do código para realmente executar estes comandos.

```python
# Definimos a função como antes
def desenhar_casa():
    ... 

# Invocamos a função para executar os comandos
desenhar_casa()
```

#### Argumentos de funções

O que aconteceria se invocarmos a função `desenhar_casa()` várias vezes? Desenharia várias casas? Em princípio sim. Esta é uma das grandes utilidades de funções: poder executar o mesmo código várias vezes. No nosso caso, no entanto, cada chamada de função desenhará cada casa exatamente por cima da anterior e o efeito final seria muito parecido como se a função tivesse sido chamada apenas uma vez.

O fato é que algumas funções só são realmente úteis se for possível passar diferentes valores de alguns parâmetros para que ela execute instruções ligeiramente diferentes a cada execução. No caso da casa, por exemplo, poderíamos controlar a posição da casa para poder desenhar várias casas em posições diferentes do cenário.

Se estivéssemos pensando como sequência de instruções, seria possível reorganizar o código mais ou menos da seguinte maneira:

```python
x = 85
y = 70

pyxel.rect(x + 10, y + 20, 70, 35, 15) # parede
pyxel.rect(x + 12, y + 30, 15, 25, 2)  # porta
pyxel.rect(x + 32, y + 30, 15, 15, 2)  # janela 1
pyxel.rect(x + 52, y + 30, 15, 15, 2)  # janela 2
pyxel.rect(x, y, 80, 20, 4)            # telhado
```

Desta forma, basta mudar o valor das variáveis x e y para alterar toda a sequência de comandos. Adaptar esta idéia para funções é muito simples. Vamos forçar que x e y sejam dados como argumentos para a função de forma que o usuário precise chamar a função como `desenhar_casa(x, y)`.

Para declarar uma função com argumentos, basta incluir o nome das variáveis na ordem correta na primeira linha de um comando `def`:

```python
def desenhar_casa(x, y):
    pyxel.rect(x + 10, y + 20, 70, 35, 15) # parede
    pyxel.rect(x + 12, y + 30, 15, 25, 2)  # porta
    pyxel.rect(x + 32, y + 30, 15, 15, 2)  # janela 1
    pyxel.rect(x + 52, y + 30, 15, 15, 2)  # janela 2
    pyxel.rect(x, y, 80, 20, 4)            # telhado
```

Agora o usuário é forçado a dar um valor para x e y e para cada par (x, y) fornecido, desenhamos uma casa diferente. Ou seja, a partir da nossa função de desenhar casa, podemos começar a construir uma cidade!

```python
import pyxel

def desenhar_casa(x, y):
    pyxel.rect(x + 5, y + 20, 70, 35, 15)  # parede
    pyxel.rect(x + 12, y + 30, 15, 25, 2)  # porta
    pyxel.rect(x + 32, y + 30, 15, 15, 2)  # janela 1
    pyxel.rect(x + 52, y + 30, 15, 15, 2)  # janela 2
    pyxel.rect(x, y, 80, 20, 4)            # telhado

# Pyxel
pyxel.init(200, 150)

# Ruas cinzas
pyxel.cls(5)

# Linha amarela
for x in range(0, 200, 30):
    pyxel.rect(x, 3, 15, 2, 10)

# Quarteirão de grama
pyxel.rect(20, 25, 180, 125, 3)

# Algumas casinhas...
desenhar_casa(25, 30)
desenhar_casa(25, 90)
desenhar_casa(115, 30)
desenhar_casa(115, 90)

# Desenha
pyxel.show()
```


### Flappy Bird

Agora é a hora de finalmente começar a programar o nosso Flappy Bird!


```python
import pyxel

# Constantes
LARGURA = 220
ALTURA = 220

# Variáveis
pos_x = LARGURA / 2
pos_y = ALTURA / 2


def update():
    ...


def draw():
    pyxel.cls(12)
    pyxel.rect(pos_x, pos_y, 20, 20, 10)


pyxel.init(LARGURA, ALTURA, fps=35)
pyxel.run(update, draw)
```
