import pygame
import random, time
from graficaEFotoMod import WIDTH, HEIGHT

class Fungo(pygame.sprite.Sprite):

                    #sprite del giocatore
    def __init__(self):

        pygame.sprite.Sprite.__init__(self)

        self.ora = pygame.time.get_ticks()
        self.frame_Corrente = 0
        self.ultimo_Update = 0
        
        self.toccato = True

        self.carica_Immagini()
        self.image = self.images[0]
        
        self.animazione()

        self.posizione()
        
        if self.toccato == True:

            self.rect.center = (0, 0)

            self.toccato = False

            self.posizione()


    def carica_Immagini(self):

        self.images = []

        self.images.append(pygame.image.load('sprites/fungo1.png'))
        self.images.append(pygame.image.load('sprites/fungo2.png'))

    def  animazione(self):

        foto = random.randrange(1, 2)

        self.image = self.images[foto]

        self.image.get_rect()

        self.mask = pygame.mask.from_surface(self.image)
            
    def posizione(self):

        self.rect = self.image.get_rect()
        
        self.rect.center = (random.randrange(30,WIDTH - 30), random.randrange(30, HEIGHT - 30))
