import pygame
from pygame.locals import *
from .Bala import *


class Nave(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Sprites/rikimartin_por_arriba.png")
        self.rect = self.image.get_rect()
        self.vel=4
        self.rect.y = 500
        self.rect.x = 300
        self.vida = 150
        self.vivo=True
        self.ListaDisparo=[]

    def dibujar(self,superficie):
        superficie.blit(self.image,self.rect)   #Dibujamos la nave.

    def disparo(self):
        pygame.mixer.init()
        bala=Bala(self.rect.x+13,self.rect.y+5)   #Instanciamos las bala sobre la nave
        self.ListaDisparo.append(bala)
        #SonidoDisparo=pygame.mixer.Sound("Sonidos/disparo1.waw")
        #pygame.mixer.Sound.play(SonidoDisparo)

    def update(self,ventana):

        keys = pygame.key.get_pressed()     #Obtenemos el mapping de teclas presionadas
        if keys [K_LCTRL]:
            self.vel=8
        else:
            self.vel=4
        if keys[K_s] and self.rect.y<535:      #Movimiento y Colisión con Y
            self.rect.y+=self.vel
            self.image=pygame.image.load("Sprites/rikimartin_por_arriba.png")
        if keys[K_w] and self.rect.y>2:
            self.rect.y-=self.vel
            self.image=pygame.image.load("Sprites/rikimartin_por_arriba.png")
        if keys[K_a] and self.rect.x>2:        #Movimiento y Colisión con X
            self.rect.x-=self.vel
            self.image=pygame.image.load("Sprites/rikimartin_izquierda.png")
        if keys[K_d] and self.rect.x<535:
            self.rect.x+=self.vel
            self.image=pygame.image.load("Sprites/rikimartin_derecha.png")
        if len(self.ListaDisparo)>0:
            for b in self.ListaDisparo:
                b.update(ventana)
                if(b.rect.y<=0):             #Si la Y supera el valor se remueve la bala de la lista
                    self.ListaDisparo.remove(b)

    def restart(self):                         #Restartear el juego
        keys = pygame.key.get_pressed()
        if keys[K_RETURN]:
            self.vida=150
            self.vivo=True
            self.rect.y = 500
            self.rect.x = 260
            self.image=pygame.image.load("Sprites/rikimartin_por_arriba.png")

    def delete_bullets(self):
        if (len(self.ListaDisparo)>0):
            for i in self.ListaDisparo:
                self.ListaDisparo.remove(i)
