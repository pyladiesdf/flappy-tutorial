# <img src="https://raw.githubusercontent.com/kitao/pyxel/master/pyxel/examples/assets/pyxel_logo_152x64.png">

[ [English](https://github.com/kitao/pyxel/blob/master/README.md) | [日本語](https://github.com/kitao/pyxel/blob/master/README.ja.md) | [中文](https://github.com/kitao/pyxel/blob/master/README.cn.md) | [한국어](https://github.com/kitao/pyxel/blob/master/README.ko.md) | [Español](https://github.com/kitao/pyxel/blob/master/README.es.md) ]

**Pyxel** é uma engine retro de games para Python.

Graças as suas simples especificações inspiradas em games retro, como jogos com apenas 16 cores e 4 sons tocados ao mesmo tempo, você pode se sentir livre para se divertir fazendo jogos com estilo de pixel arte.

<a href="https://github.com/kitao/pyxel/blob/master/pyxel/examples/01_hello_pyxel.py" target="_blank">
<img src="https://raw.githubusercontent.com/kitao/pyxel/master/pyxel/examples/screenshots/01_hello_pyxel.gif" width="48%">
</a>

<a href="https://github.com/kitao/pyxel/blob/master/pyxel/examples/02_jump_game.py" target="_blank">
<img src="https://raw.githubusercontent.com/kitao/pyxel/master/pyxel/examples/screenshots/02_jump_game.gif" width="48%">
</a>

<a href="https://github.com/kitao/pyxel/blob/master/pyxel/examples/03_draw_api.py" target="_blank">
<img src="https://raw.githubusercontent.com/kitao/pyxel/master/pyxel/examples/screenshots/03_draw_api.gif" width="48%">
</a>

<a href="https://github.com/kitao/pyxel/blob/master/pyxel/examples/04_sound_api.py" target="_blank">
<img src="https://raw.githubusercontent.com/kitao/pyxel/master/pyxel/examples/screenshots/04_sound_api.gif" width="48%">
</a>

<a href="https://github.com/kitao/pyxel/blob/master/pyxel/editor/screenshots/image_tilemap_editor.gif" target="_blank">
<img src="https://raw.githubusercontent.com/kitao/pyxel/master/pyxel/editor/screenshots/image_tilemap_editor.gif" width="48%">
</a>

<a href="https://github.com/kitao/pyxel/blob/master/pyxel/editor/screenshots/sound_music_editor.gif" target="_blank">
<img src="https://raw.githubusercontent.com/kitao/pyxel/master/pyxel/editor/screenshots/sound_music_editor.gif" width="48%">
</a>

As especificações do console de jogos e APIs para Pyxel são uma referencia aos incríveis [PICO-8](https://www.lexaloffle.com/pico-8.php) e [TIC-80](https://tic.computer/).

Pyxel é uma open source e de graça para usar. Vamos começar a fazer um jogo retro com Pyxel!

## Especificações

- Roda no Windows, Mac, and Linux
- Programado em Python3
- Paleta de 16 cores predefinidas 
- 3 bancos de imagem de tamanho 256x256
- 8 Tilemaps de tamanho 256x256
- 4 canais com 64 sons definíveis
- 8 musicas que podem combinar sons arbitrários
- Entradas para teclado, mouse e controle
- Editor de imagem e som

### Paleta de Cores

<img src="https://raw.githubusercontent.com/kitao/pyxel/master/pyxel/examples/screenshots/05_color_palette.png">
<br><br>
<img src="https://raw.githubusercontent.com/kitao/pyxel/master/pyxel/examples/assets/pyxel_palette.png">

## Como Instalar

### Windows

Depois de instalar o [Python3](https://www.python.org/) (versão 3.7 ou superior), o seguinte comando `pip` instala o Pyxel:

```sh
pip install -U pyxel
```

### Mac

Depois de instalar o [Python3](https://www.python.org/) (versão 3.7 ou superior) e o [SDL2](https://www.libsdl.org/), intale o Pyxel com o comando `pip`.

Caso o gerenciador de pacotes [Homebrew](https://brew.sh/) estiver pronto, o seguinte comando instala todos os pacotes necessários:

```sh
brew install python3 sdl2 sdl2_image
```

Depois de reiniciar o terminal,

```sh
pip3 install -U pyxel
```

### Linux

Instale o [Python3](https://www.python.org/) (versão 3.7 ou superior) e os pacotes requeridos de uma maneira apropriada para cada distribuição.

**Ubuntu:**

```sh
sudo apt install python3 python3-pip libsdl2-dev libsdl2-image-dev
sudo -H pip3 install -U pyxel
```

### Outros ambientes

Para instalar o Pyxel em outro ambiente diferente dos acima (32-bit Linux, Rapberry PI, e etc.), siga os passos abaixo:

#### Instale as ferramentes e pacotes necessários

- C++ build toolchain (deve incluir gcc e o comando make )
- libsdl2-dev e libsdl2-image-dev
- [Python3](https://www.python.org/) (versão 3.7 ou superior) e o comando pip

#### Execute o seguinte comando em qualquer pasta

```sh
git clone https://github.com/kitao/pyxel.git
cd pyxel
make -C pyxel/core clean all
pip3 install .
```

### Instale os exemplos

Depois de instalar o Pyxel, os exemplos do Pyxel serão copiados para o atual diretório com o seguinte comando:

```sh
install_pyxel_examples
```

Os exemplos copiados são:

- [01_hello_pyxel.py](https://github.com/kitao/pyxel/blob/master/pyxel/examples/01_hello_pyxel.py) - Aplicação simples
- [02_jump_game.py](https://github.com/kitao/pyxel/blob/master/pyxel/examples/02_jump_game.py) - Jogo de plataforma com o arquivo de recurso do Pyxel
- [03_draw_api.py](https://github.com/kitao/pyxel/blob/master/pyxel/examples/03_draw_api.py) - Demonstração da API de desenho
- [04_sound_api.py](https://github.com/kitao/pyxel/blob/master/pyxel/examples/04_sound_api.py) - Demonstração da API de som
- [05_color_palette.py](https://github.com/kitao/pyxel/blob/master/pyxel/examples/05_color_palette.py) - Lista de cores da paleta
- [06_click_game.py](https://github.com/kitao/pyxel/blob/master/pyxel/examples/06_click_game.py) - Jogo de mouse clicke
- [07_snake.py](https://github.com/kitao/pyxel/blob/master/pyxel/examples/07_snake.py) - Jogo da cobrinha com BGM
- [08_triangle_api.py](https://github.com/kitao/pyxel/blob/master/pyxel/examples/08_triangle_api.py) - Demonstração da API de desenho de triangulos

Os exemplos podem ser executados como codigos normais do Python:

**Windows:**

```sh
cd pyxel_examples
python 01_hello_pyxel.py
```

**Mac / Linux:**

```sh
cd pyxel_examples
python3 01_hello_pyxel.py
```

## Como usar

### Crie uma aplicação Pyxel

Depois de importar o módulo Pyxel no seu códico Python, especifique o temanho da janela com a função `init` primeiro, depois inicie a aplicação Pyxdel com a função `run`.

```python
import pyxel

pyxel.init(160, 120)

def update():
    if pyxel.btnp(pyxel.KEY_Q):
        pyxel.quit()

def draw():
    pyxel.cls(0)
    pyxel.rect(10, 10, 20, 20, 11)

pyxel.run(update, draw)
```

The arguments of `run` function are `update` function to update each frame and `draw` function to draw screen when necessary.

In an actual application, it is recommended to wrap pyxel code in a class as below:

```python
import pyxel

class App:
    def __init__(self):
        pyxel.init(160, 120)
        self.x = 0
        pyxel.run(self.update, self.draw)

    def update(self):
        self.x = (self.x + 1) % pyxel.width

    def draw(self):
        pyxel.cls(0)
        pyxel.rect(self.x, 0, 8, 8, 9)

App()
```

Também é possivel escrever um codigo simples usando as funções `show` e `flip` para desenhar gráficos simples e animações.

A função `show` exibe a tela e espera até que a tecla `ESC` seja pressionada.

```python
import pyxel

pyxel.init(120, 120)
pyxel.cls(1)
pyxel.circb(60, 60, 40, 7)
pyxel.show()
```

A função `flip` atualiza a tela uma vez.

```python
import pyxel

pyxel.init(120, 80)

while True:
    pyxel.cls(3)
    pyxel.rectb(pyxel.frame_count % 160 - 40, 20, 40, 40, 7)
    pyxel.flip()
```

### Controles especiais
Os seguintes controles especiais podem ser usados enquanto uma aplicação Pyxel está funcionando.

- `Esc`<br>
Sai do aplicativo
- `Alt(Option)+1`<br>
Salva a screenshot na área de trabalho
- `Alt(Option)+2`<br>
Reseta a hora início da gravação do vídeo de captura de tela 
- `Alt(Option)+3`<br>
Salva o vídeo de captura de tela (gif) na área de trabalho (até 30 segundos) 
- `Alt(Option)+0`<br>
Ativa/Desativa o monitor de desempenho (fps, tempo de atualização, e tempo de desenho)
- `Alt(Option)+Enter`<br>
Ativa/Desativa a tela cheia

### Como criar um recurso

O Pyxel Editor anexado pode criar imagens e sons usados em uma aplicação Pyxel.

O Pyxel Editor é aberto com o seguinte comando:

```sh
pyxeleditor [pyxel_resource_file]
```

Caso o arquivo de recurso Pyxel especificado (.pyxres) exista, o arquivo será carregado, e se ele não existe, um novo arquivo será criado com o nome especificado.
Se o nome do arquivo de recurso não for especificado, o nome será `my_resource.pyxres`.  

Depois de iniciar o Pyxel Editor, o arquivo pode ser trocado apenas arrastando e soltando outro arquivo de recurso. Caso o arquivo de recurso for arrastado e solto enquanto a tecla ``Ctrl``(``Cmd``) esteja sendo pressionada, apenas o tipo de recurso (image/tilemap/sound/music) que está atualmente sendo editado será carregado. Essa operação permite combinar diferentes arquivos de recurso em um só.

O arquivo de recurso criado pode ser carregado com a função `load`.

O Pyxel Editor tem os seguintes modos de edição.

**Editor de imagem:**

O modo para editar os bancos de imagem.

<img src="https://raw.githubusercontent.com/kitao/pyxel/master/pyxel/editor/screenshots/image_editor.gif">

Apenas arrastando e soltando o arquivo png na tela do editor de imagem, a imagem será carregada no atual banco de imagens selecionado.

**Editor de tilemap:**

O modo para editar tilempas onde as imagens do banco de imagens são organizadas em um padrão de ladrilhos.

<img src="https://raw.githubusercontent.com/kitao/pyxel/master/pyxel/editor/screenshots/tilemap_editor.gif">

**Editor de som:**

O modo para editar sons.

<img src="https://raw.githubusercontent.com/kitao/pyxel/master/pyxel/editor/screenshots/sound_editor.gif">

**Editor de musica:**

O modo para editar musicas onde os sons são organizados na ordem de reprodução.

<img src="https://raw.githubusercontent.com/kitao/pyxel/master/pyxel/editor/screenshots/music_editor.gif">

### Outros métodos de criação de recursos

Imagens Pyxel e tilemaps também podem ser criados da seguinte maneira:

- Crie uma imagem da lista de strings com a função `Image.set` ou `Tilemap.set`.
- Carregue o arquivo png na paleta Pyxel com a função `Image.load`.

Sons do Pyxel também podem ser criados da seguinte forma:

- Crie um som das strings com a função `Sound.set` ou `Music.set`.

Consulte a referência da API para usar essas funções.

### Como criar um executável independente

Usando o empacotador Pyxel predefinido, o executável independente vai funcionar mesmo em ambientes onde o Python não esta instaldo pode ser criado.

Para criar um executável independente, especifique o arquivo Python a ser usado para iniciar a aplicação com o comando `pyxelpackager`:

```sh
pyxelpackager python_file
```

Quando o processo estiver completo, o executável independente sera criado na pasta `dist`.

Caso recursos tais como arquivos .pyxres e .png também forem necessários, coloque-os na pasta `assets` e eles serão incluidos.

Também é possível especificar um ícone com a opção ``-i icon_file``.

## Referência API

### Sistema

- `width`, `height`<br>
A largura e a altura da tela

- `frame_count`<br>
O número de frames decorridos

- `init(width, height, [caption], [scale], [palette], [fps], [border_width], [border_color], [quit_key])`<br>
Inicia a aplicação Pyxel com o tamanho da tela (`width`, `height`). O máximo de largura e altura da tela é 256<br>
Também é  possível especificar o título da janela com `caption`, a ampliação da tela com `scale`, a cor da paleta com `palette`, a taxa de quadros com `fps`, a largura da margem e a cor fora da tela com `color_width` e `border_color`, e a tecla para sair da aplicação com `quit_key`. `palette` é especificada como uma lista de 16 elementos de cores de 24 bits, `border_color` como uma cor de 24 bits. <br>
e. g. `pyxel.init(160, 120, caption="Pyxel with PICO-8 palette", palette=[0x000000, 0x1D2B53, 0x7E2553, 0x008751, 0xAB5236, 0x5F574F, 0xC2C3C7, 0xFFF1E8, 0xFF004D, 0xFFA300, 0xFFEC27, 0x00E436, 0x29ADFF, 0x83769C, 0xFF77A8, 0xFFCCAA], quit_key=pyxel.KEY_NONE)`

- `run(update, draw)`<br>
Inicia o aplicativo Pyxcel e chama a função `update` para atualização de frame e a função `draw` para desenhar

- `quit()`<br>
Sai do aplicativo Pyxel no final do frame atual

- `flip()`<br>
Force drawing the screen (não use em aplicações normais)

- `show()`<br>
Desenha a tela e espera para sempre (não use em aplicações normais)

### Recurso

- `save(filename)`<br>
Save the resource file (.pyxres) to the directory of the execution script

- `load(filename, [image], [tilemap], [sound], [music])`<br>
Read the resource file (.pyxres) from the directory of the execution script. If ``False`` is specified for the resource type (image/tilemap/sound/music), the resource will not be loaded.

### Input
- `mouse_x`, `mouse_y`<br>
The current position of the mouse cursor

- `btn(key)`<br>
Return `True` if `key` is pressed, otherwise return `False` ([key definition list](https://github.com/kitao/pyxel/blob/master/pyxel/__init__.py))

- `btnp(key, [hold], [period])`<br>
Return `True` if `key` is pressed at that frame, otherwise return `False`. When `hold` and `period` are specified, `True` will be returned at the `period` frame interval when the `key` is held down for more than `hold` frames

- `btnr(key)`<br>
Return `True` if `key` is released at that frame, otherwise return `False`

- `mouse(visible)`<br>
If `visible` is `True`, show the mouse cursor. If `False`, hide it. Even if the mouse cursor is not displayed, its position is updated.

### Graphics

- `image(img, [system])`<br>
Operate the image bank `img`(0-2) (see the Image class). If `system` is `True`, the image bank for system can be accessed. 3 is for the font and resource editor. 4 is for the display screen<br>
e.g. `pyxel.image(0).load(0, 0, "title.png")`

- `tilemap(tm)`<br>
Operate the tilemap `tm`(0-7) (see the Tilemap class)

- `clip(x, y, w, h)`<br>
Set the drawing area of the screen from (`x`, `y`) to width `w` and height `h`. Reset the drawing area to full screen with `clip()`

- `pal(col1, col2)`<br>
Replace color `col1` with `col2` at drawing. `pal()` to reset to the initial palette

- `cls(col)`<br>
Clear screen with color `col`

- `pget(x, y)`<br>
Get the color of the pixel at (`x`, `y`)

- `pset(x, y, col)`<br>
Draw a pixel of color `col` at (`x`, `y`)

- `line(x1, y1, x2, y2, col)`<br>
Draw a line of color `col` from (`x1`, `y1`) to (`x2`, `y2`)

- `rect(x, y, w, h, col)`<br>
Draw a rectangle of width `w`, height `h` and color `col` from (`x`, `y`)

- `rectb(x, y, w, h, col)`<br>
Draw the outline of a rectangle of width `w`, height `h` and color `col` from (`x`, `y`)

- `circ(x, y, r, col)`<br>
Draw a circle of radius `r` and color `col` at (`x`, `y`)

- `circb(x, y, r, col)`<br>
Draw the outline of a circle of radius `r` and color `col` at (`x`, `y`)

- `tri(x1, y1, x2, y2, x3, y3, col)`<br>
Draw a triangle with vertices (`x1`, `y1`), (`x2`, `y2`), (`x3`, `y3`) and color `col`

- `trib(x1, y1, x2, y2, x3, y3, col)`<br>
Draw the outline of a triangle with vertices (`x1`, `y1`), (`x2`, `y2`), (`x3`, `y3`) and color `col`

- `blt(x, y, img, u, v, w, h, [colkey])`<br>
Copy the region of size (`w`, `h`) from (`u`, `v`) of the image bank `img`(0-2) to (`x`, `y`). If negative value is set for `w` and/or `h`, it will reverse horizontally and/or vertically. If `colkey` is specified, treated as transparent color

- `bltm(x, y, tm, u, v, w, h, [colkey])`<br>
Draw the tilemap `tm`(0-7) to (`x`, `y`) according to the tile information of size (`w`, `h`) from (`u`, `v`). If `colkey` is specified, treated as transparent color. A tile of the tilemap is drawn with a size of 8x8, and if the tile number is 0, indicates the region (0, 0)-(7, 7) of the image bank, if 1, indicates (8, 0)-(15, 0)

- `text(x, y, s, col)`<br>
Draw a string `s` of color `col` at (`x`, `y`)

### Audio

- `sound(snd, [system])`<br>
Operate the sound `snd`(0-63) (see the Sound class). If `system` is `True`, the sound 64 for system can be accessed<br>
e.g. `pyxel.sound(0).speed = 60`

- `music(msc)`<br>
Operate the music `msc`(0-7) (see the Music class)

- `play_pos(ch)`<br>
Get the sound playback position of channel `ch`. The 100's and 1000's indicate the sound number and the 1's and 10's indicate the note number. When playback is stopped, return `-1`

- `play(ch, snd, loop=False)`<br>
Play the sound `snd`(0-63) on channel `ch`(0-3). Play in order when `snd` is a list

- `playm(msc, loop=False)`<br>
Play the music `msc`(0-7)

- `stop([ch])`<br>
Stop playback of all channels. If `ch`(0-3) is specified, stop the corresponding channel only

### Image Class

- `width`, `height`<br>
The width and height of the image

- `data`<br>
The data of the image (256x256 two-dimentional list)

- `get(x, y)`<br>
Retrieve the data of the image at (`x`, `y`)

- `set(x, y, data)`<br>
Set the data of the image at (`x`, `y`) by a value or a list of strings<br>
e.g. `pyxel.image(0).set(10, 10, ["1234", "5678", "9abc", "defg"])`

- `load(x, y, filename)`<br>
Read the png image from the directory of the execution script at (`x`, `y`)

- `copy(x, y, img, u, v, w, h)`<br>
Copy the region of size (`w`, `h`) from (`u`, `v`) of the image bank `img`(0-2) to (`x`, `y`)

### Tilemap Class

- `width`, `height`<br>
The width and height of the tilemap

- `data`<br>
The data of the tilemap (256x256 two-dimentional list)

- `refimg`<br>
The image bank referenced by the tilemap

- `get(x, y)`<br>
Retrieve the data of the tilemap at (`x`, `y`)

- `set(x, y, data)`<br>
Set the data of the tilemap at (`x`, `y`) by a value or a list of strings.<br>
e.g. `pyxel.tilemap(0).set(0, 0, ["000102", "202122", "a0a1a2", "b0b1b2"])`

- `copy(x, y, tm, u, v, w, h)`<br>
Copy the region of size (`w`, `h`) from (`u`, `v`) of the tilemap `tm`(0-7) to (`x`, `y`)

### Sound Class

- `note`<br>
List of note(0-127) (33 = 'A2' = 440Hz)

- `tone`<br>
List of tone(0:Triangle / 1:Square / 2:Pulse / 3:Noise)

- `volume`<br>
List of volume(0-7)

- `effect`<br>
List of effects(0:None / 1:Slide / 2:Vibrato / 3:FadeOut)

- `speed`<br>
The length of one note(120 = 1 second per tone)

- `set(note, tone, volume, effect, speed)`<br>
Set a note, tone, volume, and effect with a string. If the tone, volume, and effect length are shorter than the note, it is repeated from the beginning

- `set_note(note)`<br>
Set the note with a string made of 'CDEFGAB'+'#-'+'0123' or 'R'. Case-insensitive and whitespace is ignored<br>
e.g. `pyxel.sound(0).set_note("G2B-2D3R RF3F3F3")`

- `set_tone(tone)`<br>
Set the tone with a string made of 'TSPN'. Case-insensitive and whitespace is ignored<br>
e.g. `pyxel.sound(0).set_tone("TTSS PPPN")`

- `set_volume(volume)`<br>
Set the volume with a string made of '01234567'. Case-insensitive and whitespace is ignored<br>
e.g. `pyxel.sound(0).set_volume("7777 7531")`

- `set_effect(effect)`<br>
Set the effect with a string made of 'NSVF'. Case-insensitive and whitespace is ignored<br>
e.g. `pyxel.sound(0).set_effect("NFNF NVVS")`

### Music Class

- `ch0`<br>
List of sound(0-63) play on channel 0. If an empty list is specified, the channel is not used for playback

- `ch1`<br>
List of sound(0-63) play on channel 1. If an empty list is specified, the channel is not used for playback

- `ch2`<br>
List of sound(0-63) play on channel 2. If an empty list is specified, the channel is not used for playback

- `ch3`<br>
List of sound(0-63) play on channel 3. If an empty list is specified, the channel is not used for playback

- `set(ch0, ch1, ch2, ch3)`<br>
Set the list of sound(0-63) of all channels. If an empty list is specified, that channel is not used for playback<br>
e.g. `pyxel.music(0).set([0, 1], [2, 3], [4], [])`

- `set_ch0(data)`<br>
Set the list of sound(0-63) of channel 0

- `set_ch1(data)`<br>
Set the list of sound(0-63) of channel 1

- `set_ch2(data)`<br>
Set the list of sound(0-63) of channel 2

- `set_ch3(data)`<br>
Set the list of sound(0-63) of channel 3

## How to Contribute

### Submitting an issue

Use the [issue tracker](https://github.com/kitao/pyxel/issues) to submit bug reports and feature/enhancement requests.
Before submitting a new issue, search the issue tracker to ensure that there is no similar open issue.

When submitting a report, select the appropriate template from [this link](https://github.com/kitao/pyxel/issues/new/choose).

### Manual testing

Anyone manually testing the code and reporting bugs or suggestions for enhancements in the issue tracker are very welcome!

### Submitting a pull request

Patches/fixes are accepted in form of pull requests (PRs). Make sure the issue the pull request addresses is open in the issue tracker.

Submitted pull request is deemed to have agreed to publish under [MIT license](https://github.com/kitao/pyxel/blob/master/LICENSE).

## Other Information

- [Wiki](https://github.com/kitao/pyxel/wiki)
- [Subreddit](https://www.reddit.com/r/pyxel/)

## License

Pyxel is under [MIT license](http://en.wikipedia.org/wiki/MIT_License). It can be reused within proprietary software provided that all copies of the licensed software include a copy of the MIT License terms and the copyright notice.

Pyxel uses the following libraries:

- [SDL2](https://www.libsdl.org/)
- [miniz-cpp](https://github.com/tfussell/miniz-cpp)
- [PyInstaller](https://www.pyinstaller.org/)
