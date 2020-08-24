import pygame
from pygame.locals import *

class Bala(pygame.sprite.Sprite):
    def __init__(self,x,y):  #Constructor de la clase bala
        pygame.sprite.Sprite.__init__(self) #Super/Constructor de la clase Sprite
        self.image=pygame.image.load("Sprites/bala.png")
        self.rect=self.image.get_rect()
        self.velocidad=10
        self.rect.x=x
        self.rect.y=y

    def trayectoria(self):
        self.rect.y = self.rect.y - self.velocidad  

    def trayectoriaE(self):
        self.rect.y = self.rect.y + self.velocidad  #Tractero para el enemigo porque sino se van las balas para abajo

    def update(self,ventana):
        self.trayectoria()                         #Aparece y se va para arriba
        ventana.blit(self.image,self.rect)
              #Dibujar bala
    def updateE(self,ventana):
        self.trayectoriaE()                        # Lo mismo pero con la trayectoria Enemigo
        ventana.blit(self.image,self.rect)
