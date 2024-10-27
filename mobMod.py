import pygame
import random
import time
from graficaEFotoMod import WIDTH, HEIGHT, NERO
vec = pygame.math.Vector2

class Mob(pygame.sprite.Sprite):

    def __init__(self):

        pygame.sprite.Sprite.__init__(self)
        self.caricamento_immagini()
        self.camminando = False
        self.image = self.frames_fermo
        self.frame_corrente = 0
        self.ultimo_cambiamento = 0
        self.rect =  self.image.get_rect()
        self.rect.center = ((random.randrange(WIDTH - self.rect.width) / 2), (random.randrange(10, 40) / 2) ) 
        self.pos = vec((random.randrange(WIDTH - self.rect.width) / 2), (random.randrange(10, 40) / 2))
        self.velocita = vec(0, 0)
         
    def caricamento_immagini(self):

        self.frames_fermo  = pygame.image.load('sprites/idle1.png')
        self.frames_camminando_d = [pygame.image.load('sprites/n_Destra1.png'), pygame.image.load('sprites/n_Destra2.png'), pygame.image.load('sprites/n_Destra3.png'), pygame.image.load('sprites/n_Destra4.png')]
        self.frames_camminando_s =[]
        for frame in self.frames_camminando_d :
            self.frames_camminando_s.append(pygame.transform.flip(frame, True, False))
        self.frames_camminando_up=[pygame.image.load('sprites/n_Sopra1.png'), pygame.image.load('sprites/n_Sopra2.png'), pygame.image.load('sprites/n_Sopra3.png'), pygame.image.load('sprites/n_Sopra4.png')]
        self.frames_camminando_down = [pygame.image.load('sprites/n_Sotto1.png'), pygame.image.load('sprites/n_Sotto2.png'), pygame.image.load('sprites/n_Sotto3.png'), pygame.image.load('sprites/n_Sotto4.png')]

    def animazione(self):

        ora = pygame.time.get_ticks()

        if self.velocita.x != 0 or self.velocita.y != 0:

            self.camminando = True

        else:

            self.camminando = False

        if self.camminando:

            if ora - self.ultimo_cambiamento > 200:
                    self.ultimo_cambiamento = ora
                    self.frame_corrente = (self.frame_corrente + 1) % len(self.frames_camminando_s)
                    n_Sotto = self.rect.bottom
                    if self.velocita.x > 0:
                        self.image = self.frames_camminando_d[self.frame_corrente]
                    elif self.velocita.x < 0:
                        self.image = self.frames_camminando_s[self.frame_corrente]
                    elif self.velocita.y < 0:
                        self.image = self.frames_camminando_up[self.frame_corrente]
                    elif self.velocita.y > 0:
                        self.image = self.frames_camminando_down[self.frame_corrente]

        if not self.camminando:
            if ora - self.ultimo_cambiamento > 200:
                self.ultimo_cambiamento = ora
                self.image = self.frames_fermo

        self.mask = pygame.mask.from_surface(self.image)
