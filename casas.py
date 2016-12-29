import pygame

#Cores
branco = (255, 255, 255)
preto = (0, 0 , 0)
verde = (0, 200, 0)
azul = (0, 0, 255)
vermelho = (255, 0, 0)
cinza = (100, 100, 100)


class Casa(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.largura = 30
        self.altura = 30
        self.numero = 0
        self.bomba = False
        self.corpo = pygame.Rect(self.x , self.y, self.largura, self.altura)

    def pintar(self, tela):
        pygame.draw.rect(tela, cinza, self.corpo)