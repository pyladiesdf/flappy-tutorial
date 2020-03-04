import flappy
import pyxel
...  # Coloque outros imports aqui!


#===============================================================================
# Constantes e variáveis
#===============================================================================
largura_tela = 175
altura_tela = 255
abertura_cano = 200
gravidade = 1
pulo = 8
...  # Coloque outras variáveis aqui!


#===============================================================================
# Funções
#===============================================================================
def desenhar():
    desenhar_fundo()
    desenhar_nuvens()
    desenhar_canos()
    desenhar_chao()
    desenhar_flappy()
    desenhar_instrucoes()


...  # Coloque outras funções aqui!


#
# Iniciar jogo
#
flappy.comecar()