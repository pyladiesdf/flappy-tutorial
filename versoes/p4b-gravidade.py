import pyxel

# Constantes
LARGURA = 220
ALTURA = 220

# Variáveis
pos_x = LARGURA / 2
pos_y = ALTURA / 2
vel_x = 0
vel_y = 0
gravidade = 1


def update():
    global pos_y, vel_y

    vel_y += gravidade
    pos_y += vel_y


def draw():
    pyxel.cls(12)
    pyxel.rect(pos_x, pos_y, 20, 20, 10)


pyxel.init(LARGURA, ALTURA, fps=35)
pyxel.run(update, draw)