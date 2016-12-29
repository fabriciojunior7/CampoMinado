import pygame, sys, os
import casas

#Cores
branco = (255, 255, 255)
preto = (0, 0 , 0)
verde = (0, 200, 0)
azul = (0, 0, 255)

def main():
    quadrado = 100
    locais = []
    xx = 0
    yy = -10

    for num in range(quadrado):
        if(num % 10 != 0):
            novaCasa = casas.Casa(xx, yy)
            xx += 35
        else:
            yy += 35
            xx = 45
            novaCasa = casas.Casa(xx, yy)

        locais.append(novaCasa)

    os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (200, 200)

    largura = 600
    altura = 400
    pygame.init()
    tela = pygame.display.set_mode((largura, altura))
    pygame.display.set_caption("Campo Minado!")
    relogio = pygame.time.Clock()
    frames = 30

    #Superficies
    sup1 = pygame.Surface((400, altura-10))
    sup2 = pygame.Surface((185, altura-10))

    while(True):
        for event in pygame.event.get():
            if(event.type == pygame.QUIT):
                pygame.quit()
                sys.exit()

        #Rodar
        relogio.tick(frames)
        pygame.display.update()
        #Desenhar
        tela.fill(branco)
        sup1.fill(verde)
        #Superficie 1
        for e in locais:
            e.pintar(sup1)
        #Superficie 2
        sup2.fill(azul)
        tela.blit(sup1 , (5, 5))
        tela.blit(sup2 , (410, 5))



main()