import sys as _sys
from random import randrange as _randrange, randint as _randint

import pyxel


class _Names:
    """
    Objeto auxiliar para recuperar variáveis globais ou definidas pelo usuário.
    """

    _aliases = {
        'começar': 'comecar',
        'atualizar_colisões': 'atualizar_colisoes',
        'desenhar_chão': 'desenhar_chao',
        'desenhar_instruções': 'desenhar_instrucoes',
    }
    _exports = (
        'atualizar',
        'reiniciar',
        'atualizar_jogo',
        'atualizar_flappy',
        'atualizar_canos',
        'atualizar_colisoes',
        'atualizar_score',
        'desenhar',
        'desenhar_fundo',
        'desenhar_nuvens',
        'desenhar_canos',
        'desenhar_chao',
        'desenhar_flappy',
        'desenhar_instrucoes',
        'comecar',
    )

    def __init__(self):
        self._main = _sys.modules['__main__']
        self._fallback = _sys.modules[__name__]
        for name in self._exports:
            if not hasattr(self._main, name):
                setattr(self._main, name, getattr(self._fallback, name))

    def __getattr__(self, name):
        name = self._aliases.get(name, name)

        if name.startswith('_'):
            raise AttributeError(name)
        elif hasattr(self._main, name):
            return getattr(self._main, name)
        elif hasattr(self._fallback, name):
            return getattr(self._fallback, name)

        msg = f'Nome não reconhecido: {name}. Será que você digitou errado?'
        raise NameError(msg)

    def __setattr__(self, name, value):
        if name in ('_main', '_fallback'):
            super().__setattr__(name, value)
        else:
            name = self._aliases.get(name, name)
            setattr(self._main, name, value)


noop = lambda *args, **kwargs: None
id = lambda x, *args, **kwargs: x
do = lambda fn, *args, **kwargs: (noop if fn is None else fn)(*args, **kwargs)


def atualizar():
    """
    Atualiza o jogo. Roda a cada frame.
    """
    # Sai com Q ou ESC
    if pyxel.btnp(pyxel.KEY_Q):
        pyxel.quit()

    # Reinicia com R
    elif _.ativo and pyxel.btnp(pyxel.KEY_R):
        do(_.reiniciar)

    # Roda o jogo
    elif _.ativo:
        do(_.atualizar_jogo)

    # Ativa com espaço ou seta para cima
    elif pyxel.btnp(pyxel.KEY_SPACE) or pyxel.btnp(pyxel.KEY_UP):
        _.ativo = True


def reiniciar():
    """
    Reinicia as variáveis de estado que controlam o jogo.
    """
    _.ativo = False
    _.morto = False
    _.flappy_x = _.largura_tela // 3
    _.flappy_y = _.altura_tela // 2
    _.velocidade = 0
    distancia_canos = 80
    cano1 = _.largura_tela + distancia_canos * 0, -10 * _randint(1, 8)
    cano2 = _.largura_tela + distancia_canos * 1, -10 * _randint(1, 8)
    cano3 = _.largura_tela + distancia_canos * 2, -10 * _randint(1, 8)
    cano4 = _.largura_tela + distancia_canos * 3, -10 * _randint(1, 8)
    _.canos = [cano1, cano2, cano3, cano4]
    _.score = 0


#==============================================================================
# Atualizar mecânicas do jogo 
#==============================================================================
def atualizar_jogo():
    """
    Atualiza as variáveis em cada frame de jogo.
    """

    do(_.atualizar_flappy)
    do(_.atualizar_canos)
    do(_.atualizar_colisoes)
    do(_.atualizar_score)


# Atualiza o Flappy calculando a gravidade e a existência de pulos
def atualizar_flappy():
    _.velocidade += _.gravidade
    if not _.morto and (pyxel.btnp(pyxel.KEY_SPACE) or pyxel.btnp(pyxel.KEY_UP)):
        _.velocidade = -_.pulo
    _.flappy_y += _.velocidade

    # Limita velocidade e impõe deslocamento quando jogador morrer
    _.flappy_y = min(_.flappy_y, _.altura_tela - 29)
    if _.morto:
        _.flappy_x -= 1


# Atualiza os canos movendo cada posição x 1 pixel para a esquerda.
# Caso o cano ultrapasse o início da tela, cria um novo cano.
def atualizar_canos():
    canos = _.canos
    for i, (x, y) in enumerate(canos):
        x -= 1
        if x < -80:
            xmax = max(x for (x, _) in _.canos)
            x += xmax + 160
            y = _randrange(-100, 0, 10)
        canos[i] = (x, y)


# Verifica colisões
def atualizar_colisoes():
    if _.flappy_y > _.altura_tela - 30:
        _.morto = True

    for i, (x, y) in enumerate(_.canos):
        colide_x = _.flappy_x + 17 > x and _.flappy_x < x + 25
        colide_y = _.flappy_y < y + 135 or _.flappy_y + 13 > y + _.abertura_cano
        if colide_x and colide_y:
            _.morto = True


# Atualiza o score quando o flappy possui a mesma posição de algum cano
def atualizar_score():
    for (x, y) in _.canos:
        if _.flappy_x == x:
            _.score += 1


#==============================================================================
# Desenha elementos de jogo 
#==============================================================================
def desenhar():
    """
    Desenha elementos na tela.
    """
    do(_.desenhar_fundo)
    do(_.desenhar_nuvens)
    do(_.desenhar_canos)
    do(_.desenhar_chao)
    do(_.desenhar_flappy)
    do(_.desenhar_instrucoes)


# Fundo azul
def desenhar_fundo():
    pyxel.cls(12)


# Nuvens com paralaxe
def desenhar_nuvens():
    offset = -pyxel.frame_count // 2
    pyxel.blt(offset % (_.largura_tela + 32) - 32, _.altura_tela // 2, 2, 0, 16, 32, 32, 12)
    pyxel.blt((offset + 96) % (_.largura_tela + 32) - 32, _.altura_tela // 4, 2, 0, 48, 32, 32, 12)
    pyxel.blt(offset % (_.largura_tela + 32) - 64, int(_.altura_tela / 1.5), 2, 0, 80, 32, 32, 12)


# Canos: cada cano é representado por uma tupla (x, y), com a posição do
# em x e a altura do cano
def desenhar_canos():
    for (x, y) in _.canos:
        pyxel.blt(x, y, 1, 0, 0, 25, 135, 0)
        pyxel.blt(x, y + _.abertura_cano, 1, 0, 0, 25, -135, 0)


# Chão: desenhamos duas texturas separadas pela largura da tela que
# se deslocam 1 pixel por frame
def desenhar_chao():
    offset = -pyxel.frame_count % _.largura_tela
    pyxel.bltm(offset, _.altura_tela - 16, 0, 0, 0, 32, 3)
    pyxel.bltm(offset - _.largura_tela, _.altura_tela - 16, 0, 0, 0, 32, 3)


# Flappy
def desenhar_flappy():
    frame = (pyxel.frame_count // 4) % 3
    pyxel.blt(_.flappy_x, _.flappy_y, 0, 0, frame * 16, 17, 13, 0)


# Desenha instruções na tela e placar
def desenhar_instrucoes():
    if not _.ativo:
        msg = "Espaco ou seta para cima para comecar"
        pyxel.text(_.largura_tela // 2 - len(msg) * 2, _.altura_tela // 3, msg, 7)
    else:
        pyxel.text(_.largura_tela // 2, _.altura_tela // 3, str(_.score), 7)

    if _.morto:
        msg = "Aperte R para reiniciar"
        pyxel.text(_.largura_tela // 2 - len(msg) * 2, _.altura_tela // 2, msg, 7)


#
# Iniciar jogo
#
def comecar():
    _.reiniciar()
    desenhar = _.desenhar or noop
    atualizar = _.atualizar or noop

    pyxel.init(width=_.largura_tela, height=_.altura_tela, caption="Flappy Bird", fps=35)
    pyxel.load('data.pyxres')
    pyxel.run(atualizar, desenhar)


#
# Apelidos
#
começar = comecar


#
# Constantes
#
_ = _Names()
_.largura_tela = 150
_.altura_tela = 255
_.abertura_cano = 200
_.gravidade = 1
_.pulo = 8


if __name__ == '__main__':
    comecar()