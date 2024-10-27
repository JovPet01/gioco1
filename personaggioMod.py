import pygame
from graficaEFotoMod import *
vec = pygame.math.Vector2

class Player(pygame.sprite.Sprite):

                    #sprite del giocatore
    def __init__(self):

        pygame.sprite.Sprite.__init__(self)
        self.caricamento_immagini()
        self.image = self.frames_fermo
        self.rect =  self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT  / 2)
        self.pos = vec(WIDTH / 2, HEIGHT  / 2)
        self.camminando = False
        self.frame_corrente = 0
        self.ultimo_cambiamento = 0
        self.velocita = vec(0, 0)
        
    def movimento(self):

        key = pygame.key.get_pressed()

        if key[pygame.K_DOWN]: 

            self.pos.y += 5
            self.velocita.y = 5

        elif key[pygame.K_UP]:

            self.pos.y -= 5
            self.velocita.y = -5

        if key[pygame.K_RIGHT]:

            self.pos.x += 5
            self.velocita.x = 5

        elif key[pygame.K_LEFT]: 

            self.pos.x -= 5
            self.velocita.x = -5

        if self.rect.right >= WIDTH:

            self.pos.x = WIDTH - 26

        elif self.rect.left <= 0:

            self.pos.x = 26

        if self.rect.bottom >= HEIGHT:
            
            self.pos.y = HEIGHT - 50

        elif self.rect.top <= 10:

            self.pos.y = 50
        
        self.rect.center = self.pos
        
        self.animazione()
        self.velocita.x = 0
        self.velocita.y = 0
    
    def caricamento_immagini(self):

        self.frames_fermo  = pygame.image.load('sprites/idle.png')
        self.frames_camminando_d = [pygame.image.load('sprites/destra1.png'), pygame.image.load('sprites/destra2.png'), pygame.image.load('sprites/destra3.png'), pygame.image.load('sprites/destra4.png')]
        self.frames_camminando_s =[]
        for frame in self.frames_camminando_d :
            self.frames_camminando_s.append(pygame.transform.flip(frame, True, False))
        self.frames_camminando_up=[pygame.image.load('sprites/sopra1.png'), pygame.image.load('sprites/sopra2.png'), pygame.image.load('sprites/sopra3.png'), pygame.image.load('sprites/sopra4.png')]
        self.frames_camminando_down = [pygame.image.load('sprites/sotto1.png'), pygame.image.load('sprites/sotto2.png'), pygame.image.load('sprites/sotto3.png'), pygame.image.load('sprites/sotto4.png')]

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
                    sotto = self.rect.bottom
                    
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
