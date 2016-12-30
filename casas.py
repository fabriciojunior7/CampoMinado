import pygame

#Cores
branco = (255, 255, 255)
preto = (0, 0 , 0)
verde = (0, 200, 0)
azul = (0, 0, 255)
vermelho = (255, 0, 0)
cinza = (50, 50, 50)
cinzaClaro = (160, 160, 160)

class Casa(object):
    def __init__(self, x, y, bomba):
        self.x = x
        self.y = y
        self.largura = 30
        self.altura = 30
        self.numero = 0
        self.bomba = bomba
        self.clicado = False
        self.bandeira = False
        self.corpo = pygame.Rect(self.x , self.y, self.largura, self.altura)

    def pintar(self, tela):
        pygame.draw.rect(tela, cinza, self.corpo)

    def pintar_mouse(self, tela):
        pygame.draw.rect(tela, cinzaClaro, self.corpo)

    def pintar_bandeira(self, tela):
        pygame.draw.rect(tela, vermelho, self.corpo)

    def pintar_clicado(self, tela):
        pygame.draw.rect(tela, branco, self.corpo)
