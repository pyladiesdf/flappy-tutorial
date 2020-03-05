from collections import namedtuple
from random import randrange
import pyxel

#
# Constantes
#
LARGURA = 255
ALTURA = 255
ABERTURA = 200
GRAVIDADE = 1


def atualizar():
    """
    Atualiza o jogo. Roda a cada frame.
    """
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


def reiniciar():
    """
    Reinicia as variáveis de estado que controlam o jogo.
    """
    global ativo, morto, flappy_x, flappy_y, score, velocidade, canos

    ativo = False
    morto = False
    flappy_x = LARGURA / 3
    flappy_y = ALTURA / 2
    velocidade = 0
    canos = [((i * 80) + LARGURA, randrange(-100, 0, 10)) for i in range(4)]
    score = 0


def atualizar_jogo():
    """
    Atualiza as variáveis em cada frame de jogo.
    """
    global velocidade, flappy_x, flappy_y, morto, score
    
    # Atualiza o Flappy calculando a gravidade e a existência de pulos
    velocidade += GRAVIDADE
    if not morto and (pyxel.btnp(pyxel.KEY_SPACE) or pyxel.btnp(pyxel.KEY_UP)):
        velocidade = -8
    flappy_y += velocidade
    
    # Limita velocidade e impõe deslocamento quando jogador morrer
    flappy_y = min(flappy_y, ALTURA - 29)
    if morto:
        flappy_x -= 1

    # Atualiza os canos movendo cada posição x 1 pixel para a esquerda.
    # Caso o cano ultrapasse o início da tela, cria um novo cano.
    for i, (x, y) in enumerate(canos):
        x -= 1
        if x < -80:
            x += LARGURA + 80
            y = randrange(-100, 0, 10)
        canos[i] = (x, y)

    # Verifica colisões
    if flappy_y > ALTURA - 30:
        morto = True
    
    for i, (x, y) in enumerate(canos):
        colide_x = x + 12.5 > flappy_x > x - 12.5
        colide_y = flappy_y > y + ABERTURA or flappy_y < y + 140 
        if colide_x and colide_y:
            morto = True
    
    # Atualiza o score quando o flappy possui a mesma posição de algum cano
    for (x, y) in canos:
        if flappy_x == x:
            score += 1


def desenhar():
    """
    Desenha elementos na tela.
    """
    # Fundo azul
    pyxel.cls(12)
 
    # Canos: cada cano é representado por uma tupla (x, y), com a posição do
    # em x e a altura do cano
    for (x, y) in canos:
        pyxel.blt(x, y, 1, 0, 0, 25, 150, 0)
        pyxel.blt(x, y + ABERTURA, 1, 0, 0, -25, -150, 0)

    # Chão: desenhamos duas texturas separadas pela largura da tela que
    # se deslocam 1 pixel por frame
    offset = -pyxel.frame_count % LARGURA
    pyxel.bltm(offset, ALTURA - 16, 0, 0, 0, 32, 3)
    pyxel.bltm(offset - LARGURA, ALTURA - 16, 0, 0, 0, 32, 3)

    # Flappy
    frame = (pyxel.frame_count // 4) % 3
    pyxel.blt(flappy_x, flappy_y, 0, 0, frame * 16, 17, 13, 0)
        
    # Desenha instruções na tela e placar
    if not ativo:
        msg = "APERTE ESPACO OU SETA PARA CIMA PARA COMECAR"
        pyxel.text(LARGURA / 2 - len(msg) * 2, ALTURA / 3, msg, 7)
    else:
        pyxel.text(LARGURA // 2, ALTURA // 3, str(score), 7)
    
    if morto:
        msg = "Aperte R para reiniciar"
        pyxel.text(LARGURA // 2 - len(msg) * 2, ALTURA // 2, msg, 7)


#
# Iniciar jogo
#
reiniciar() 
pyxel.init(width=LARGURA, height=ALTURA, caption="Flappy Bird", fps=35)
pyxel.load('data.pyxres')
pyxel.run(atualizar, desenhar)