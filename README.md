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
tem uma idéia para criar um jogo que ninguém fez? E que tal um web site? Um aplicativo de celular? Um algoritmo de 
aprendizado de máquina? Enfim, o objetivo do tutorial é abrir a caixa de Pandora, o resto é com você!


## Ambiente de programação

Programação é uma mistura de criatividade com técnica. Pense como um artista ou artesão: criatividade é muito
importante, mas a técnica é necessária para usar os instrumentos corretamente e obter o efeito desejado.

O instrumento básico de um programador é o editor de código. É onde escrevemos e lemos o código fonte dos 
programas e podemos interagir com os resultados rodando o programa, controlando as versões, etc.
Cada linguagem de programação exige algumas ferramentas adicionais. No caso do Python, precisamos de
um interpretador de Python instalado na máquina. Este é um programa que lê programas Python e executa
as instruções codificadas. Por fim, dependendo do projeto, precisamos de instalar alguns módulos
ou programas adicionais. No nosso caso, vamos instalar o Pyxel, que é uma espécie de extensão do Python (em
linguagem de programador, uma "biblioteca") que permite a criação de joguinhos retrô, estilo 8-bit. (Alguém 
aqui já jogou Atari, ou isso é velho demais?) 

Vamos à lista de recursos que devemos preparar antes de começar:

- [Visual Studio Code](https://code.visualstudio.com/): O editor de código. É uma escolha pessoal, mas 
  se você não conhece nenhum editor de código, o Visual Studio Code (ou VSCode, para os íntimos), é um 
  ótimo ponto de partida: grátis, leve, simples de usar e cheio de recursos.
- [Python 3.7+](http://python.org/): O interpretador do Python. Precisamos instalar a versão 3.7 ou superior.
- [Pyxel](https://github.com/kitao/pyxel): Biblioteca para criar joguinhos 8-bit em Python.
- [Módulo auxiliar flappy.py](https://github.com/pyladiesdf/flappy-tutorial/blob/master/flappy.py):
  Módulo auxiliar que usaremos nesse tutorial. Possui a implementação 
  completa do jogo que vamos substituir pela nossa ao longo do tutorial.
- [Arquivo de imagens data.pyxres](https://github.com/pyladiesdf/flappy-tutorial/blob/master/data.pyxres):
  Arquivo com as imagens em pixel art utilizadas no jogo. Possui o 
  desenho de um passarinho, canos, nuvens, terreno etc. Podemos editar este arquivo pixel a pixel utilizando
  o editor de imagens que vem incluído no Pyxel. 

Se você ainda não possui estes recursos instalados, siga um dos tutoriais abaixo, a depender do
sistema operacional no seu computador:

- Eu uso o [Windows](https://github.com/pyladiesdf/flappy-tutorial/blob/master/windows-install.md).
- Eu uso o [Linux](https://github.com/kitao/pyxel#linux).
- Eu sou chique e uso o [MacOS](https://github.com/kitao/pyxel#mac).

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
deste tutorial. Já a segunda linha, `flappy.comecar()` manda o Python executar a função
`comecar` definida dentro deste módulo. Em programação, uma função é uma espécie de maquininha: quando pedimos
para executá-la, o computador realiza uma série de instruções e no final pode retornar um resultado ou 
realizar um conjunto de ações. Neste caso, a função `comecar` simplesmente executa o jogo.

A primeira parte deste comando, `flappy.comecar` representa o nome completo da função dentro do programa. Algo como
`sobrenome.nome` da função, já que todas funções que começam com o mesmo prefixo `flappy.` fazem parte do mesmo 
módulo flappy. Já os parênteses `()` no final do nome da função dizem para o Python 
que queremos executá-la sem passar nenhum parâmetro adicional (os parâmetros adicionais, se existissem,
ficariam entre os parênteses).

Com estas duas linhas, criamos o jogo completo. Simples, né? 

Claro que não! Um programa de computador tipicamente funciona em camadas. Criamos funções que
executam operações simples, depois juntamos estas funções para criar operações um pouco mais complexas,
que juntamos em outras funções ainda mais elaboradas e assim por diante. No caso do nosso jogo, a `flappy.comecar` 
esconde uma enorme complexidade: esta função executa outras funções que, entre outras coisas, desenham o
estado do jogo na tela, atualizam a posição dos elementos, verificam colisões, etc. A função de desenhar pode 
chamar outras funções responsáveis por operações mais simples
como, por exemplo, desenhar somente o passarinho, ou desenhar os canos. Estas, por sua vez, podem chamar funções
ainda mais fundamentais que manipulam pixels específicos na tela e interagem com o sistema 
operacional, placa de vídeo e outros detalhes de baixo nível. 

Nós não vamos descer o buraco até o nível mais 
fundamental dos bits: se puxarmos o fio de qualquer programa de computador trivial, iríamos nos deparar com um
conjunto imenso de milhões de linhas de código feitas por milhares de programadoras e programadores do
mundo inteiro ao longo de décadas e que lidam com detalhes altamente técnicos do funcionamento de computadores. 
É muita coisa para qualquer um acompanhar! Mas vamos descer o suficiente para
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
valores negativos. **Importante:** os valores da tela devem estar entre 0 e 256.

Você também pode criar qualquer variável que quiser no programa, (ex.: `numero_preferido = 42`), mas, a 
não ser que a variável tenha um nome reconhecido pelo módulo flappy, ela ainda não terá efeito algum.

**Dica:** o lado direito de uma definição de variável pode ser uma expressão matemática como, por exemplo,
`pulo = 16 / 2`. O Python reconhece as 4 operações fundamentais e outras operações um pouco mais avançadas como
exponenciação, resto da divisão, entre outras. 


# Tutorial, Parte 2: Desenhando na tela

Ao calibrar os valores das variáveis, podemos controlar apenas alguns aspectos básicos do nosso jogo.
Agora é hora de abrir o brinquedo, ver o que tem dentro e mexer nas engrenagens. Vamos começar com a
primeira função importante, que é desenhar os elementos do jogo na tela: o céu, nuvens, o passarinho, 
os canos, etc. 

Para fazermos isto, é necessário aprender como se define funções. Com isso, vamos trocar
a função responsável por pintar a tela pela nossa própria versão personalizada. Vimos que para chamar uma 
função, basta escrever o nome da mesma e abrir e fechar um parênteses no final (como em `flappy.comecar()`).

O módulo flappy entende que se você criar uma função chamada `desenhar`, ele irá utilizá-la ao invés de usar a versão
padrão desta função. Podemos testar essa idéia definindo a variável `desenhar = None` no nosso código. O valor
especial `None` (que "nulo/nada" em português) representa situações onde queremos anunciar que uma determinada variável
ainda não possui um valor bem definido, ou que está em um estado inválido ou inconsistente. No nosso caso, 
se falarmos que a função desenhar é nula, estamos pedindo para o módulo flappy não fazer nada quando esta função
for chamada. Coloque a linha `desenhar = None` antes de iniciar o jogo e você verá que a tela permanece preta! 
 
Talvez este último experimento não tenha sido muito útil, mas no espírito de desmontar o brinquedo e depois
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
reaproveitar e dar um nome a um conjunto de instruções. No nosso caso, estamos mostrando
para o Pyxel quais instruções devem ser executadas a cada frame para desenhar as imagens na tela enquanto o jogo
estiver rodando.

Um outro detalhe importante que devemos levar em conta é o alinhamento destas instruções no código. Alinhamento (ou 
"indentação", no jargão de programadores) é como o Python entende quais intruções estão associadas a uma função
ou bloco de código e quais instruções seriam executadas diretamente no módulo. Portanto, tome **muito** cuidado
para deixar o alinhamento perfeito, caso contrário o programa pode executar instruções diferentes daquelas que 
você está imaginando. A recomendação é que começamos com a linha `def <nome-da-função>():` e o bloco de instruções
abaixo esteja alinhado com quatro espaços a direita. Confira que o editor de código permite que a gente
digite apenas uma única vez a tecla *tab* no lugar dos quatro espaços e que ele mantêm o alinhamento (ou nível
de indentação) de uma linha para outra. Estas pequenas coisinhas tornam nossa vida muito mais fácil quando usamos
um editor especializado em código em comparação com um editor de texto genérico como o Word ou o Notepad. 


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

Habilite todas as instruções da função desenhar que, aos poucos, vamos ver o que tem dentro de cada pedacinho. 
A função mais simples de todas, e a que escolhemos para começar, é a `desenhar_fundo()`. Vamos criar
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

![Paleta de cores](imgs/color-palette.png)

Agora que você sabe o que está acontecendo, mude o número para trocar a cor para outro valor. Quem sabe ficar com
um céu vermelho ou roxo?


### Opcional: efeito estroboscópico

Podemos usar a correspondência entre números e cores para fazer um efeito estroboscópico no fundo do jogo. A idéia
básica é alternar a cor a cada frame avançando o número de 1 em 1. Para fazermos isto, é necessário juntar duas
idéias simples: a variável `pyxel.frame_count` conta quantos frames de jogo já foram mostrados na tela e aumenta
em 1 a cada novo frame. Se fizermos algo como,

```python
def desenhar_fundo():
    pyxel.cls(pyxel.frame_count)
```

veremos o jogo na tela por uma fração de segundo e depois aparecerá uma mensagem de erro falando que não existe
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


## Desenhando figuras geométricas

Pintar o fundo inteiro de uma única cor é simples. Como fazemos para desenhar uma figura complexa feita de vários
pixels escolhidos a dedo por uma artista de pixel art? Vamos explorar estas questões olhando o que tem dentro da
função `desenhar_flappy`.

Começamos com um objetivo mais modesto que desenhar pixel art: vamos representar o passarinho do Flappy Bird
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
que possui vários parâmetros, especificamos cada valor separando-os por vírgulas. O significado para a função 
depende da sua posição na lista de argumentos. Por exemplo, em `pyxel.rect` o primeiro argumento sempre diz respeito
à posição x onde o retângulo começa, o segundo define a posição y do retângulo e assim por diante.

Você também pode ter percebido que as variáveis `flappy_x` e `flappy_y` não foram definidas no código. Na verdade,
podemos omití-las porque estas variáveis foram definidas pelo módulo flappy e ao omití-las estamos simplesmente utilizando 
os seus valores padrão. Usar variáveis não definidas seria normalmente um erro e quando criar um código Python do zero 
é importante tomar cuidado com isto.


## Sistema de coordenadas e cores

Uma imagem na tela do computador ou celular é formada por uma grade de vários pontinhos coloridos. Cada um destes
pontinhos é conhecido como um pixel (do inglês **pic**ture **el**ement, ou elemento da imagem). Quando criamos
nossas próprias imagens a partir de código, é natural usar *pixels* (ou seriam *píxeis*?) para medir tamanhos
e posições. É justamente isto que vamos fazer ao longo deste tutorial.

A biblioteca Pyxel usa pixels fictícios, já que o objetivo dela é emular um computador antigo com muito menos
recursos que os computadores modernos. Enquanto um computador antigo poderia ter uma resolução típica da ordem
de 320x240 pixels, computadore modernos tipicamente possuem algo da ordem de 1920x1080. Se multiplicarmos 
os dois números, vemos que o segundo é quase 30 vezes maior que o primeiro. 

Além disto, um monitor moderno possui um controle muito preciso da cor de cada pixel. Você já deve ter ouvido 
falar do padrão RGB: este é o mecanismo típico que monitores e telas de TV usam para gerar as várias cores. No RGB, 
cada pixel é formado por um ponto de luz vermelha (**R**ed), outro verde (**G**reen) e outro azul (**B**lue). Se 
você tiver acesso a uma lupa potente ou microscópio, é possível ver os três pontos de cor distintos muito 
claramente. O monitor então controla a intensidade de cada uma destas três cores em cada ponto da tela para gerar
qualquer cor distinguível pelo olho humano.

Um computador moderno típico usa 256 intensidades para cada cor RGB de cada pixel, o que resulta em aproximadamente 16.8
milhões de cores distintas! O Pyxel, por sua vez, nos limita a somente 16 cores, o que equivale ao número de cores 
nos primeiros monitores coloridos dos primeiros computadores pessoais da IBM.

Agora que sabemos que as distâncias são medidas em pixels e as cores são representadas por números de 0 a 15, 
vamos ver como se identifica um ponto específico na tela. A idéia básica é que podemos encontrar um ponto contando
quantos pixels é necessário andar na direção horizontal e quantos na direção vertical para conseguir identificá-lo.

Em notação matemática usual, contaríamos quantos pixels a partir do canto esquerdo da tela para representar a 
coordenada horizontal (coordenada **x**) e quantos pixels a partir da margem inferior para 
representar a coordenada vertical (coordenada **y**). Programadores gostam de complicar as coisas e contam a
partir do canto superior esquerdo. Isto significa que a coordenada y é invertida com relação à direção usual: `y = 0`,
representa o canto superior da tela e, na medida que y cresce, caminhamos para baixo na tela do computador.

O fato que a coordenada vertical y cresce para baixo significa que, muitas vezes, temos que fazer algumas
conversões. Para encontrar um ponto que esteja 10 pixels a esquerda da tela e 20 acima, teríamos que usar as 
coordenadas `x = 10` e `y = altura_tela - 20`. 


## Pyxeleditor

Pyxel nos ajuda a criar joguinhos retrô baseados em *pixel art*. Por enquanto, vimos como desenhar coisas simples:
como pintar a tela de uma única cor e desenhar retângulos. Poderíamos criar nossas artes em código, programando 
as cores de cada pixel manualmente, e isto era mais ou menos a abordagem usada para criar os primeiros jogos 
eletrônicos. Considerando que mesmo a tela de computadores antigos tinha dezenas de milhares de pixels, podemos
ver facilmente que isto seria **muito** trabalhoso.

Vamos usar uma abordagem alternativa e executar o Pyxeleditor, que é uma espécie de Photoshop retrô que vem junto
com o Pyxel para editar *pixel art*. O arquivo de imagens padrão para o tutorial, [data.pyxres](data.pyxres), já vem 
com o desenho do Flappy Bird, canos, chão e nuvens. Você pode modificá-los depois, mas não queremos exigir um 
grande talento artístico e domínio completo sobre os pixels para terminar este tutorial e portanto já deixamos
a arte pronta.

Pyxeledit é aberto a partir da linha de comando. Abra novamente o terminal (no menu `Terminal > Novo Terminal`)
e digite `pyxeleditor data.pyxres`. Deve abrir uma tela como esta

![Pyxeledit](imgs/pyxeleditor.png)

Aqui temos um editor simples que permite modificar as imagens disponíveis no jogo pixel a pixel. Você pode brincar
um pouco aqui, mudar a cor do passarinho, desenhar algum adereço, etc, mas podemos simplesmente utilizar as imagens
como estão.

Observe que no canto inferior direito da tela temos um contator escrito "Image - 0 +". Isto permite escolher qual
imagem vamos editar. O Pyxel aceita apenas 3 imagens distintas, ainda que em cada imagem podemos fazer diversos
desenhos diferentes. Cada imagem possui um máximo de 256 por 256 pixels e pode ser editada em blocos menores de
16 por 16. Veja que ao passar o cursor em um ponto da imagem, o editor mostra as coordenadas do pixel no
canto superior direito. Isto é muito útil quando precisamos selecionar quais partes da imagem serão mostradas em
cada parte do jogo.

Veja que a primeira imagem (Image 0) possui 3 variantes do passarinho. Preste bastante atenção: cada variante possui
uma posição ligeiramente diferente para a asa. Assim, se alternarmos entre as variantes, podemos obter a ilusão de
movimento.
 
Finalmente, para desenhar uma destas imagens na tela precisamos de recolher algumas informações:

* **Posição x e y da imagem na tela do jogo.** Esta posição corresponde à posição que o pixel
  superior esquerdo da imagem terá na tela de jogo. 
* **O número da imagem (0, 1, ou 2).** Escolhemos quais das 3 imagens do Pyxeledit será utilizada.
* **Posição u e v da imagem no Pyxeleditor.** Corresponde ao ponto onde o pedaço da imagem que estamos copiando 
  começa no Pyxeleditor. Se a imagem estiver no canto superior esquerdo, este valor seria (0, 0). Caso 
  contrário, precisamos verificar as coordenadas no Pyxeleditor e utilizá-las no código Python para
  carregar estas imagens
* **Largura e altura.** Determina quantos pixels serão utilizados na direção horizontal e vertical
  a partir do pixel de início no Pyxeleditor.
* **Cor de máscara.** Podemos, opcionalmente, marcar uma das cores como sendo transparente. Deste modo,
  ao invés de desenhar os pixels desta cor, o Pyxel irá simplesmente manter o que já estava desenhado
  no fundo da tela.

Agora voltando para o código Python, podemos usar estas informações e passar para a função `pyxel.blt` para
desenhar uma imagem que se encontra no Pyxeleditor dentro do seu jogo. A função `blt` utiliza os parâmetros
mencionados acima (nesta mesma ordem) e seu uso é ilustrado abaixo

```python
def desenhar_flappy():
    # Número da imagem
    img = 0
    
    # Posição inicial no Pyxeleditor
    u = 0
    v = 0
    
    # Tamanho da imagem
    largura = 17
    altura = 13
    
    # Cor tratada como transparente
    mascara = 0

    # Chamamos a função blt para desenhar tudo isso!
    pyxel.blt(flappy_x, flappy_y, img, u, v, largura, altura, mascara)
```

Note que trocamos `x` e `y` por `flappy_x` e `flappy_y` já que estas são as variáveis que guardam as posições x
e y do passarinho. Para trocarmos a imagem, temos que alterar o valor de u e v na chamada de função.
Podemos, por exemplo, escolher a segunda imagem do passarinho com a asa para cima, usando `v = 16`, já
que é onde esta imagem começa na coordenada y. Altere um pouco estes valores para entender como cada um
funciona!


## Animando o Flappy Bird

Agora que sabemos como mostrar uma imagem na tela, vamos dar um passo além e criar uma animação! Vimos que na
imagem 0 do Pyxeleditor temos 3 versões do passarinho que diferem entre si pela posição das asas. Se alternarmos
entre estas três figuras, podemos criar uma ilusão de animação em que vai parecer que o passarinho está batendo
asas. 

A idéia é ficar apenas alguns poucos frames em cada uma das imagens e depois trocar por outra. Felizmente, 
as imagens são muito parecidas e estão próximas entre si, diferindo apenas pela posição inicial em y. Temos
a primeira imagem começando em `y = 0`, depois a seguinte em `y = 16` e a última em `y = 24`. Cada um destes casos
pode ser escrito simplesmente como `y = 0 * 16`, `y = 1 * 16` ou `y = 2 * 16`, de forma que apenas o número
que multiplica o 16 precisa mudar de uma imagem para a outra. 

Vamos supor que este número fica salvo na variável `frame`, para apontar o número do frame. Podemos modificar
o nosso código anterior para mudarmos facilmente o frame que será mostrado na tela:

```python
def desenhar_flappy():
    # Fixamos o frame 
    frame = 0
 
    # Posição inicial no Pyxeleditor agora depende do frame escolhido
    u = 0
    v = frame * 16

    # O resto continua como antes...
    img = 0
    largura = 17
    altura = 13
    mascara = 0
    pyxel.blt(flappy_x, flappy_y, img, u, v, largura, altura, mascara)
```

Note que isto não resolve o problema da animação. Simplesmente alternamos a imagem do Flappy Bird entre
a que ele fica com a asa levantada (`frame = 1`) e as que ele fica com a asa abaixada (`frame = 0 ou 2`).
Para animarmos, é necessário avançar esta variável a cada frame ou a cada grupo de alguns poucos frames. 
Podemos fazer isto facilmente igualando `frame` ao `pyxel.frame_count`, mas tomando o resto da divisão por
3 para obter um número entre 0 e 2.

Troque a linha `frame = 0` por:

```python
frame = pyxel.frame_count % 3
```

Isto funciona, mas o passarinho bate asas **muito** rápido! Um modo fácil de consertar isto é dividir
`pyxel.frame_count` por um valor qualquer antes de calcular o resto para dimuinir a taxa de alternância
entre as imagens. Algo como isto:

```python
frame = (pyxel.frame_count / 4) % 3
```

Este código deveria alterar a imagem a cada 4 frames, mas ao invés disto produz um bug muito estranho
(rode para ver!). O problema aqui é que frame deve ser sempre uma variável inteira e `pyxel.frame_count / 4`
pode resultar em valores fracionários. Consertamos isto trocando a divisão usual expressa como `a / b` pela
divisão inteira `a // b`, que garante que a resposta final é sempre um número inteiro. Juntando tudo isso,
ficamos com o código:


```python
def desenhar_flappy():
    # Escolhemos qual dos 3 frames 0, 1 ou 2 utilizar
    frame = (pyxel.frame_count // 4) % 3

    # Número da imagem
    img = 0
    
    # Posição inicial no Pyxeleditor
    u = 0
    v = frame * 16
    
    # Tamanho da imagem
    largura = 17
    altura = 13
    
    # Cor tratada como transparente
    mascara = 0

    # Chamamos a função blt para desenhar tudo isso!
    pyxel.blt(flappy_x, flappy_y, img, u, v, largura, altura, mascara)
```
 
Maravilha! Agora nosso passarinho aparece em toda glória do pixel art com direito a animação e tudo. E o 
mais importante de tudo isso: o código para fazer isto aparecer é todo seu!


## Desenhando o chão

O chão é basicamente um retângulo. Podemos implementar nossa função de `desenhar_chao` de forma
simplificada simplesmente desenhando um retângulo de uma cor com cara de terra:

```python
def desenhar_chao():
    altura = 16
    cor = 11
    pyxel.rect(0, altura_tela - altura, largura_tela, altura, cor)
```

Apesar de funcional, esta versão do chão é bem desinteressante. O chão não possui texturas, não
produz a ilusão de movimento e a qualidade artística deixa muito a desejar. Felizmente, existe uma
imagem de chão pronta no arquivo de imagens que podemos usar para contornar estes problemas.

O chão está definido na seção de "tilemaps" do Pyxel editor. Um tilemap é simplesmente uma imagem 
formada pela repetição de outras imagens menores. No caso, temos uma pequena imagem de 16x16 pixels
que desenha um chão de grama texturizado. Vamos repetir esta imagem várias vezes para preencher a
tela com uma bela imagem de chão.

Os tilemaps são maneiras de fazer imagens maiores dentro das limitações do Pyxel. Cada coordenada
em um tilemap corresponde a um ladrilho de 8x8 pixels. Assim, um tilemap com altura de 2 equivaleria a 
16 pixels usados na tela. Vamos carregar a imagem do chão a partir do primeiro tilemap 
na nossa biblioteca de imagens.

A função `pyxel.bltm(x, y, tm, i, j, largura, altura)` desenha uma imagem de largura e altura dadas
(estas medidas são em ladrilhos 8x8, não em pixels), na posição (x, y) da tela usando os ladrilhos
que começam nas posições i e j no tilemap. A variável `tm` é um índice de 0 a 2 que representa um
dos 3 tilemaps disponíveis no Pyxel. Juntando tudo isso, temos a versão inicial da nossa função de
desenhar o chão

```python
def desenhar_chao():
    # Posição na tela
    x = 0
    y = altura_tela - 16
    
    # Posição do ladrilho no tilemap
    i = 0
    j = 0
    
    # Número de ladrilhos usados na largura e altura da imagem
    largura = 32
    altura = 2
    
    # Mostra o tilemap
    pyxel.bltm(x, y, 0, i, j, largura, altura)
```

Um problema com esta função é que o chão permanece estático na posição `x = 0`. Podemos corrigir isto
fazendo `x` diminuir a medida que `pyxel.frame_count` aumenta. Um jeito bom de fazê-lo é usar 

```python
x = -pyxel.frame_count % largura_tela
```

Isto faz com que x fique sempre limitada num intervalo válido que está sendo mostrado na tela. Se você substituir
a definição de x em `desenhar_chao` pela linha acima, verá que isto também não resolve totalmente o nosso 
problema: o chão agora acompanha o movimento dos canos, mas não preenche totalmente a posição do fundo na tela.
O truque para resolver isto é criar 2 retângulos com `pyxel.bltm` separados pela largura da tela de distância.
Desta forma, quando um dos retângulos desaparecer, ou outro ainda estará visível preenchendo o resto da tela.   

A função, no final, fica assim:
 
```python
def desenhar_chao():
    # Posição na tela
    x1 = -pyxel.frame_count % largura_tela
    x2 = -pyxel.frame_count % largura_tela - largura_tela
    y = altura_tela - 16
    
    # Posição do ladrilho no tilemap
    i = 0
    j = 0
    
    # Número de ladrilhos usados na largura e altura da imagem
    largura = 32
    altura = 2
    
    # Mostra os dois blocos do tilemap
    pyxel.bltm(x1, y, 0, i, j, largura, altura)
    pyxel.bltm(x2, y, 0, i, j, largura, altura)
```

Parabéns! Agora sabemos utilizar tilemaps. Um uso mais comum para tilemaps é criar fases de um jogo de plataforma
como Mário ou Sonic. Neste caso, podemos definir as imagens básicas como chão, itens, entre outros e usar o
tilemap para desenhar a fase, fazendo a disposição dos blocos que formam o chão, dos blocos que possuem itens, etc.


## Escrevendo instruções na tela

A última parte do nosso código de desenhar o jogo na tela consiste em mostrar mensagens de texto na tela de jogo.
A função que faz isto no Pyxel chama-se `pyxel.text` e recebe com argumentos as coordenadas x e y da posição 
do texto, a mensagem de texto propriamente dita e a cor do mesmo.

A função `desenhar_instrucoes` determina que mensagem será mostrada para o jogador. Inicialmente, devemos
mostrar algum tipo de instrução orientando a apertar espaço ou seta para cima para começar. Enquanto o
jogo estiver ativo, esta mensagem deve ser substituída pelo placar e, finalmente, quando o jogador perder,
devemos mostrar uma mensagem pedindo para pressionar "R" para reiniciar.

Tudo isso é um bocado complicado, então vamos começar mostrando uma mensagem fixa na tela.

```python
def desenhar_instrucoes():
    msg = "OLA! BEM VINDA AO FLAPPY BIRD!"
    x = 0
    y = altura_tela / 3
    cor = 7
    pyxel.text(x, y, msg, cor)
```

Observe que o texto fica alinhado à esquerda e não acompanha o estado do jogo. A primeira coisa que
vamos fazer é alinhá-lo ao centro. Isto melhora a legibilidade, principalmente quando as mensagens 
de texto variam muito de tamanho.

Controlamos o alinhamento modificando o valor da coordenada x. A fórmula correta para fazer isto é
igualar x à metade da largura da tela menos metade da largura do texto. A questão é: como calculamos
a largura do texto?

O primeiro passo é contar o número de caracteres na mensagem. Poderíamos fazer isto manualmente, mas o
computador é muito melhor em contar coisas que seres humanos. Em Python, obtemos o tamanho de uma
sequência usando a função `len`. Como um texto pode ser entendido como uma sequência de caracteres, 
obtemos o seu tamanho a partir de `len(msg)`.

Agora que sabemos o número de caracteres, é necessário multiplicar por quantos pixels cada caractere utiliza e
dividir este resultado por dois. O Pyxel possui uma variável `pyxel.FONT_WIDTH` que especifica (em pixels)
a largura de cada caractere. O resultado de tudo isto, é que a variável x deve seguir a seguinte fórmula
para centralizar o texto guardado na variável `msg`:

```python
largura_texto = pyxel.FONT_WIDTH * len(msg)
x = largura_tela / 2 - largura_texto / 2
```

Juntando tudo isso, ficamos com a seguinte função:

```python
def desenhar_instrucoes():
    cor = 7
    msg = "OLA! BEM VINDA AO FLAPPY BIRD!"
    largura_texto = pyxel.FONT_WIDTH * len(msg)
    x = largura_tela / 2 - largura_texto / 2
    y = altura_tela / 3
    pyxel.text(x, y, msg, cor)
```

Troque por uma mensagem que signifique algo mais importante para você e vamos para a próxima etapa!


## Se, então, senão

Agora que sabemos como desenhar textos na tela do jogo, vamos escolher um conjunto de mensagens 
mais apropriado para a situação do jogador. Temos que lidar com basicamente 3 situações diferentes:

1. **Jogador morreu.** Mensagem diz para apertar R para reiniciar.
2. **Jogo está rodando.** Mostramos o placar.
3. **Jogo ainda não começou.** Mensagem diz para pular para começar.

Este tipo de estrutura lógica é chamado em programação de execução condicional. Temos uma lógica do
tipo *"se acontecer A, faça B, mas se acontecer C, faça D"*. Em Python, descrevemos esta estrutura
usando o comando if/elif/else. Este é um dos conceitos mais importantes de programação e por isso 
vamos voltar no comando **if** com mais detalhes posteriormente neste tutorial.

A estrutura básica de um bloco condicional é dada por

```python
if condicao A:
    comando A
elif condicao B:
    comando B
else:
    comando C
```

Neste bloco, o computador primeiro testa a condição A, que pode ser qualquer expressão que resulte
em um valor de verdadeiro ou falso, e caso esta condição seja verdadeira, ele executa somente o 
comando A. Apenas no caso em que a primeira condição for falsa, ele segue com o teste e avalia a condição
B. Caso ela seja verdadeira, ele executa o comando B e se for falsa, executa o comando C. 

Lembre-se que em um bloco de if/elif/else, somente um dos blocos de comando será executado. O Python sempre
escolhe o bloco associado à primeira condição verdadeira, mas caso nenhuma condição seja satisfeita, ele
executa o bloco **else**.

Vamos usar esta estrutura para definir o texto da mensagem que vai aparecer na tela de acordo com
o estado do jogo. A nossa lista de situações pode ser traduzida para as variáveis de programação
de forma mais ou menos simples:

1. **Jogador morreu.** A variável `morto` possui um valor verdadeiro.
2. **Jogo está rodando.** A variável `ativo` possui um valor verdadeiro.
3. **Jogo ainda não começou.** Corresponde à condição else no nosso condicional.

As variáveis `morto` e `ativo` começam com um valor `False` (falso, em inglês) e depois podem mudar
de valor dependendo de como o usuário interagir com o jogo. Se, por exemplo, o jogador bater em um
cano, o estado de `morto` muda de `False` para `True`. Nós não vamos nos preocupar agora em
controlar estas variáveis, mas apenas em mostrar a mensagem correta de acordo com o valor
que elas assumirem ao longo do jogo.

O código final da nossa função `desenhar_instrucoes` após utilizar o comando **if** fica:

```python
def desenhar_instrucoes():
    cor = 7

    if morto:
        msg = "Aperte R para reiniciar"
    elif ativo:
        msg = str(score)
    else:
        msg = "Espaço ou seta para cima para começar"
    
    largura_texto = pyxel.FONT_WIDTH * len(msg)
    x = largura_tela / 2 - largura_texto / 2
    y = altura_tela / 3
    pyxel.text(x, y, msg, cor)
```

A primeira e a última condições são simples de entender: estamos simplesmente atribuindo um 
valor de texto para a variável `msg`. Já a condição do meio possui o comando `str(score)`, que
merece uma explicação. A variável `score` guarda o placar atual do jogo. Começa sempre no valor
zero e aumenta em 1 a cada cano que o passarinho atravessar. 

Score é uma variável numérica e não podemos simplesmente atribuí-la à mensagem porque `pyxel.text`
espera um texto e não um número no terceiro argumento onde passamos a mensagem. Precisamos, portanto,
converter o número para texto e é justamente isto que a função `str` faz: `str(x)` retorna uma 
representação de x como texto, qualquer que seja o valor de x.

O nome `str` para converter valores para texto pode parecer um pouco misterioso. Porque não algo como
`text(x)`?  O nome `str` é uma abreviação de `string`, que em inglês significa cadeia/corrente. É um
jargão comum em computação chamarmos um texto de uma "cadeia" de caracteres. Pode parecer um pouco 
estranho pensar deste jeito, já que raramente pensamos em um texto como uma sequência aleatória de
caracteres. Lembre-se que o computador não entende nada do que escrevemos. Assim, se você fosse um 
computador, o texto completo deste tutorial, as obras completas de Machado de Assis, a música do Michel
Teló cantanda em russo ou o texto de um gato que subiu no teclado teriam exatamente o mesmo 
significado: um bando de letras na memória. 

As variáveis de texto normalmente são criadas colocando o conteúdo do texto entre aspas. No entanto,
se você quiser converter qualquer tipo de variável `x` para texto, basta executar a função `str(x)`
que o Python retornará uma representação razoável para o valor de `x`.


## Desenhando os canos

O Flappy Bird mostra uma lista aparentemente infinita de canos andando para esquerda junto com o cenário. Esta
lista infinita, na verdade, é uma mentira! Na realidade, são apenas 4 canos que andam para esquerda e são
reciclados na medida que saem pelo lado esquerdo da tela. Cada cano também é representado apenas por 2 valores:
a coordenada x com a posição horizontal e a coordenada y que determina a altura dos canos para verificar 
as colisões.

A lista de canos está salva na variável também chamada `canos`. Esta é uma variável do tipo lista, que contêm
varios valores diferentes dentro dela. Existem várias operações que podemos fazer em listas, mas vamos aprender
apenas algumas das mais básicas. 

A primeira delas é a de ler um elemento da lista: listas são indexadas a partir do zero. Assim, o primeiro
elemento é representado por `canos[0]`, o segundo por `canos[1]` e assim por diante. Note que usamos os
colchetes para especificar a posição na lista. Para extrair as coordenadas x e y de um dos canos basta fazer:

```python
x, y = canos[0]
```

Aqui podemos trocar o índice de 0 para qualquer valor até 3 para escolher o cano adequado. Podemos
desenhar um cano inicialmente como um retângulo. Vamos nos preocupar só com o primeiro deles, por enquanto.
Um cano é bem representado por um retângulo:

```python
abertura_cano = 200

def desenhar_canos():
    cor = 11
    largura = 25
    altura = 135
    x, y = canos[0]
    
    # Cano superior
    pyxel.rect(x, y, largura, altura, cor)
    
    # Cano inferior
    pyxel.rect(x, y + abertura_cano, largura, altura, cor)
```

Note que o código acima mostra apenas o primeiro cano da lista. Poderíamos copiar e colar as últimas linhas
alterando o índice de `canos[0]` para os valores 1, 2 e 3, mas isto não ficaria muito elegante. Se tem
uma coisa que o computador faz bem, é realizar tarefas repetitivas sem se cansar ou se confundir. 

Vamos ver um comando que permite fazer justamente isto. O comando **for** repete uma série de instruções alterando o valor
de uma variável em cada uma das repetições. A sintaxe do `for` é

```python
for elemento in lista:
    comandos que dependem de elemento
```

Este comando percorre uma lista de valores (no nosso caso queremos percorrer a lista de posições dos canos) e
executa uma ou mais instruções que dependem da variável associada a cada elemento da lista. Como cada elemento
na lista de canos é um par de variáveis, podemos separá-las diretamente no comando for:

```python
# Percorre a posição x, y de cada cano
for x, y in canos: 
    # Desenha o cano na posição x, y
    pyxel.rect(x, y, largura, altura, cor)
    pyxel.rect(x, y + abertura_cano, largura, altura, cor)
```

Juntando todos esses pedacinhos, podemos escrever a função responsável por desenhar os canos. Você consegue
fazer isto sozinha? Se esbarrar em alguma bug, não tem problema. Mostramos abaixo como pode ser o resultado
final. É lógico que esta não é a única (e nem necessariamente a melhor) maneira de se fazer.

```python
def desenhar_canos():
    cor = 11
    largura = 25
    altura = 135
    for x, y in canos:
        pyxel.rect(x, y, largura, altura, cor)
        pyxel.rect(x, y + abertura_cano, largura, altura, cor)
```

## Opcional: canos em pixel art

Um problema da implementação anterior é que os canos estão desenhados somente como retângulos sem graça. O
banco de imagens do tutorial possui uma versão desenhada com sombras e texturas em pixel art. A lógica é
muito parecida com o caso anterior, mas agora usamos a função `pyxel.blt` ao invés da função `pyxel.rect`.

Para usar `pyxel.blt`, precisamos indentificar a posição da imagem no banco de imagens e o tamanho em pixels
na altura e largura. Estes valores estão explicados no código abaixo:

```python
def desenhar_canos():
    img = 1       # índice da imagem (0 a 3)
    u = 0         # posição x no banco de imagens
    v = 0         # posição y no banco de imagens
    largura = 25  # largura em pixels
    altura = 150  # altura em pixels
    cor = 0       # cor considerada transparente ao desenhar a imagem (opcional)
    for x, y in canos:
        pyxel.blt(x, y, img, u, v, largura, altura, cor)
        pyxel.blt(x, y + abertura_cano, img, u, v, largura, -altura, cor)
``` 

Uma observação importante aqui: an segunda chamada a `pyxel.blt` usamos uma altura negativa. Isto simplesmente
diz para o Pyxel espelhar a imagem verticalmente. Se especificarmos uma largura negativa, ele espelharia no 
sentido horizontal. 

Este código pode ser reescrito de forma mais enxuta. Não é necessário definir `id = 1`, `u = 0`, `v = 0`, etc e usar 
o nome da variável na chamada de função. Podemos substituir os valores diretamente na posição dos argumentos e 
economizar várias linhas de código com isto. A chamada de função ficaria parecida com `pyxel.blt(x, y, 1, 0, 0, 25, 150, 0)`.
Usando este truque, com quantas linhas você consegue criar esta função?


## Nuvens com paralaxe (opcional)

Esta parte é um pouco mais avançada e não acrescenta nenhuma funcionalidade importante no jogo. Vamos apenas desenhar as
nuvens no fundo do cenário. Cada nuvem se desloca uma fração de pixel para a esquerda por frame. Esta proporção pixel é
importante para dar um efeito de profundidade. Se as nuvens se deslocassem na mesma velocidade do cenário (1 pixel por frame),
elas dariam a impressão de estarem fixas ao cenário e, portanto, em um mesmo plano na tela. Se as nuvens se deslocarem mais
lentamente, teremos a impressão que elas estariam em um plano mais distante que os canos na tela e, por isto, teriam uma 
velocidade aparente menor.

Podemos controlar o deslocamento em x usando a variável `pyxel.frame_count`. Devemos obter um valor negativo e, em valor
absoluto, menor que a quantidade de frames para que o deslocamento das nuvens no fundo fique mais lento que os 
canos em primeiro plano. Basta usar uma regra parecida com esta:

```python
x = -pyxel.frame_count / 2
```

Queremos também que as nuvens se desloquem para a esquerda, mas que reapareçam do lado direito da tela quando tiverem
cruzado a tela completamente. Assim, queremos fazer o deslocamento em múltiplos de `largura_maxima = largura_tela + largura_nuvem`:
cada vez que uma nuvem percorrer este intervalo, ela deve cruzar de volta para o lado direito da tela. 

Podemos garantir que a imagem dá esta volta depois de percorrer a `largura_maxima` é realizar a operação de resto da divisão,
ou seja, `x % largura_maxima`. Este valor ainda não é ideal porque a nuvem irá desaparecer e reaparecer no fim da tela assim
que a coordenada x ficar negativa. Isto é ruim, porque se tivermos algo como `x = -1`, a maior parte da imagem ainda estará 
na tela e este "teletransporte" ficará visível para o jogador. Vamos usar portanto `x % largura_maxima - largura_nuvem` 
como base de cálculo. Como cada nuvem deve aparecer em um local diferente da tela, acrescentamos um deslocamento em x
diferente para cada uma das nuvens. 

O código final ficaria parecido com este. Tente modificar alguns parâmetros para entender o que está acontencendo e
procure o desenho das nuvens no Pyxeledit, quem sabe fazendo algumas alterações.

```python
def desenhar_nuvens():
    # Deslocamento base em x
    x = -pyxel.frame_count / 2

    # Largura da nuvem e tamanho do intervalo a ser percorrido em cada ciclo
    largura_nuvem = 32
    altura_nuvem = 32
    largura_maxima = largura_tela + largura_nuvem 
    
    # Posições de cada nuvem
    x1 = (x + largura_tela * 0.25) % largura_maxima - largura_nuvem
    y1 = altura_tela / 2
    x2 = (x + largura_tela * 0.50) % largura_maxima - largura_nuvem
    y2 = altura_tela / 4
    x3 = (x + largura_tela * 0.75) % largura_maxima - largura_nuvem
    y3 = altura_tela / 1.5
    
    # Desenha as três nuvens        
    pyxel.blt(x1, y1, 2, 0, 16, largura_nuvem, altura_nuvem, 12)
    pyxel.blt(x2, y2, 2, 0, 48, largura_nuvem, altura_nuvem, 12)
    pyxel.blt(x3, y3, 2, 0, 80, largura_nuvem, altura_nuvem, 12)
```


# Lógica do jogo

Lembra da nossa função `desenhar` que chamava várias outras funções para desenhar partes específicas do jogo?
Vamos fazer algo parecido com a função `atualizar_jogo`, que atualiza partes específicas do nosso jogo e modifica
o valor de algumas variáveis dependendo de como o usuário interage com o jogo.

A implementação padrão desta função segue abaixo.

```python
def atualizar_jogo():
    atualizar_flappy()
    atualizar_canos()
    atualizar_colisoes()
    atualizar_score()
```

Nesse ponto você já deve entender como isto funciona. Esta função é executada no início de cada frame e realiza 
algumas tarefas em sequência: atualiza a posição e velocidade do passarinho, em seguida move os canos para a 
posição correta, testa se houve alguma colisão do passarinho com um cano ou com o chão e, finalmente, atualiza o
a pontuação do jogo se o jogador conseguir passar por mais um cano.

Você perceberá que estas funções tendem a ser um pouco mais complicadas que as funções de desenho. Isto não é 
necessariamente inesperado já que elas precisam fazer mais coisas e controlar a lógica do jogo. Elas também são
responsáveis por controlar as variáveis que controlam o estado do jogo como, por exemplo, a posição do passarinho,
sua velocidade, o número de pontos, etc. Todas estas tarefas exigem pequenos passos adicionais que vamos 
apresentar aos poucos nas próximas seções.


## Simulando gravidade

Vamos implementar as funções dentro de `atualizar_jogo` na ordem em que aparecem. A primeira delas, e talvez a
mais interessante, é a função de `atualizar_flappy`, que controla a posição do passarinho na tela. Esta função
controla basicamente 4 variáveis, que devemos declarar explicitamente agora antes de utilizá-las:

```python
flappy_x = largura_tela / 3
flappy_y = altura_tela / 2
velocidade = 0
morto = False
```

As variáveis `flappy_x` e `flappy_y` controlam as coordenadas (x, y) do passarinho na tela. `velocidade` se
refere à velocidade vertical onde valores positivos significa que o passarinho está caindo. Finalmente, a variável
`morto` pode assumir apenas os valores `True` (verdadeiro) ou `False` (falso) e diz se o passarinho está morto
ou não.

Lembre-se que quando fazemos `flappy_x = largura_tela / 3` é necessário que a variável `largura_tela` esteja 
previamente definida no código. Nossa sugestão é que você arrume o código para que as primeiras linhas sejam
todas de `import ...`, depois coloque as definições de variáveis, em seguida a definição de funções e, finalmente,
o código `flappy.comecar()` na última linha do seu programa.

Vamos começar simulando a gravidade no nosso jogo. A idéia básica é que a cada frame vamos aumentar a velocidade
por um incremento proporcional à gravidade e em seguida aumentar a posição em x de acordo com o valor da 
velocidade. Seria algo como fazer as transformações:

```python
velocidade = velocidade + gravidade
flappy_y = flappy_y + velocidade
```

Neste código, temos que ler o sinal de `=` não como representando uma igualdade, mas sim como 
*"velocidade **recebe** velocidade mais gravidade"*. Isto significa que, ao executar esta linha o Python
calcularia o valor do lado direito (somando velocidade com a gravidade) e depois atualizaria a variável 
do lado esquerdo com o novo valor. O fato do mesmo nome aparecer dos dois lados da equação é um pouco
confuso, mas pense que cada lado opera em instantes diferentes de tempo: primeiro o computador avalia
o lado direito e somente *depois* de completar o lado direito que ele salva os valores nas variáveis do 
lado esquerdo.

Infelizmente, se simplesmente colocarmos este código dentro da função `atualizar_flappy` como abaixo,
o código não vai funcionar (o jogo trava logo no começo):

```python
def atualizar_flappy():
    velocidade = velocidade + gravidade
    flappy_y = flappy_y + velocidade
```

O problema aqui é bastante sutil e tem a ver com o que os programadores chamam de escopo de variáveis. Sempre que
criamos uma variável dentro de uma função o Python entende que esta variável só fica definida durante a execução
da função. Isto acontece mesmo quando existe outra variável com o mesmo nome definida anteriormente fora da 
função.

O primeiro tipo de variáveis (criadas dentro de uma função) são chamadas de **variáveis locais**. Recebem este nome
porque elas ficam disponíveis de forma localizada à função. Uma função **não** pode modificar as variáveis locais 
de outra e se duas funções usarem o mesmo nome para variáveis diferentes não acontece nada problemático na 
execução do programa. 

Por outro lado, as variáveis definidas fora de funções são as que chamamos de 
**variáveis globais**. Elas estão disponíveis globalmente para todas as funções, que compartilham os
mesmos valores de suas variáveis globais. Para evitar que as funções alterem sem querer o valor de variáveis
globais, o Python exige que a gente declare explicitamente uma variável como global quando vamos modificá-la 
de dentro de uma função. Isto é só uma proteção para evitar que um código modifique uma variável que
todos acessam de forma não-intencional. 

Dito isto, vamos modificar a nossa função de atualização para declarar flappy_x, flappy_y e velocidade
como globais (ou seja, se nós modificarmos estas variáveis dentro de uma função, ela será modificada 
globalmente).

```python
def atualizar_flappy():
    global velocidade, flappy_x, flappy_y

    velocidade = velocidade + gravidade
    flappy_y = flappy_y + velocidade
```

A instrução `global <nomes-de-variáveis>` especifica quais variáveis devem ser tratadas
como globais no corpo da função. Lembre-se que se a variável não for alterada dentro da função (ou seja, se 
estivermos utilizando-a somente para leitura, não é necessário fazer a declaração global.

**Observação para nerds:** quem lembra das aulas de física pode pensar que as fórmulas estão erradas. Isto porque tomamos alguns
atalhos. Em física, a velocidade incrementa com a aceleração *multiplicada pelo intervalo de tempo* (e de forma análoga
para a posição), o que faz com que a fórmula correta seja `velocidade = velocidade + gravidade * dt`  e `flappy_y = flappy_y + velocidade * dt`.
Significa que estamos assumindo que o intervalo de tempo `dt = 1`. Isto não é correto se estivermos medindo tempo em
segundos, mas funciona se estivermos medindo em frames. Neste caso, dt é realmente igual a um, a posição é medida em 
pixels, a velocidade em pixels por frame e aceleração por pixels por frames ao quadrado!   


## Pulos e interação com o teclado

Estamos progredindo, mas o jogo agora tornou-se impossível: começamos uma partida e o passarinho simplesmente
cai sem nenhuma chance do jogador fazer qualquer progresso. Temos que verificar se o jogador realizou um
comando de pulo e, neste caso, alterar a velocidade do nosso Flappy Bird. 

Para fazer isto, é necessário articular duas verificações: primeiro, descobrir se uma determinada tecla foi 
pressionada ou não (no nosso caso o espaço ou a seta para cima). Depois, modificar a velocidade *somente se* 
esta tecla estiver pressionada no frame atual. 

A primeira parte é feita pela função `pyxel.btnp(<tecla>)`. Podemos selecionar a tecla usando uma de várias
variáveis presentes no módulo Pyxel. Todas variáveis que representam teclas possuem nomes da forma 
`pyxel.KEY_<nome-da-tecla>`. Por exemplo, `pyxel.KEY_A`, `pyxel.KEY_B`, etc representam letras. Já `pyxel.KEY_UP`,
`pyxel.KEY_DOWN`, `pyxel.KEY_LEFT` e `pyxel.KEY_RIGHT` representam as setas do teclado. Os nomes estão em inglês,
mas geralmente são o que se espera para cada uma das teclas.

Podemos, assim, criar uma variável `pulando` que guarda um valor de verdadeiro ou falso dependendo se alguma tecla
de pulo for apertada ou não:

```python
pulando = pyxel.btnp(pyxel.KEY_SPACE)
```

O código acima testa somente a tecla de espaço. Podemos verificar mais de uma tecla criando uma expressão lógica.
Temos um pulo se o jogador *apertar o espaço **OU SE** apertar a seta para cima*. Em inglês **ou** se escreve como 
**or** e a expressão lógica ficaria traduzida para Python como

```python
pulando = pyxel.btnp(pyxel.KEY_SPACE) or pyxel.btnp(pyxel.KEY_UP)
```

Agora temos a variável `pulando` que diz se o passarinho deve pular ou simplesmente cair de acordo com a lei da
gravidade. Caso esteja pulando, devemos mudar a direção do movimento para cima, alterando o valor da velocidade.
Este tipo de regra *se condição A for satisfeita, então faça ação B* é conhecido como uma execução condicional
em programação. Colocamos isto no nosso código criando blocos condicionais com o comando **if**. Algo como o código
abaixo.

```python
if pulando:
    velocidade = velocidade_de_pulo  # escolhemos a velocidade do pulo
```

A estrutura geral do comando **if** é `if <condição>: <bloco-de-instruções>`, onde o bloco de instruções pode conter
várias linhas de comandos. A condição pode ser qualquer valor, variável ou expressão que represente um valor 
verdadeiro ou falso. No nosso caso, vamos simplesmente utilizar o valor da variável `pulando`, que sabemos que 
deve ser `True` ou `False`, dependendo se o usuário tiver ou não pressionado as teclas de pulo.

Lembra que o sistema de coordenadas do Pyxel considera que a coordenada y cresce na medida que andamos para baixo na tela?
Assim, uma velocidade positiva significa que o objeto está caindo e uma velocidade negativa representa um objeto subindo.
A variável pulo, que representa a velocidade de cada pulo do Flappy Bird é um valor positivo, então devemos inverter seu
sinal ao modificar a velocidade, efetivamente trocando `velocidade_de_pulo` por `-pulo`.

Finalmente, temos que limitar a posição y do passarinho para que ele não ultrapasse o chão. A soma da altura da arte
do chão com a do passarinho dá 29 pixels, o que significa que ele deve estar pelo menos a 29 pixels de distância da 
parte inferior da tela. Em outras palavras, a posição máxima em y deve ser `altura_tela - 29`. Podemos limitar isto
utilizando um condicional. Algo como *se posição maior que altura máxima, então posição recebe altura máxima*.

Juntando tudo isso, ficamos com o seguinte código para atualizar o passarinho: 

```python
def atualizar_flappy():
    global velocidade, flappy_x, flappy_y

    pulando = pyxel.btnp(pyxel.KEY_SPACE) or pyxel.btnp(pyxel.KEY_UP)
    
    # Atualiza a velocidade
    velocidade += gravidade

    # Verifica se está pulando antes de atualizar a posição
    if pulando:
        velocidade = -pulo
        
    # Atualiza a posição
    flappy_y += velocidade
    
    # Limita altura
    if flappy_y > altura_tela - 29:
        flappy_y = altura_tela - 29
```

Muito bom! Agora nosso personagem cai e também consegue pular! Evite somente copiar e colar este código. Você consegue escrever
a mesma lógica de um jeito diferente? Usando menos linhas ou trocando a ordem de alguns comandos? Existe alguma troca que altera
o funcionamento do código? Faça experimentos para entender bem o que está acontecendo. Se o experimento der errado, ctrl+z é 
sempre seu amigo :)


## Vivo ou morto?

No Flappy Bird, o passarinho começa vivo e consegue voar enquanto não tiver tocado em nenhum cano ou no chão. O módulo
auxiliar flappy define uma variável chamada `morto` que controla se o passarinho está morto ou não. É lógico que ele
só deve ser capaz de pular se `morto = False`. 

Por enquanto não precisamos preocupar em determinar quando trocar `morto` de `False` para `True`, porque a implementação
padrão já faz isto para gente. Vamos apenas assumir que recebemos sempre o valor correto e vamos atualizar o passarinho de
acordo com isto. Existem duas mudanças que podemos fazer no nosso código: primeiramente, a de previnir pulos quando o
passarinho estiver no estado morto. Depois, fazê-lo andar junto com o cenário quando estiver caído no chão para que os
canos não continuem passando por ele.

A primeira parte é a mais fácil: basta trocar a condição `if pulando: ...` para `if pulando and not morto: ...`. No Python,
podemos fazer expressões lógicas de maneira muito parecida com o que elas seriam em inglês. A segunda condição lê-se como
***se** estiver pulando **e** **não** estiver morto, então atualize a velocidade*. 

A parte de deslocar o passarinho junto com o cenário vai exigir um condicional extra. Neste caso, vamos controlar o valor
da posição x e afastar 1 pixel por frame para esquerda caso o passarinho estiver morto. Esta velocidade de 1 pixel por
frame não foi escolhida à toa: é mesma velocidade com que o cenário se desloca no jogo. Algo como:

```python
if morto:
    flappy_x = flappy_x - 1
```

Tente fazer estas alterações por conta própria e veja o que funciona. Se travar, dê uma olhadinha na implementação 
abaixo ou use ela apenas para conferir se as suas alterações estão boas. Em programação, não existe uma única 
resposta correta. Se seu código estiver diferente, mas funcionando bem, então parabéns! Significa que você está 
encontrando seu próprio caminho e próprio estilo na programação :)

```python
def atualizar_flappy():
    global velocidade, flappy_x, flappy_y

    pulando = pyxel.btnp(pyxel.KEY_SPACE) or pyxel.btnp(pyxel.KEY_UP)
    
    # Atualiza a velocidade
    velocidade += gravidade

    # Verifica se está pulando antes de atualizar a posição
    if pulando:
        velocidade = -pulo
        
    # Atualiza a posição
    flappy_y += velocidade
    
    # Limita altura
    if flappy_y > altura_tela - 29:
        flappy_y = altura_tela - 29

    # Desloca-se com o cenário, caso esteja morto
    if morto:
        flappy_x -= 1
```

Ufa! Esta parte foi difícil, mas valeu a pena! Agora entendemos como o passarinho se move e obedece 
à Lei da Gravidade. 


## Canos

Vamos passar para a próxima parte do nosso tutorial que é a de animar o cenário, em particular os canos.
Vamos alterar a posição de cada cano 1 pixel para a esquerda para dar a impressão que o passarinho está
andando para a direita. 

A função responsável por mover os canos é a `atualizar_canos`. Aqui vamos relembrar um pouco a lógica da 
função responsável por desenhá-los, a `desenhar_canos`. A parte mais importante era o laço **for** que 
percorria as coordenadas x e y de cada cano desenhando a imagem de acordo com estes valores.

```python
for x, y in canos:
    pyxel.blt(x, y, img, u, v, largura, altura, cor)
    pyxel.blt(x, y + abertura_cano, img, u, v, largura, -altura, cor)
```

Vamos usar uma lógica semelhante, mas agora temos que não só ler, mas também reescrever a
posição de cada cano. É necessário, portanto, saber não só as coordenada x e y, mas também qual
é a posição do cano na lista de canos. Existem vários métodos de fazer isto, vamos simplesmente
criar uma nova variável `i` que guarda a posição atual na lista. Esta variável começa em zero
e aumenta em 1 a cada vez que os comandos do for são executados.

Usamos a posição i na lista para atualizar o valor do cano, deslocando um pixel para esquerda.

```python
i =  0
for x, y in canos:
    cano[i] = x - 1, y
    i = i + 1
```

Preste atenção na linha `cano[i] = (x - 1, y)`. Tem muita coisa acontencendo aqui! Lembra-se que 
`lista[i]` obtem o par na posição `i` da lista? De forma semelhante `lista[i] = valor` salva o 
valor do lado direito na posição `i` da lista. No nosso caso, o valor do lado direito do sinal de igual é um par
de variáveis: subtraímos 1 de x e mantemos y igual para representar o deslocamento de 1 pixel para
a esquerda. 

Agora que sabemos mais ou menos como atualizar a posição dos canos, precisamos cobrir outra parte importante
do código que é a inicialização da variável `canos`. Já vimos que cada cano é representado por um par de
valores representando as coordenadas x e y do cano. 

Quando o jogo começa, o primeiro cano fica oculto fora da tela (mas pronto para entrar, assim que o jogador
apertar para pular). Não conseguimos ver, mas o cano também tem um tamanho vertical bem maior que a tela e, 
normalmente teria um pedaço sobrando tanto em cima quanto em baixo. 

O primeiro cano, portanto, poderia ser algo como

```python
cano1 = largura_tela, -50
```

Aqui igualamos a coordenada x à largura da tela para especificar um cano que está oculto imediatamente ao
lado direito da tela e irá aparecer imediatamente quando o cenário começar a andar. Atribuímos um valor
arbitrário -50 à coordenada y para lembrar que existem 50 pixels sobrando para cima da tela. 

Seguindo essa lógica, poderíamos agora criar 4 variáveis, uma para cada cano, com os valores das posições 
em x e y

```python
cano1 = largura_tela, -50
cano2 = largura_tela + 80, -20
cano3 = largura_tela + 160, -70
cano4 = largura_tela + 240, -90
```

Neste caso, os canos estão a uma distância horizontal de 80 pixels entre si e com valores aparentemente 
aleatórios na coordenada y. Podemos melhorar este código de duas maneiras: a primeira é fazer a distância
entre os canos controlável a partir de uma variável e a segunda é transformar estes valores 
pseudo-aleatórios em valores aleatórios de verdade.

O primeiro passo é trocar o número 80 pela variável `distancia_canos` (com um valor inicial de 80). Veja que
a coordenada x de cada cano possui um padrão do tipo `largura_tela + distancia_canos * i`, onde i é a posição
do cano 0, 1, 2 ou 3.

```python
distancia_canos = 80
cano1 = largura_tela + distancia_canos * 0, -50
cano2 = largura_tela + distancia_canos * 1, -20
cano3 = largura_tela + distancia_canos * 2, -70
cano4 = largura_tela + distancia_canos * 3, -90
```

O próximo passo é fazer a coordenada y realmente aleatória. Para isto, temos que importar a função `randint`
do módulo `random` do Python. Esta função recebe 2 parâmetros: o menor valor e o maior e sorteia um número
inteiro entre (e incluindo) estes valores. Sorteamos um número entre 1 e 10 e multiplicamos por 10 para ficar
num intervalo entre 10 e 100. Como a coordenada y deve ser negativa (o cano começa acima do topo da tela),
colocamos um sinal negativo antes.


```python
from random import randint

distancia_canos = 80
cano1 = largura_tela + distancia_canos * 0, -10 * randint(1, 10)
cano2 = largura_tela + distancia_canos * 1, -10 * randint(1, 10)
cano3 = largura_tela + distancia_canos * 2, -10 * randint(1, 10)
cano4 = largura_tela + distancia_canos * 3, -10 * randint(1, 10)
```

Agora que temos os 4 canos, basta criar uma lista com os valores e salvar como `canos` para
criar a lista de canos. Em Python, uma lista é criada colocando diversos valores separados
por vírgulas entre colchetes.

```python
canos = [cano1, cano2, cano3, cano4]
```

Já sabemos criar a lista de canos, então vamos voltar na função responsável por atualizar suas posições

```python
def atualizar_canos():
    i = 0
    for x, y in canos:
        canos[i] = x - 1, y
        i = i + 1
```

Existe um problema sério com esta função: uma vez que os canos saem pelo lado esquerdo da tela, eles nunca mais 
serão vistos! Temos que reposicionar os canos que se deslocaram muito à esquerda novamente de volta para fora da
tela no seu lado direito. 

Podemos fazer isto checando, antes de atualizar a posição x, se o cano já passou completamente para
o lado esquerdo da tela. Isto é feito verificando se a posição x é menor que o negativo da largura do 
cano. Consultado o código anterior, vemos que o cano tem 25 pixels de largura e, portanto se estiver a
-25 pixels em x ou ainda mais a esquerda, ele estará totalmente encoberto na tela.

Isto dá uma boa idéia de uma checagem que pode ser feita antes de salvarmos o valor na variável `canos[i]`
  
```python
def atualizar_canos():
    i = 0
    for x, y in canos:
        if x < -25:
            ... # Atualiza as coordenadas x e y
        canos[i] = x - 1, y
        i = i + 1
```

O código para atualizar as coordenadas x e y do novo cano deve seguir a lógica: deslocamos o cano por
4 distâncias para a direita e sorteamos um novo valor aleatório para y:

```python
if x < -25:
    x = x + distancia_cano * 4
    y = -10 * randint(1, 10)
```

Se você se perdeu um pouco no seu código, segue o código completo desta parte.

```python
# Coloque junto com os outros imports
from random import randint


# Definição de variáveis
distancia_canos = 80
cano1 = largura_tela + distancia_canos * 0, -10 * randint(1, 10)
cano2 = largura_tela + distancia_canos * 1, -10 * randint(1, 10)
cano3 = largura_tela + distancia_canos * 2, -10 * randint(1, 10)
cano4 = largura_tela + distancia_canos * 3, -10 * randint(1, 10)
canos = [cano1, cano2, cano3, cano4]


def atualizar_canos():
    i = 0
    for x, y in canos:
        if x < -30:
            x = x + 4 * distancia_canos * 4
            y = -10 * randint(1, 10)
        canos[i] = x - 1, y
        i = i + 1
```

Lembre-se de colocar cada pedaço em seu local correto no arquivo jogo.py: os imports ficam sempre no final, em seguida
vem as definições de variáveis, depois as declarações de funções e, por último, a chamada de função `flappy.comecar()`

## Colisões

@TODO
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

    for x, y in canos:
        colide_x = x + 12.5 > flappy_x > x - 12.5
        colide_y = flappy_y > y + abertura_cano or flappy_y < y + 140
        
        if colide_x and colide_y:
            morto = True
```


## Score

Vamos finalmente implementar a última função da lógica do jogo, `atualizar_score`. Aqui nossa tarefa é relativamente
simples: temos que contar quantos canos já passaram pelo Flappy Bird. Para isto, basta ver a posição x de cada cano
e verificar se ela coincide com a posição do passarinho. Se elas coincidirem, sabemos que o passarinho acabou de 
passar por um cano e, se ele não estiver morto, isto significa que o score deve aumentar por um.

Lembre-se de declarar o valor inicial `score = 0` junto com as outras variáveis do jogo e em seguida crie
a função `atualizar_score`. A parte mais difícil aqui é percorrer a lista de canos. Vimos que cada cano
é representado apenas por um par (x, y) com a posição x do cano e a altura da sua abertura. Podemos
percorrer esta lista de valores usando o comando `for (x, y) in canos: ...`, onde o Python vai automaticamente
atribuir o primeiro valor do par à variável x e o segundo à variável y. 

Novamente, tente fazer as modificações por conta própria, mas se travar em algum ponto, mostramos uma
implementação possível da função `atualizar_score`.

```python
score = 0

def atualizar_score():
    global score

    # Percorre as coordenadas x e y de cada cano
    for (x, y) in canos:

        # Verifica se a posição do cano coincide com a do passarinho e se ele
        # não está morto
        if flappy_x == x and not morto:
            score = score + 1
```

Terminamos aqui a parte de atualizar a lógica do jogo e já podemos passar para a última parte do
tutorial.


# Finalizando

Agora estamos quase lá! Já fizemos todas as funções de desenhar e atualizar a lógica do jogo. Agora vamos
passar para a parte final que é a de configurar e inicializar o jogo usando as funções do Pyxel. Quando 
terminarmos, poderemos descartar completamente o módulo auxiliar retirando as linhas `import flappy` e 
`flappy.comecar()`. Basicamente o que falta é criar a nossa própria versão da função `flappy.comecar`.


## Reiniciando o jogo

Criamos, até agora, várias variáveis e funções para controlar cada aspecto do jogo. É uma boa idéia (se é que você já não 
está fazendo isto), organizar o código de forma que as linhas que declaram variáveis globais aparecam no início, logo abaixo
dos imports, e as funções venham em seguida, onde completamos o código colocando `flappy.comecar()` na última linha.

Vamos agora colocar todas as declarações de variáveis num mesmo lugar e mover todas estas declarações para dentro de
uma função. O objetivo aqui é que a gente consiga reiniciar facilmente o jogo para o estado inicial já que toda lógica
de inicialização fica concentrada em uma função que pode ser chamada várias vezes.

Começamos recolhendo as variáveis mais importantes. Deve ser uma lista parecida com esta:

```python
# Estado de jogo
ativo = False
morto = False
score = 0

# Passarinho
flappy_x = largura_tela // 3
flappy_y = altura_tela // 2
velocidade = 0

# Cria canos
distancia_canos = 80
cano1 = 0 * distancia_canos + largura_tela, randrange(-100, 0, 10)
cano2 = 1 * distancia_canos + largura_tela, randrange(-100, 0, 10)
cano3 = 2 * distancia_canos + largura_tela, randrange(-100, 0, 10)
cano4 = 3 * distancia_canos + largura_tela, randrange(-100, 0, 10)
canos = [cano1, cano2, cano3, cano4]
``` 

Vamos agora mover todas estas variáveis para uma função chamada `reiniciar` para que seja fácil
restaurar estes valores sempre que quisermos reiniciar o jogo. Para isto, basta alinhar todas estas
linhas um pouco mais a direita e colocar estas variáveis no corpo da função `reiniciar`. Lembre-se
que devemos fazer a declaração global de todas variáveis que serão utilizadas em outras partes do
código.

Tente fazer por conta própria, mas se não estiver funcionando, veja abaixo como fizemos:

```python
def reiniciar():
    global ativo, morto, flappy_x, flappy_y, velocidade, score, canos, distancia_canos

    # Estado de jogo
    ativo = False
    morto = False
    score = 0
    
    # Passarinho
    flappy_x = largura_tela // 3
    flappy_y = altura_tela // 2
    velocidade = 0
    
    # Cria canos
    distancia_canos = 80
    cano1 = 0 * distancia_canos + largura_tela, randrange(-100, 0, 10)
    cano2 = 1 * distancia_canos + largura_tela, randrange(-100, 0, 10)
    cano3 = 2 * distancia_canos + largura_tela, randrange(-100, 0, 10)
    cano4 = 3 * distancia_canos + largura_tela, randrange(-100, 0, 10)
    canos = [cano1, cano2, cano3, cano4]
```

Agora que temos a função reiniciar definida, basta executá-la sempre que quisermos
restaurar as variáveis de jogo para os valores padrão.


## Atualizando o loop de jogo

Programas com interface gráfica como jogos, editores de texto, navegadores, etc, tipicamente possuem um 
loop principal da aplicação. Esta é uma espécie de laço for infinito que funciona mais ou menos da 
seguinte maneira:

```python
# Visão esquemática do loop principal de um programa
for i in range(infinito):
    verifica_interações_com_usuário()
    atualiza_estado_do_programa()
    atualiza_as_saídas_para_o_usuário()
    espera_alguns_milissegundos_para_o_próximo_frame()
```

A parte de atualizar o programa no Pyxel consiste em basicamente realizar duas operações: atualizar o 
estado do jogo e desenhar o resultado na tela. Como todo o resto é bastante previsível e não muda muito
de um jogo para o outro, o Pyxel pede apenas que nós forneçamos duas funções que realizam cada uma
destas operações para que ele as execute no loop principal.

Nós já temos funções que fazem isto e foram implementadas nas etapas anteriores do tutorial: a função 
`atualizar_jogo` e a `desenhar`. A função `desenhar`, do jeito que está, encontra-se perfeita. Já a
primeira função implementa a lógica de atualização apenas enquanto o jogo está ativo, mas ela
não gerencia os estados intermediários quando o jogador ainda não iniciou o jogo ou quando ele
deseja reiniciá-lo.

Vamos então implementar a função `atualizar` que chama `atualizar_jogo` quando o jogo estiver
ativo, mas gerencia as outras interações adicionais como reiniciar e sair do jogo. Vamos começar
acrescentando estas duas funcionalidades:

```python
def atualizar():
    # Sai com Q ou ESC
    if pyxel.btnp(pyxel.KEY_Q):
        pyxel.quit()

    # Reinicia com R
    elif pyxel.btnp(pyxel.KEY_R):
        reiniciar()

    # Caso contrário, chama a versão padrão de atualizar_jogo()
    else:
        atualizar_jogo()
```

Note como a estrutura da nossa execução condicional é diferente aqui. Temos o comando **if <condição>**,
seguido do **elif <condição>** e finalmente um **else**. O significado disto é simples: sempre que tivermos
um bloco de if/elifs/else, o Python executará apenas a primeira condição que for verdadeira e, caso nenhuma
seja, ele executará o bloco **else**. 

A diferença entre **if** e **elif** é um pouco confusa. Eles funcionam de forma semelhante, mas cada bloco
condicional começa sempre com um único **if** e todas as outras alternativas devem ser escritas como **elif**'s. 
Elif é a contração em inglês de **else if**, que em português se traduziria como *ou então se*. 

Para ficar mais claro, escrevemos a lógica da função acima em português

```
se pressionou Q ou ESC:
    sai do jogo.
ou então se pressionou R:
    reinicia variáveis.
caso contrário:
    atualiza o jogo.
``` 

Só tem um pequeno problema com esta nova implementação: quando executamos o jogo, ele começa imediatamente, sem
dar um fôlego para o jogador se concentrar, ler as instruções e preparar a sua mão no teclado. Temos que criar
uma nova variável de estado que diz se o jogo está ativo ou não. Só executamos `atualizar_jogo` agora se o 
jogo estiver ativo. Caso contrário, esperamos o jogador pressionar uma tecla de pulo para sinalizar que já 
podemos começar.

```python
ativo = False

def atualizar():
    global ativo

    # Sai com Q ou ESC
    if pyxel.btnp(pyxel.KEY_Q):
        pyxel.quit()

    # Reinicia com R
    elif pyxel.btnp(pyxel.KEY_R):
        reiniciar()

    # Roda o jogo
    elif ativo:
        atualizar_jogo()

    # Ativa com espaço ou seta para cima
    elif pyxel.btnp(pyxel.KEY_SPACE) or pyxel.btnp(pyxel.KEY_UP):
        ativo = True

    # O bloco else é opcional. Não precisamos dele aqui!
```

Agora nossa função de atualizar cuida de todos os pequenos detalhes da inicialização. Estamos quase
no ponto de implementar o jogo inteiro do zero e entender como um jogo baseado no Pyxel funciona. Espero
que você já esteja elocubrando com as próprias idéias de jogos e projetos para o futuro :) 


## Pyxel run!

Vamos substituir a última parte do código auxiliar e apagar de vez o módulo `flappy.py` do HD! O primeiro
passo é criar coragem e apagar as linhas que dependem dele: `import flappy` logo no início 
e `flappy.comecar()` logo no final. Faça isso e execute o jogo para confirmar que ele para de funcionar.
Na verdade, se você executar o jogo depois destas alterações, não acontecerá nada porque o Pyxel não será
inicializado.

Começamos trocando a última linha `flappy.comecar()` por uma sequência de comandos. O primeiro deles é
o de inicializar as variáveis de jogo, que podemos fazer executando `reiniciar()`. Em seguida, precisamos
configurar a Pyxel com as configurações adequadas para o nosso jogo. Existem duas funções importantes
nesta etapa: `pyxel.init` e `pyxel.load`.

A função `pyxel.init(largura, altura, nome)` configura a tela de jogo para a largura e altura especificadas
em pixels. O nome da janela aparece como um título na barra superior da janela. Podemos especificá-lo 
colocando qualquer texto entre aspas. Finalmente, podemos modificar a taxa de atualização do jogo controlando
o parâmetro opcional `fps=valor`. Neste último caso, não basta apenas colocar um número como argumento 
adicional para a função init, mas é necessário especificar explicitamente o nome deste argumento. A sintaxe
para isto é 

```python
pyxel.init(largura_tela, altura_tela, "Flappy Bird", fps=35)
```

Já a função `pyxel.load(arquivo)` carrega um arquivo de imagens a partir do seu nome. Nós estamos utilizando 
o arquivo `data.pyres` que foi fornecido pelo tutorial. Não podemos simplesmente escrever o nome do arquivo como
argumento da função porque esta função espera um valor do tipo texto. Para representar um texto, temos que 
escrever o nome do arquivo entre aspas:

```python
pyxel.load("data.pyxres")
```

Finalmente, a última linha do seu código deve ser a função `pyxel.run(atualizar, desenhar)` que realmente
inicia o jogo. Esta função recebe dois parâmetros, que são funções. A primeira delas deve ser uma função
que atualiza o estado do jogo a cada frame, a nossa função `atualizar` definida anteriormente. A segunda
função é responsável por desenhar o estado do jogo na tela e corresponde à nossa função `desenhar`. 

O Pyxel utiliza estas duas funções para implementar o loop de jogo. A cada frame ele executa `atualizar()`
e depois antes de desenhar o resultado na tela, `desenhar()`. Entre estas execuções, o Pyxel faz uma série
de tarefas comuns a vários jogos, mas trabalhosas de implementar caso a caso. Por exemplo, ele verifica
as entradas do usuário, tenta manter uma taxa de atualização constante, verifica se a janela foi 
redimensionada, etc. 

Juntando tudo, as últimas linhas do seu código que substituem a linha `flappy.comecar()` devem ficar mais ou menos
como abaixo.

```python
# Inicializar o jogo
reiniciar()
pyxel.init(largura_tela, altura_tela, "Flappy Bird", fps=35)
pyxel.load("data.pyxres")
pyxel.run(atualizar, desenhar)
```

Execute o jogo, agora 100% feito por você!
