import pygame
from random import randint
import time
from wallsMod import *
from wallsMod1 import *
from personaggioMod import *
from graficaEFotoMod import *
from mobMod import *
from fungoMod import *

pygame.mixer.music.load('music\sottofondo.wav')      
            
class Gioco:

    def __init__(self):

        pygame.init()
        pygame.mixer.init()
        self.running =  True
        self.game_over = False
        self.fattoPunto = 0
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Phyton Ideas")
        pygame.display.set_icon(icona)
        self.clock = pygame.time.Clock()
        self.i = 0
        self.conteggio = 0
        self.col = False
        

    def definisciBordi(self):

        for count in range(1, 20):
            
            self.murosoprasotto = muroLungo(self.i, 0, 20, 600)
            self.murodestrasinistra = muroAlto(- 6, self.i, 130, 20)
            self.all_walls.add(self.murosoprasotto)
            self.all_walls.add(self.murodestrasinistra)
            self.all_walls.update()
            self.i += 40
            self.conteggio += 1

        self.i = 0
        
        for count in range(1,20):

            self.murosoprasotto = muroLungo(self.i, (HEIGHT - 30), 20, 600)
            self.walls_bot.add(self.murosoprasotto)
            self.murodestrasinistra = muroAlto((WIDTH - 4), self.i, 130, 20)
            self.all_walls.add(self.murodestrasinistra)
            self.all_walls.update()
            self.walls_bot.update()
            self.i += 40
        
    def nuovo(self):
        # Inizia nuovo gioco
        pygame.mixer.music.play(-1) 
        self.all_sprites = pygame.sprite.Group()
        self.all_nemici = pygame.sprite.Group()
        self.all_walls = pygame.sprite.Group()
        self.walls_bot = pygame.sprite.Group()
        self.collezionabili = pygame.sprite.Group()
        self.giocatore = Player()
        self.nemico = Mob()
        self.funghi = Fungo()
        self.lanciato()

    def lanciato(self):
        # Game Loop
        self.giocando = True

        while self.giocando:
                self.clock.tick(FPS)
                self.update()
                self.azioni()
                self.disegna()

                if self.game_over:
                        self.show_go_screen()
                        game_over = False
                        

    def update(self):

        if self.conteggio == 0:
            self.definisciBordi()
        self.all_sprites.add(self.giocatore)
        self.all_nemici.add(self.nemico)
        self.collezionabili.add(self.funghi)
        self.all_sprites.update()
        self.all_nemici.update()
        self.collezionabili.update()

    def punteggio(self, fattoPunto):

        self.draw_text(" Punteggio:" + str(self.fattoPunto), 15, NERO, 45, 10)

    
    def azioni(self):
        
        for event in pygame.event.get():
    #   Controllo se si vuole chiudere la finestra
           if event.type == pygame.QUIT:
            if  self.giocando:
                    self.giocando = False


        self.collisione = pygame.sprite.spritecollide(self.giocatore, self.collezionabili, True, pygame.sprite.collide_mask)

        if self.collisione:

            random.choice(morso).play()
            self.funghi.rect.x = randint(2, 10) * 44
            self.funghi.rect.y = randint(2, 10) * 44

            self.fattoPunto += 10
            
            self.collezionabili.update() 

    def disegna(self):

        self.giocatore.movimento()
        self.muoviNemico()
        self.screen.fill(NERO)
        self.screen.blit(pygame.transform.scale(bg, (WIDTH, HEIGHT)) , (0, 0))
        self.all_walls.draw(self.screen)
        self.collezionabili.draw(self.screen)
        self.all_nemici.draw(self.screen)
        self.all_sprites.draw(self.screen)
        self.punteggio(self.fattoPunto)
        self.walls_bot.draw(self.screen)
        pygame.display.flip()

    def muoviNemico(self):

        if self.nemico.pos.x > self.giocatore.pos.x:

            self.nemico.pos.x -= 2
            self.nemico.velocita.x -= 2

        elif self.nemico.pos.x < self.giocatore.pos.x:

            self.nemico.pos.x += 2
            self.nemico.velocita.x += 2

        if self.nemico.pos.y > self.giocatore.pos.y:

            self.nemico.pos.y -= 2
            self.nemico.velocita.y -= 2

        elif self.nemico.pos.y < self.giocatore.pos.y:

            self.nemico.pos.y += 2
            self.nemico.velocita.y += 2


        self.nemico.rect.center = self.nemico.pos
        
        self.nemico.animazione()
        self.nemico.velocita.x = 0
        self.nemico.velocita.y = 0

        self.collisione1 = pygame.sprite.spritecollide(self.giocatore, self.all_nemici, False, pygame.sprite.collide_mask)

        if self.collisione1:

            pygame.mixer.music.stop()
            perso.play()
            time.sleep(2)
            sconfitta_Sound.play()

            self.show_go_screen()
            self.conteggio = 0
            self.fattoPunto = 0
            self.i = 0
            self.nuovo()
            self.game_over = True


    def draw_text(self, text, size, color, x, y):

        font = pygame.font.Font("C:\Windows\Fonts\Arial.ttf", size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x, y)
        self.screen.blit(text_surface, text_rect)
        
    def show_start_screen(self):

        self.screen.fill(NERO)
        self.draw_text(" T_Fox", 48, BIANCO, WIDTH / 2, HEIGHT / 4)
        self.draw_text("Frecce direzionali per muoversi", 22, BIANCO, WIDTH / 2, HEIGHT /2)
        self.draw_text("Premi un tasto per iniziare", 22, BIANCO, WIDTH / 2, HEIGHT *3 / 4)
        pygame.display.flip()
        self.aspetta_pressione()
                    
    def show_go_screen(self):
        aspettando1 = True
        if not self.running:
            return
        self.screen.fill(NERO)
        self.screen.blit(facciaNemico, [10, HEIGHT / 2 - 50])
        self.screen.blit(tomba, [WIDTH / 2 + 50, HEIGHT / 2 - 100])
        self.draw_text(" HAI PERSO!", 48, ROSSO, WIDTH / 2, HEIGHT / 4)
        self.draw_text("Punteggio: " + str(self.fattoPunto), 22, BIANCO, WIDTH / 2, HEIGHT /2)
        self.draw_text("Premi un tasto per ricominciare", 22, BIANCO, WIDTH /2, HEIGHT * 3 /4)
        pygame.display.flip()
        while aspettando1:
            for event in pygame.event.get():
                if event.type == pygame.KEYUP:
                    self.aspetta_pressione()
                    aspettando1 = False

    def aspetta_pressione(self):

        aspettando = True
        while aspettando:
                self.clock.tick(FPS)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.running = False
                        aspettando = False
                    if event.type == pygame.KEYUP:
                       aspettando = False     

                    
g = Gioco()
g.show_start_screen()
while g.running:
    g.nuovo()
    g.show_go_screen()

pygame.quit()
