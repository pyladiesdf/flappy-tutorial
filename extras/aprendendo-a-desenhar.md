## Desenhando na tela

A principal função de um motor de jogos é desenhar imagens na tela, tocar sons e interagir com os comandos do usuário. Vamos começar pela primeira parte, ou seja, vamos desenhar algumas figuras básicas na tela do jogo e criar algumas animações básicas. Para isso, vamos usar algumnas das idéias aprendidos na seção anterior adaptando para o nosso objetivo que é criar um jogo.

### Instalando Pyxel

@TODO


### Importando o Pyxel

Nosso primeiro passo é importar a biblioteca Pyxel no prompt interativo do Python. Digite `python` no terminal para abrir o interpretador Python. Cada comando que você digitar agora será interpretado como uma instrução Python e o interpretador irá executá-lo seguindo as regras da linguagem. Para importar o Pyxel digite:

>>> import pyxel

Isso não produzirá nenhum efeito aparente, já que ele apenas carregou a biblioteca, mas não inicializou a janela de jogo ou mostrou qualquer imagem. Para iniciar o jogo, vamos usar a função init com a resolução de tela: isto criará uma tela de jogo que *simula* a resolução especificada. Se você reparar, a resolução que fornecemos abaixo é muito pequena. Isto porque o Pyxel simula jogos retrô com resoluções baixíssimas e limita a resolução máxima da tela para um valor que hoje em dia seria considerado muito baixo.

>>> pyxel.init(200, 150)  # inicializa uma tela de 200 por 150 pixels

O comando acima cria uma janela completamente preta. Dependendo do seu computador, ele pode acreditar que a janela está travada, já que ela está nos esperando digitar comandos para passar para o sistema operacional. Se o computador falar que a janela está travada, tenha paciência e peça para esperar (mas não feche a janela, para não estragar o resto da atividade).

#### Desenhando figuras

A janela padrão foi criada com todos os pixels escuros. Vamos desenhar algo um pouco mais interessante usando as funções do Pyxel. Antes, no entanto, é necessário entender como o computador desenha objetos na tela. Como você deve imaginar, tudo no computador pode ser rastreados a números (muitas vezes escritos como zeros e uns). A tela do computador não é muito diferente. Ainda que os computadores modernos introduzam várias complicações, a idéia básica é simples: a placa de vídeo expõe uma certa quantidade de memória e se manipularmos diretamente esta região de memória podemos reescrever cada pixel individualmente.

Considere, por exemplo, que a sua resolução de tela seja de 1920x1080. Isto corresponde a um pouco mais de 2 milhões de pixels individuais que precisamos controlar. Num computador moderno, cada pixel pode ser representado por 3 números de 0 até 255: são as componentes vermelho (red), verde (green) e azul (blue) que definem cada cor possível. Se analizarmos cada combinação possível destas componentes, temos quase 17 millhões de cores distintas por pixel. É muita informação!

Pyxel simula um computador antigo e limita bastante o número de pixels que temos que lidar. Primeiramente, a resolução máxima possível é de 256x256, o que nos limita a "apenas" cerca de 65 mil pixels. O número de cores também é extremamente reduzido: ao invés de utilizar 17 milhões de combinações, o Pyxel nos limita a 16, onde cada cor é identificada por um único número. Isso facilita muito o nosso trabalho pois não precisamos pensar muito em otimizações e em escolher a linguagem mais rápida possível para fazer nossos joguinhos. 

O segundo conceito importante de entender sobre o método que o Pyxel desenha elementos na tela é a técnica de "double buffering". O nome é complicado, mas a idéia é relativamente simples. Ao invés de manipularmos diretamente a área de memória responsável por desenhar os pixels na tela, trabalhamos em uma região de memória separada e deixamos a biblioteca escolher a melhor hora de mandar essa informação para a placa gráfica. 

Tavez seja mais simples de entender com um exemplo. O comando ``pyxel.cls(cor)`` limpa o fundo da tela e desenha a cor selecionada. Vamos usar a cor número 12, que se olharmos na paleta de cores, corresponde a um azul celeste.

>>> pyxel.cls(12)

Note que este comando não modifica a tela do jogo, que continua preta. Ele pinta de azul esta área de memória separada, e podemos acrescentar outros comandos antes de enviar a imagem final.

>>> pyxel.circ(100, 75, 20, 10)

A imagem só aparecerá na tela depois que executarmos a função "flip" (virar) do pyxel. A metáfora que eles usaram para escolher o nome dessa função é como se pintássemos gradualmente o lado de trás da tela e, quando chegar a hora de mostrar um frame pro usuário, apenas viramos a tela com o desenho completo.  

>>> pyxel.flip()

Isto atualizará a tela com o desenho de um belo dia de sol :)
A esta altura, você já deve ter advinhado que a função ``pyxel.circ(...)`` é responsável por desenhar círculos na tela. Modifique os 4 argumentos para entender a função de cada um deles. Lembre que um círculo é definido pela posição do centro, o raio e sua cor. Cada parâmetro deve, portanto, corresponder a cada uma destas propriedades.

@TODO: exercício, outras figuras geométricas


#### Arquivo de script

Você deve estar se questionando que para mostrar qualquer imagem minimamente interessante, temos que rodar vários comandos e depois executar a função `pyxel.flip()` para atualizar a tela de jogo. É muito pouco prático fazer isto no terminal interativo porque temos que digitar (ou copiar e colar) os comandos manualmente. Lembre-se que num jogo real, o computador realiza este processo várias vezes por segundo (lembra de frames por segundo?), o que torna a interação manual completamente impraticável. 

Vamos melhorar um pouco esta situação colocando todos os comandos em um script. Um script Python é simplesmente um arquivo de texto com a extensão `.py` que contem uma lista de comandos Python. Basta escrever o que você digitaria no terminal interativo, linha por linha. Você pode editar seus scripts no Notepad, Word, ou qualquer editor de texto comum. No entanto, editores especializados em código são muito mais eficientes e fáceis de usar. Nós recomendamos usar o [Visual Studio Code](https://code.visualstudio.com/), um editor simples e de código aberto desenvolvido pela Microsoft. O Visual Studio Code possui versões para Windows, Linux, MacOS e até algumas versões adaptadas para rodar diretamente no navegador (@CITAR).

@TODO instalando VSCode

Agora que instalamos e abrimos o VSCode, vamos escrever nosso primeiro arquivo de código Python. Começamos importando o Pyxel, depois pedimos para desenhar algumas figuras na tela e aplicamos a função `pyxel.flip()`. O conteúdo do seu arquivo vai ser algo como abaixo:

```python
import pyxel

pyxel.init(200, 150)
pyxel.cls(12)
pyxel.circ(50, 25, 15, 10)
pyxel.flip()
```

Executamos esse código chamando o comando `python <nome-do-arquivo.py>`, onde `<nome-do-arquivo.py>` corresponde ao arquivo que você salvou o código acima. 

@TODO explicar o terminal do VSCode, apontar atalhos e atalho para executar script pelo VSCode.  

Uma coisa que você vai notar imediatamente do código acima é que o programa mostra rapidamente uma janela com a imagem desejada e depois termina. Pode parecer que tem uma coisa errada, mas não! A função `pyxel.flip()` dura apenas um frame de execução e não mantêm a tela aberta. Depois que nosso script executa todas as instruções na tela, ele encerra a execução. Deste modo, o computador está fazendo exatamente o que mandamos ele fazer: inicializa o Pyxel, desenha o fundo azul e um sol amarelo, mostra a cena na tela e depois encerra. Podemos previnir o encerramento da tela chamando `pyxel.show()`, no lugar do `pyxel.flip()`. As duas mostram a imagem atual na tela, mas a função `pyxel.show()` mantêm a tela visível até que o usuário clique no botão de fechar a janela. 

```python
import pyxel

pyxel.init(200, 150)
pyxel.cls(12)
pyxel.circ(50, 25, 15, 10)
pyxel.show()
```

Se você ainda está confusa sobre a diferença entre `show()` e `flip()`, não se preocupe que vamos voltar neste assunto em breve. Antes, vamos melhorar um pouco a nossa cena colocando alguns elementos geométricos novos e imagens em pixel art. 

O Pyxel possui várias funções para desenhar figuras geométricas como círculos, retângulos, linhas e triângulos. Além disto, podemos criar um arquivo com figuras, sons e músicas para carregar no jogo.  


```python
import pyxel

pyxel.init(200, 150)

# Céu: pinta a tela de azul
pyxel.cls(12)

# Sol: desenha um círculo de raio 15px em (50px, 25px)
pyxel.circ(50, 25, 15, 10)

# Chão: retângulo na parte de baixo do sistema de coordenadas
pyxel.rect(0, 170, 150, 30, 4)

pyxel.show()
```

@TODO: descrever loops for


@TODO: descrever animação



@TODO: descrever animação
