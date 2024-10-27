import pygame
from graficaEFotoMod import HEIGHT

class muroAlto(pygame.sprite.Sprite):

    def __init__(self, x_muro, y_muro, lunghezza, altezza):

        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('sprites\staccionatasxdx.png')
        self.rect = self.image.get_rect()
        self.rect.x = x_muro
        self.rect.y = y_muro
