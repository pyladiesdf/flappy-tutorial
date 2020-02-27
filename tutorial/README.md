Arquivo com o esqueleto do tutorial

# Ambiente de programação

Apresentar as ferramentas e apontar para instruções de instalação do kit básico:

- Python 3.7+
- VScode
- Pyxel
- Módulo auxiliar flappy.py
- Arquivo de imagens data.pyres


# Iniciando o jogo 

- Importar módulos (flappy e pyxel)
- Chamando funções (flappy.comecar())
- Definido variáveis (largura_tela, altura_tela, gravidade, pulo, ...)

```python
import flappy
import pyxel

flappy.comecar()
```


# Desenhando na tela

- Definindo funções com o def

```python
def desenhar():
    desenhar_fundo()
    desenhar_nuvens()
    desenhar_canos()
    desenhar_chao()
    desenhar_flappy()
    desenhar_instrucoes()
```

- Comentando funções
- pyxel.cls() - cor do fundo + descrição das cores no pyxel
- Operador de mod (%) e pyxel.frame_count
- def desenhar_flappy(): retângulo -> blit
- apresentar o pyxeledit no caminho

```python
def desenhar_flappy():
    largura = 17
    altura = 13
    cor = 10
    pyxel.rect(flappy_x, flappy_y, largura, altura, cor)


def desenhar_flappy():
    img = 0
    u = 0
    v = 0
    largura = 17
    altura = 13
    mascara = 0
    pyxel.blt(flappy_x, flappy_y, img, u, v, largura, altura, mascara)


def desenhar_flappy():
    frame = (pyxel.frame_count // 4) % 3
    img = 0
    u = 0
    v = frame * 16
    largura = 17
    altura = 13
    mascara = 0
    pyxel.blt(flappy_x, flappy_y, img, u, v, largura, altura, mascara)
```

- desenhar_chao() e a função pyxel.bltm()

```python
def desenhar_chao():
    altura = 16
    cor = 11
    pyxel.rect(0, altura_tela - altura, largura_tela, altura, cor)


def desenhar_chao():
    offset = -pyxel.frame_count % largura_tela
    pyxel.bltm(offset, altura_tela - 16, 0, 0, 0, 32, 3)
    pyxel.bltm(offset - largura_tela, altura_tela - 16, 0, 0, 0, 32, 3)

```

- desenhar_instrucoes() e função pyxel.text() e depois comando "if"

```python
def desenhar_instrucoes():
    cor = 7
    msg = "OLA! BEM VINDA AO FLAPPY BIRD!"
    x = largura_tela // 2 - len(msg) * 2
    y = altura_tela // 3
    pyxel.text(x, y, msg, cor)


def desenhar_instrucoes():
    cor = 7

    if not ativo:
        msg = "APERTE ESPACO OU SETA PARA CIMA PARA COMECAR"
    else:
        msg = str(score)
    if morto:
        msg = "Aperte R para reiniciar"
    
    x = largura_tela // 2 - len(msg) * 2
    y = altura_tela // 3
    pyxel.text(x, y, msg, cor)
```


- desenhar_canos() - for

```python
def desenhar_canos():
    cor = 11
    largura = 25
    altura = 135
    for (x, y) in canos:
        pyxel.rect(x, y, largura, altura, cor)
        pyxel.rect(x, y + abertura_cano, largura, altura, cor)


def desenhar_canos():
    for (x, y) in canos:
        pyxel.blt(x, y, 1, 0, 0, 25, 150, 0)
        pyxel.blt(x, y + abertura_cano, 1, 0, 0, -25, -150, 0)
``` 


- desenhar nuvem com paralaxe (avançado: mostra o código e pula)

```python
def desenhar_nuvens():
    offset = -pyxel.frame_count // 2
    pyxel.blt(offset % (largura_tela + 32) - 32, altura_tela // 2, 2, 0, 16, 32, 32, 12)
    pyxel.blt((offset + 96) % (largura_tela + 32) - 32, altura_tela // 4, 2, 0, 48, 32, 32, 12)
    pyxel.blt(offset % (largura_tela + 32) - 64, int(altura_tela / 1.5), 2, 0, 80, 32, 32, 12)
```



# Lógica do jogo

- Começamos com a função básica de atualizar o jogo

```python
def atualizar_jogo():
    atualizar_flappy()
    atualizar_canos()
    atualizar_colisoes()
    atualizar_score()
```

- def atualiza_score() e variáveis globais (começa pela mais fácil!)

```python
score = 0

def atualizar_score():
    global score

    for (x, y) in canos:
        if flappy_x == x:
            score += 1
```

- atualizar_flappy(): gravidade / pyxel.btnp() / controle do estado de morto

```python
flappy_x = largura_tela / 3
flappy_y = altura_tela / 2
velocidade = 0
morto = False


def atualizar_flappy():
    global velocidade, flappy_x, flappy_y

    velocidade += gravidade
    flappy_y += velocidade


def atualizar_flappy():
    global velocidade, flappy_x, flappy_y

    pulando = pyxel.btnp(pyxel.KEY_SPACE) or pyxel.btnp(pyxel.KEY_UP)
    velocidade += gravidade
    if pulando:
        velocidade = -pulo
    flappy_y += velocidade


def atualizar_flappy():
    global velocidade, flappy_x, flappy_y

    pulando = pyxel.btnp(pyxel.KEY_SPACE) or pyxel.btnp(pyxel.KEY_UP)
    velocidade += gravidade
    if pulando and not morto:
        velocidade = -pulo
    flappy_y += velocidade

    # Limita velocidade e impõe deslocamento quando jogador morrer
    flappy_y = min(flappy_y, altura_tela - 29)
    if morto:
        flappy_x -= 1
```

- atualizar_canos(): listas (inserção e seleção por índice) randrange()

```python
from random import randrange

espaco = 80
canos = [
    (0 * espaco + largura_tela, randrange(-100, 0, 10)),
    (1 * espaco + largura_tela, randrange(-100, 0, 10)),
    (2 * espaco + largura_tela, randrange(-100, 0, 10)),
    (3 * espaco + largura_tela, randrange(-100, 0, 10)),
]
```


```python
def atualizar_canos():
    for i in range(4):
        x, y = canos[i]
        canos[i] = (x - 1, y)

def atualizar_canos():
    espaco_x = 80 

    for i in range(4):
        x, y = canos[i]
        if x < -80:
            x = x + espaco_x * 4
            y = randrange(-100, 0, 10)
        canos[i] = (x - 1, y)
```

- atualiza_colisoes(): colisão com os extremos da tela e com os canos

```python
def atualizar_colisoes():
    global morto

    if flappy_y > altura_tela - 30:
        morto = True


def atualizar_colisoes():
    global morto

    if flappy_y > altura_tela - 30:
        morto = True

    for (x, y) in canos:
        colide_x = x + 12.5 > flappy_x > x - 12.5
        colide_y = flappy_y > y + abertura_cano or flappy_y < y + 140
        
        if colide_x and colide_y:
            morto = True
```


# Finalizando


- função de atualização completa: atualizar()
- controle do menu e atalhos para sair e reiniciar o jogo

```python
ativo = False

def atualizar():
    atualizar_jogo()

def atualizar():
    global ativo

    # Sai com Q ou ESC
    if pyxel.btnp(pyxel.KEY_Q):
        pyxel.quit()

    # Reinicia com R
    elif ativo and pyxel.btnp(pyxel.KEY_R):
        reiniciar()

    # Roda o jogo
    elif ativo:
        atualizar_jogo()

    # Ativa com espaço ou seta para cima
    elif pyxel.btnp(pyxel.KEY_SPACE) or pyxel.btnp(pyxel.KEY_UP):
        ativo = True
```

- Reiniciar as variáveis

```python
def reiniciar():
    global ativo, morto, flappy_x, flappy_y, velocidade, canos, score

    ativo = False
    morto = False
    flappy_x = largura_tela // 3
    flappy_y = altura_tela // 2
    velocidade = 0
    score = 0
    
    espaco = 80
    canos = [
        (0 * espaco + largura_tela, randrange(-100, 0, 10)),
        (1 * espaco + largura_tela, randrange(-100, 0, 10)),
        (2 * espaco + largura_tela, randrange(-100, 0, 10)),
        (3 * espaco + largura_tela, randrange(-100, 0, 10)),
    ]
```

- Função principal do Pyxel e rotinas de inicialização do pyxel

```python
# Inicializar o jogo
reiniciar()
pyxel.init(width=largura_tela, height=altura_tela, caption="Flappy Bird", fps=35)
pyxel.load('data.pyxres')
pyxel.run(atualizar, desenhar)
```


OBSERVAÇÕES IMPORTANTES:
- Apresenta o básico de programação: variáveis, chamar e criar funções, if, for
- Apresenta algumas estruturas de dados superficialmente (strings e listas)
- NAO utiliza o laço while
- Alguns conceitos moderadamente avançados (desconstrução de valores, compreensões de listas?)