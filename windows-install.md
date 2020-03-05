Instruções de instalação num abiente Windows

# Recursos que devemos instalar

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

## Instalando o Visual Studio Code

Primeiro você precisa baixar o instalador do Visual Code Studio. É só entrar na
[página de downloads do VS Code](https://code.visualstudio.com/download) e clicar no botão abaixo do símbolo do Windows.

Ele vai abrir uma janela para escolher onde salvar o instalador. Pode baixar na pasta de Downloads mesmo. Se o seu navegador, mostrar o arquivo no rodapé, pode clicar para executá-lo. Caso contrário, vá na sua pasta de Downloads e mande executar o instalador.

Ao rodar o instalador, ele vai abrir uma janela de instalação. Pode seguir apenas apertando *Próximo* até que ele conclua a instalação.

Você pode verificar se deu tudo certinho abrindo o VS Code pelo menu do Windows.

## Instalando o Python 3.7+

No site do Python, vá até a [seção de downloads](https://www.python.org/downloads/windows/) para baixar a versão mais recente.

Após o download ser concluído, precisamos executar o instalador. Clique duas vezes sobre o arquivo e ele vai abrir uma janela de instalação. Nesse passo, precisamos marcar a caixinha que *Adiciona Python ao $PATH*.

![Janela de instalação com a opção de adicionar Python ao $PATH selecionada](https://files.realpython.com/media/win-install-dialog.40e3ded144b0.png)

Para verificar se o Python foi instalado, pode ir no menu e digitar Python e ele deve aparecer.

## Instalando o Pyxel

Com o Python 3.7 já instalado, podemos agora instalar o Pyxel. É só abrir o console do Python e copiar o comando a seguir, colar no console e apertar enter

```sh
pip install -U pyxel
```

## Baixando os arquivos do nosso tutorial

Precisamos baixar os dois arquivos que estão listados ali em cima:
- [Módulo auxiliar flappy.py](https://github.com/pyladiesdf/flappy-tutorial/blob/master/flappy.py)
- [Arquivo de imagens data.pyxres](https://github.com/pyladiesdf/flappy-tutorial/blob/master/data.pyxres)

Caso queira baixar os dois juntos, só pegar [neste link](https://drive.google.com/file/d/1Vfiml81eJLq-iNvFb2DezQ4zdFnWnrh3/view?usp=sharing). Aqui você vai encontrar os arquivos dentro de uma pasta zip. Peça para fazer o Download.

Depois, você deve encontrar a pasta zip, clicar com o botão direito e selecionar a opção *Extrair todos* e colocar na pasta que vamos fazer o nosso jogo. Lembre onde você deixou :)


# Mão na massa

Agora que já instalamos os recursos necessário, podemos voltar ao nosso [tutorial](https://github.com/pyladiesdf/flappy-tutorial#tutorial-parte-1-iniciando-o-jogo) :)
