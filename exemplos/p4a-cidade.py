import pyxel

def desenhar_casa(x, y):
    pyxel.rect(x + 5, y + 20, 70, 35, 15) # parede
    pyxel.rect(x + 12, y + 30, 15, 25, 2)  # porta
    pyxel.rect(x + 32, y + 30, 15, 15, 2)  # janela 1
    pyxel.rect(x + 52, y + 30, 15, 15, 2)  # janela 2
    pyxel.rect(x, y, 80, 20, 4)            # telhado

# Pyxel
pyxel.init(200, 150)

# Ruas cinzas
pyxel.cls(5)

# Linha amarela
for x in range(0, 200, 30):
    pyxel.rect(x, 3, 15, 2, 10)

# Quarteirão de grama
pyxel.rect(20, 25, 180, 125, 3)

# Algumas casinhas...
desenhar_casa(25, 30)
desenhar_casa(25, 90)
desenhar_casa(115, 30)
desenhar_casa(115, 90)

# Desenha
pyxel.show()