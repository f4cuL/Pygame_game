import pygame
from pygame.locals import *
from .Bala import *
from .Nave import *

import random

class NaveEnemiga(Nave):
    def __init__(self):
        Nave.__init__(self)
        self.image = pygame.image.load("Sprites/enemigo.png")
        self.rect = self.image.get_rect()
        self.vel=10
        self.rect.y = random.randrange(-100,0)
        self.rect.x = random.randrange(0,600)
        self.contador=0
        self.izquierda=True
        self.vida=100

    def dibujar(self,ventana):
        if (self.vida>0):
            ventana.blit(self.image,self.rect)   #Dibujamos la nave.
        self.aparecer(ventana)

    def disparo(self):
        bala=Bala(self.rect.x+30,self.rect.y+50)
        self.ListaDisparo.append(bala)

    def aparecer(self,ventana):
        if (self.rect.y<=20):
            self.rect.y=self.rect.y+3
        if (self.rect.y>=20):
            self.update(ventana)

    def update(self,ventana):
        if (self.contador<1):
            if (random.randrange(0,2)):   #Numero random para determinar para que lado sale la nave
                self.izquierda=True
            else:
                self.izquierda=False
        self.contador=1                   #Contador para que se haga una vez
        if (self.izquierda==True):
            self.rect.x=self.rect.x-self.vel
        elif(self.izquierda==False):
            self.rect.x=self.rect.x+self.vel
        if (self.rect.x>=540):
            self.izquierda=True
        if (self.rect.x<=0):
            self.izquierda=False
        self.rect.y=self.rect.y+1
        if ((self.rect.x%9)==0 and self.vida>0):
            self.disparo()
        if (len(self.ListaDisparo)>0):
            for i in self.ListaDisparo:
                i.updateE(ventana)
                if (i.rect.y>=600):
                    self.ListaDisparo.remove(i)
