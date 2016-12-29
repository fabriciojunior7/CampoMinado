import pygame, sys, os

#Cores
branco = (255, 255, 255)
preto = (0, 0 , 0)
verde = (0, 200, 0)
azul = (0, 0, 255)

def main():

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
        sup2.fill(azul)
        tela.blit(sup1 , (5, 5))
        tela.blit(sup2 , (410, 5))

main()