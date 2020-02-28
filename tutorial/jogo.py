import flappy
import pyxel
from random import randrange

#
# Constantes
#
largura_tela = 150
altura_tela = 255
abertura_cano = 200
gravidade = 1
pulo = 8


def desenhar():
    desenhar_fundo()
    desenhar_nuvens()
    desenhar_canos()
    desenhar_chao()
    desenhar_flappy()
    desenhar_instrucoes()


def desenhar_flappy():
    largura = 17
    altura = 13
    cor = 10
    pyxel.rect(flappy_x, flappy_y, largura, altura, cor)


def desenhar_chao():
    altura = 16
    cor = 11
    pyxel.rect(0, altura_tela - altura, largura_tela, altura, cor)


def desenhar_canos_():
    cor = 11
    for (x, y) in canos:
        pyxel.rect(x, y, 25, 135, cor)
        pyxel.rect(x, y + abertura_cano, 25, 135, cor)


def atualizar_canos():
    espaco_x = 80

    for i in range(4):
        x, y = canos[i]
        if x < -80:
            x += espaco_x * 4
            y = randrange(-100, 0, 10)
        canos[i] = (x - 1, y)


flappy.comecar()