Arquivo com o esqueleto do tutorial

# Hello World!

- Porque programar, porque jogos, motivadores, parabéns por começar, etc.

## Flappy Bird

Neste tutorial, vamos criar um joguinho estilo Flappy Bird e aprender o suficiente de programação 
para que você tenha independência para modificar o jogo e consiga criar outros joguinhos
diferentes do zero. A notícia boa é que com apenas alguns poucos conceitos, podemos
criar uma infinidade de novos jogos, programas, websites etc. Assim, aprender estes blocos básicos
da programação nos leva bem longe. É lógico que nem sempre é fácil: programação é
um desafio constante e mesmo programadores e programadoras experientes de vez em quando
encontram dificuldades inesperadas, ou pegam caminhos complicados, becos sem saída, abordagens
mal planejadas, etc. Esses obstáculos fazem parte da diversão e são como um quebra-cabeça: 
se for muito fácil e previsível, logo perdemos o interesse.

Nosso tutorial segue um caminho um pouco diferente de outros tutoriais de programação. Isso porque
**não** vamos criar nosso Flappy Bird de bloco em bloco, começando das funções básicas até finalmente
culminar em um jogo completo. A abordagem é quase inversa: começamos com um módulo auxiliar que possui
uma versão completa do jogo e vamos abrindo, desmontando, entendendo aos poucos o que está 
acontencendo em cada pedaço e gradualmente podemos substituir as peças que estavam lá por 
peças novas que nós mesmas criamos. No fim do tutorial, sobrará apenas o nosso código e este módulo
auxiliar poderá ser descartado.

No meio do caminho, podemos brincar com os parâmetros do jogo, inventar novas regras, mudar as cores
e fazer todo tipo de coisa estranha. Esperamos que, ao terminar o tutorial, todas tenham o conhecimento
necessário para começar um novo projeto do zero e a se desafiar. Será que você consegue fazer um jogo
como o Pong do zero? Quais regras do Flappy Bird você alteraria? Quais seriam os novos efeitos visuais? Você 
tem uma idéia de jogo que ninguém fez? E que tal um web site? Um aplicativo de celular? Um algoritmo de 
aprendizado de máquina? Enfim, o objetivo é abrir a caixa de Pandora, o resto é com vocês!


## Ambiente de programação

Programação é uma mistura de arte com técnica. Pense como um artista ou artesão: criatividade é muito
importante, mas a técnica é necessária para usar nossos instrumentos corretamente e obter o efeito desejado
para nossos projetos.

O instrumento básico de um programador é o editor de código. É onde escrevemos e lemos o código fonte dos 
programas e podemos interagir com os resultados rodando o programa, fazendo testes, controlando as versões, etc.
Cada linguagem de programação exige algumas ferramentas adicionais. No caso do Python, precisamos de
um interpretador de Python instalado na máquina. Este é um programa que lê programas Python e executa
as instruções codificadas. Por fim, dependendo do projeto, precisamos de instalar alguns módulos
ou programas adicionais. No nosso caso, vamos instalar o Pyxel, que é uma espécie de extensão do Python (em
linguagem de programador, "biblioteca") que permite a criação de joguinhos vintage, estilo 8-bit. (Alguém 
aqui já jogou Atari, ou isso é velho demais?) 

Vamos à lista de recursos que devemos preparar antes de começar:

- [Visual Studio Code](https://code.visualstudio.com/): O editor de código. É uma escolha pessoal, mas 
  se você não conhece nenhum editor de código, o Visual Studio Code (ou VSCode, para os íntimos), é um 
  ótimo ponto de partida: grátis, leve, simples de usar e cheio de recursos.
- [Python 3.7+](http://python.org/): O interpretador do Python. Precisamos instalar a versão 3.7 ou superior.
- [Pyxel](https://github.com/kitao/pyxel): Biblioteca para criar joguinhos 8-bit em Python.
- [Módulo auxiliar flappy.py](...): Módulo auxiliar que usaremos nesse tutorial. Possui a implementação 
  completa do jogo que vamos substituir pela nossa ao longo do tutorial.
- [Arquivo de imagens data.pyres](...): Arquivo com as imagens em pixel art utilizadas no jogo. Possui o 
  desenho de um passarinho, canos, nuvens, terreno etc. Podemos editar este arquivo pixel a pixel utilizando
  o editor de imagens que vem incluído no Pyxel. 

Se você ainda não possui estes recursos instalados, siga um dos tutoriais abaixo, a depender do
sistema operacional no seu computador:

- Eu uso o [Windows]().
- Eu uso o [Linux]().
- Eu sou chique e uso o [MacOS]().

### Testando o ambiente (?)

@TODO: talvez as instruções de testar devam ficar no final de cada sub-tutorial. 

# Tutorial, Parte 1: Iniciando o jogo 

Agora que temos tudo preparado, vamos começar com o nosso tutorial. O primeiro passo é criar uma pasta
onde vamos guardar nosso projeto e abrir o Visual Studio Code nesta pasta. Nosso projeto começa vazio e 
precisamos criar um arquivo contendo o código fonte e copiar alguns arquivos auxiliares.

O primeiro passo é ir para a pasta do projeto e copiar os arquivos [flappy.py] e 
[data.pyres] para a pasta do projeto. Ao lado destes dois arquivos, crie um arquivo vazio
chamado `jogo.py` usando a função `Arquivo > Novo Arquivo` (ou Ctrl+N) no VSCode. Vamos
abrir este arquivo e começar a trabalhar.

## Executando o jogo

Abra o arquivo `jogo.py` e copie e cole as duas linhas abaixo:

```python
import flappy

flappy.comecar()
```

A primeira linha diz para o Python importar o módulo auxiliar flappy, que irá nos ajudar ao longo
deste tutorial. Já a segunda linha, `flappy.comecar()` está falando para o Python executar a função
`comecar` definida dentro deste módulo. Em programação, uma função é uma espécie de maquininha: quando pedimos
para executá-la, o computador realiza uma série de instruções e no final pode retornar um resultado ou 
realizar um conjunto de ações. Neste caso, a função `comecar` simplesmente executa o jogo.

A primeira parte `flappy.comecar` representa o nome completo da função dentro do nosso programa. Algo como se
fosse `sobrenome.nome`, já que todas funções que começam com `flappy.<alguma coisa>` fazem parte do conjunto
de funções do módulo flappy. Já os parênteses `()` no final do nome da função dizem para o Python 
que queremos executá-la sem passar nenhum parâmetro adicional (os parâmetros adicionais, se existissem,
ficariam entre os parênteses).

Com estas duas linhas, criamos o jogo completo. Simples, né? 

Claro que não! Um programa de computador tipicamente funciona em camadas. Criamos funções que
executam operações simples, depois juntamos estas funções para criar operações um pouco mais complexas,
que juntamos em outras funções ainda mais elaboradas e assim por diante. No caso do nosso jogo, a `flappy.comecar` 
esconde uma enorme complexidade: esta função executa outras funções que, entre outras coisas, desenham o
estado do jogo na tela e atualizam a posição dos elementos. A função de desenhar pode chamar outras funções responsáveis por operações mais simples
como, por exemplo, desenhar somente o passarinho, ou desenhar os canos. Estas, por sua vez, podem chamar funções
ainda mais fundamentais que manipulam pixels específicos na tela e interagem com o sistema 
operacional, placa de vídeo e outros detalhes de baixo nível. 

Nós não vamos descer o buraco até o nível mais 
fundamental dos bits: se puxarmos o fio de qualquer programa de computador trivial, iríamos nos deparar com um
conjunto imenso de milhões de linhas de código feitas por milhares de programadoras e programadores do
mundo inteiro ao longo de décadas. É muita coisa para qualquer um acompanhar! Mas vamos descer o suficiente para
que as novas habilidades sejam úteis: que você consiga criar novos jogos, pensar em novos projetos e personalizar
o Flappy Bird para ele funcionar exatamente do jeito que você deseja! 

Podemos executar o nosso programa `jogo.py` diretamente no VSCode. Basta abrir um terminal clicando
no menu `Terminal > Novo Terminal` (ou Ctrl+Shift+') e digitar a seguinte instrução: `python jogo.py`. Você deve
ver uma janela parecida com esta:

@TODO: screenshot

Aproveita a chance e tenta quebrar o seu recorde do Flappy Bird ;-)


## Variáveis

A função `flappy.comecar` analisa seu código procurando por várias dicas de personalização. Podemos
redefinir funções para controlar elementos específicos do jogo (por exemplo, como desenhamos o passarinho).
O jeito mais simples de interagir, no entanto, é modificar algumas variáveis de configuração.

Em Python, podemos criar uma variável simplesmente usando a notação `<nome-da-variável> = <valor>`. Assim,
podemos escrever algumas variáveis entre as linhas `import flappy` e `flappy.comecar()` e, caso seja uma variável
reconhecida, ela irá alterar a execução do jogo.

Modifique o arquivo `jogo.py` para ficar mais ou menos como abaixo:

```python
import flappy

largura_tela = 150
altura_tela = 255
gravidade = 1.0
pulo = 8.0

flappy.comecar()
```

Os números mostrados são os valores padrão de cada uma destas variáveis. Modifique estes números para 
ver o que acontece. Você verá o tamanho da tela se alterar e a gravidade funcionando de modos estranhos. 
As variáveis que terminam com `.0` aceitam valores quebrados como, por exemplo, `gravidade = 0.75` e até
valores negativos.

Você também pode criar qualquer variável que quiser no programa, (ex.: `numero_preferido = 42`), mas, a 
não ser que a variável tenha um nome reconhecido pelo módulo flappy, ela ainda não terá efeito algum.

**Dica:** o lado direito de uma definição de variável pode ser uma expressão matemática como, por exemplo,
`pulo = 16 / 2`. O Python reconhece as 4 operações fundamentais e outras operações um pouco mais avançadas como
exponenciação, resto da divisão, entre outras. 


# Tutorial, Parte 2: Desenhando na tela

Ao calibrar os valores das variáveis, podemos controlar apenas alguns aspectos básicos do nosso jogo.
Agora é hora de abrir nosso brinquedo, ver o que tem dentro e mexer nas engrenagens. Vamos começar com a
primeira função importante, que é desenhar os elementos do jogo na tela: o céu, nuvens, o flappy, 
os canos, etc. 

Para fazermos isto, é necessário aprender como se define funções. Com isso, vamos trocar
a função responsável por pintar a tela pela nossa própria versão personalizada. Vimos que para chamar uma 
função, basta escrever o nome da mesma e abrir e fechar um parênteses no final (como em `flappy.comecar()`).

O módulo flappy entende que se você criar uma função chamada `desenhar`, ele irá utilizá-la ao invés de usar o
método padrão. Podemos testar essa idéia definindo a variável `desenhar = None` no nosso código. O valor
especial `None` (que "nulo/nada" em português) representa situações onde queremos anunciar que uma determinada variável
ainda não possui um valor bem definido, ou que está em um estado inválido ou inconsistente. No nosso caso, 
se falarmos que a função desenhar é nula, estamos pedindo para o módulo flappy não fazer nada quando esta função
for chamada. Coloque a linha `desenhar = None` antes de iniciar o jogo e você verá que a tela permanece preta! 
 
Talvez este último experimento não tenha sido muito útil, mas no espírito de quebrar o brinquedo e depois
colocar as peças de volta no lugar, vamos ver como a função `desenhar` é definida no módulo
flappy:

```python
def desenhar():
    desenhar_fundo()
    desenhar_nuvens()
    desenhar_canos()
    desenhar_chao()
    desenhar_flappy()
    desenhar_instrucoes()
```

Muita coisa para explicar aqui! Primeiro, observe que a função desenhar chama várias outras funções aparentemente
responsáveis por desenhar partes diferentes do nosso jogo. `desenhar_fundo`, nuvens, canos, chao, flappy, etc, 
parecem ser responsáveis por lidar com cada um destes pequenos elementos. Nosso objetivo é recriar
todas estas funções, mas vamos com calma: existem alguns detalhes importantes dessa notação que precisamos
entender primeiro.

Note como a definição da função desenhar começa com um `def <nome-da-função>`, depois colocamos os parênteses e
um sinal de dois-pontos (`:`). Esta é a estrutura básica que usaremos para definir qualquer função em Python. 
Em seguida, aparece uma série de instruções alinhadas um pouco mais à direita. Estas instruções são o que chamamos
de **corpo da função** e representam a parte principal da definição. Uma função nada mais é que um jeito de
dar nome e reaproveitar um conjunto de instruções específico. No nosso caso, estamos mostrando
para o Pyxel quais instruções devem ser executadas a cada frame para desenhar as imagens na tela enquanto o jogo
estiver rodando.

Um outro detalhe importante que devemos levar em conta é o alinhamento destas instruções. Alinhamento (ou 
"indentação", no jargão de programadores) é como o Python entende quais intruções estão associadas a uma função
ou bloco de código e quais instruções seriam executadas diretamente no módulo. Portanto, tome **muito** cuidado
para deixar o alinhamento perfeito, caso contrário o programa pode executar instruções diferentes daquelas que 
você está imaginando.


## Comentários

Comece copiando o código da função desenhar para o seu próprio código. Lembre-se que ele deve ficar **antes**
da instrução final `flappy.comecar()`, senão a nossa versão da função não terá sido definida quando o jogo 
começar e ele utilizará a implementação padrão.

Podemos conferir que a nossa função está sendo utilizada apagando algumas linhas. Por exemplo, se você apagar 
a linha `desenha_flappy()`, o jogo não mostrará o passarinho! Vai ficar estranho porque todo o resto funciona
normalmente: o jogo continua calculando colisões, contando pontos, simulando a gravidade, etc. Só não mostra o 
passarinho na tela, o que deixa muito mais difícil de jogar!

Você já deve ter visto que apagar as linhas não é muito prático se quisermos depois escrevê-las de volta. Um método
muito mais eficiente é utilizar comentários de código. Um comentário é simplesmente uma linha que é ignorada pelo
Python e é muito útil para desligar um pedaço de código ou escrever qualquer observação em Português puro, ao 
invés de Python. Trata-se, portanto, de uma parte do código lida apenas por humanos e que o computador ignora.

Em Python, os comentários são as linhas que começam com um `#`, como no exemplo

```python
def desenhar():
    desenhar_fundo()
    desenhar_nuvens()
    desenhar_canos()
    # Vamos apagar o próximo comando para ver o que acontece!
    # desenhar_chao()
    desenhar_flappy()
    desenhar_instrucoes()
```

Comentários são ótimos para explicar um trecho de código meio nebuloso ou para apontar para links ou outros
recursos que expliquem melhor o que está acontecendo.


## Desenhando o fundo

Habilite todas as instruções da função desenhar e vamos começar a abrir cada pedacinho para ver o que tem
dentro. A função mais simples de todas, e a que escolhemos para começar, é a `desenhar_fundo()`. Vamos criar
a nossa própria versão, mas antes dê uma olhada na implementação padrão:

```python
import pyxel

def desenhar_fundo():
    pyxel.cls(12)
```

O comando `import pyxel` carrega o módulo Pyxel e na verdade deve ficar logo junto ao comando `import flappy`
no seu código principal (não tem diferença aparecer antes ou depois). Isto não faz parte da função, mas é só
uma preparação!

Olhando o corpo da função, vemos que ela tem uma única instrução: chamar a função `pyxel.cls` passando o
número 12 como único parâmetro entre parênteses. Este código misterioso na verdade executa uma instrução muito 
simples: `pyxel.cls` limpa a tela aplicando uma única cor em toda área do jogo. `cls` vem de *clear screen*, 
ou *limpar a tela* em inglês. O valor 12 é simplesmente o número que identifica esta cor e, por um acaso, 
corresponde ao azul celeste que estávamos utilizando. 

A parte mais importante aqui é entender como o Pyxel representa cores. Um computador moderno é capaz de 
desenhar milhões de cores distintas que representam praticamente qualquer cor reconhecida pelo olho humano. 
O Pyxel, por sua vez, simula um computador antigo daqueles que só conseguem representar uma quantidade 
muito limitada de cores, de pixels, de sons, etc. No caso das cores, temos apenas 16 possibilidades, que 
são identificadas pelos números de 0 a 15. A correspondência entre números e cores é dada pela imagem abaixo:

![Paleta de cores](../imgs/color-palette.png)

Agora que você sabe o que está acontecendo, mude o número para trocar a cor para outro valor. Quem sabe ficar com
um céu vermelho ou roxo!

### Opcional: efeito estroboscópico

Podemos usar a correspondência entre números e cores para fazer um efeito estroboscópico no fundo do jogo. A idéia
básica é alternar a cor a cada frame avançando o número de 1 em 1. Para fazermos isto, é necessário juntar duas
idéias simples: a variável `pyxel.frame_count` conta quantos frames de jogo já foram mostrados na tela e aumenta
em 1 a cada novo frame. Se fizermos algo como,

```python
def desenhar_fundo():
    pyxel.cls(pyxel.frame_count)
```

teremos o jogo na tela por uma fração de segundo e depois aparecerá uma mensagem de erro falando que não existe
uma cor com o valor 16. Isto porque `pyxel.frame_count` irá atingir valores grandes com o tempo já que a taxa de
atualização é próxima de 30 frames a cada segundo.

Podemos consertar este problema usando alguma operação matemática que limita o número para um valor no intervalo
de 0 a 15. Uma maneira simples de fazer isto é usar o resto da divisão por 16. O resto é sempre um número entre 
0 e 15 (já que um resto 16 seria equivalente a aumentar 1 no resultado da divisão com resto zero). O resto da 
divisão de um número `n` pelo divisor `d` é representado em Python por `n % d`. A escolha do sinal de porcentagem
é um pouco curiosa neste contexto, mas é algo comum em programação. Nosso código final ficaria 

```python
def desenhar_fundo():
    pyxel.cls(pyxel.frame_count % 16)
```

Muito bom! Agora a não ser que você queira que os jogadores tenham dor de cabeça ou um ataque epiléptico, é 
melhor escolher um valor fixo para a cor do fundo ;-)

**Dica:** Se você não se lembra o que é o resto, um pequeno lembrete. Quando fazemos a divisão de dois números
inteiros, muitas vezes o resultado não é exato. O resto é justamente o quanto sobra com relação à divisão exata.
Por exemplo, 42 dividido por 16 vai dar duas vezes 16 sobrando 10. Daí dizemos que a divisão inteira de 42 por 16 
é igual à 2 com o resto 10. Em Python, `42 / 2` realiza a divisão fracionária (com o resultado 2.625), `42 // 16` retorna a
divisão inteira (no caso, 2) e `42 % 2` calcula o resto da divisão inteira (que nesse caso é 10).


## Desenhando imagens

Pintar o fundo inteiro de uma única cor é simples. Como fazemos para desenhar uma figura complexa feita de vários
pixels escolhidos a dedo por uma artista de pixel art? Vamos explorar estas questões olhando o que tem dentro da
função `desenhar_flappy`.

Começamos com um objetivo mais modesto que desenhar pixel art: vamos representar o passarinho do Flappy Birdo
simplesmente como um retângulo. Veja o código abaixo:

```python
def desenhar_flappy():
    largura = 17
    altura = 13
    cor = 10
    pyxel.rect(flappy_x, flappy_y, largura, altura, cor)
```

A parte importante aqui é a função `pyxel.rect(x, y, largura, altura, cor)`. Esta função desenha um retângulo
na tela que começa no ponto de coordenadas x e y, com determinada largura e altura (também medida em pixels) e
que possui a cor sólida especificada no último argumento (um número de 0 a 15, lembra?). Observe que numa função
que possui vários parâmetros, passamos todos valores separando-os por vírgulas. O significado de cada valor
depende da sua posição na chamada de função. Por exemplo, em `pyxel.rect` o primeiro argumento sempre diz respeito
à posição x onde o retângulo começa e o último especifica a sua cor (onde cada posição define uma propriedade 
específica).

Você também pode ter percebido que as variáveis `flappy_x` e `flappy_y` não foram definidas no código. Na verdade
podemos fazer isto porque estas variáveis foram definidas pelo módulo flappy e estamos simplesmente utilizando os 
seus valores padrão. Usar variáveis não definidas normalmente seria um erro e quando você estiver criando um 
código Python do zero é importante tomar cuidado com isto.


## Pyxeledit

@TODO
- apresentar o pyxeledit no caminho

```python
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


- def desenhar_flappy(): retângulo -> blit
- apresentar o pyxeledit no caminho



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