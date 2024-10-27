import pygame

WIDTH = 750
HEIGHT = 600
FPS = 30
pygame.init()
pygame.mixer.init()
# Definisci colori
BIANCO = (255, 255, 255)
NERO = (0, 0, 0)
ROSSO = (255, 0, 0)
VERDE = (0, 255, 0)
BLU = (0, 0, 255)

smallfont = pygame.font.SysFont("comcsansms", 25)
medfont = pygame.font.SysFont("comcsansms", 50)
largefont = pygame.font.SysFont("comcsansms", 80)

morso = []
for snd in ['music/morso1.wav', 'music/morso2.wav']:
    morso.append(pygame.mixer.Sound(snd))

facciaNemico = pygame.image.load('sprites/perso1.png')
tomba = pygame.image.load('sprites/perso.png')
perso = pygame.mixer.Sound('music/perso.wav')
sconfitta_Sound = pygame.mixer.Sound('music\sconfitta_Suono.wav')
bg = pygame.image.load('sprites/bg.png')
icona = pygame.image.load('sprites/ico.png')
sconfitta = pygame.image.load('sprites\perso.png')
sconfitta1 = pygame.image.load('sprites\perso1.png')
bordoss =   pygame.image.load('sprites\staccionataupdown.png')
bordods = pygame.image.load('sprites\staccionatasxdx.png')




