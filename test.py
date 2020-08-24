import pygame,sys
from pygame.locals import *
import random

#Inicializamos pygame
pygame.init()

ventana = pygame.display.set_mode((400,300))
pygame.display.set_caption("Eric se la come doblada")
pygame.draw.circle(ventana,(8,70,120),(80,90),20)
pygame.draw.rect(ventana,(130,70,70),(0,70,100,50))

running=True
while running:
    for event in pygame.event.get():    #Cuando ocurre un evento...
        if event.type == pygame.QUIT:   #Si el evento es cerrar la ventana
            pygame.quit()               #Se cierra pygame
            sys.exit()                  #Se cierra el programa
    pygame.display.update()
    pygame.mouse.get_pos()
    print(random.randrange(0,600))
ventana.fill(green)
