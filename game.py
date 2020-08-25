import pygame
import sys
from Clases.Nave import *
from Clases.Bala import *
from Clases.NaveEnemiga import *
from pygame.locals import *

def animacion(carpeta,nombre,total,formato):  #Best algoritmo ever
    vector=[]
    n1=carpeta+"/"+nombre + " "
    for i in range(1,total):
        n1=n1+"("+ str(i) + ")."+formato
        vector.append(pygame.image.load(n1))
        n1=carpeta+"/"+nombre + " "
    return vector


pygame.display.set_icon(pygame.image.load("icono.png"))
#Animación del fondo

fondos=animacion("FondoJuego","fondog",39,"png")
#Inicializamos pygame

pygame.mixer.init()
pygame.init()


#Tamaño de la ventana
ventana = pygame.display.set_mode((800,600))
#Violeta
Color=pygame.Color(91,20,176)
#Nombre de la ventana
recX=100
recY=50
#Rectangulo=pygame.Rect(0,0,recX,recY)
score=0
pygame.display.set_caption("Eric se la come doblada")

# Fuente del juego
fuente_sistema=pygame.font.SysFont("calibri",30)
#Creación de un texto
texto_muerte=fuente_sistema.render("Game Over | Press Enter to restart",0,(0,0,0),(255,0,0)) # Texto, 0 , Color, fondo //  llamarlo ventana.blit(texto,(300,300))
#Clock para los FPS
clock=pygame.time.Clock()
 #Instancia de la clase Nave
n1=Nave()
ListaEnemigos=[]
#Para iniciar el juego
running=True
#Bucle juego
sprite=0 #Para el fondo
pygame.mixer.music.load("Sonidos/musicaFondo.wav")
pygame.mixer.music.play()


cont=0
while running:                          #Ejecución permanente
    #print(pygame.mouse.get_pos())
    clock.tick(30)                                   #Limitar fps
    tiempo_juego=(int)(pygame.time.get_ticks()/1000) #Obtener segundos de juego
    score+=1
    #print(score)
    ventana.fill((255,255,255))         #Actualizo ventana a Blanco para que el sprite no se repita
    ventana.blit(fondos[sprite],(0,0))
    if(sprite==len(fondos)-1):
        sprite=0
    else:
        sprite+=1
    #pygame.draw.rect(ventana,(0,0,0),Rectangulo)
    #Rectangulo.left,Rectangulo.top=pygame.mouse.get_pos() #Capturar posición del mouse y colocarlo
    #Rectangulo.x=Rectangulo.x-50  #Centrado rectangulo
    #Rectangulo.y=Rectangulo.y-25

    for event in pygame.event.get():    #Cuando ocurre un evento...
        if event.type == pygame.QUIT:   #Si el evento es cerrar la ventana
            pygame.quit()               #Se cierra pygame
            sys.exit()                  #Se cierra el programa
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_SPACE:
                n1.disparo()            #Verificamos si el evento es = pygame.KEYDOWN para que se ejecute una sola vez
                n1.image=pygame.image.load("Sprites/rikimartin_por_arriba.png")
    #HUD de la derecha con VIDA
    pygame.draw.rect(ventana,Color,(600,0,200,600))            #Lugar donde se dibuja, color, coord, ancho, largo
    pygame.draw.rect(ventana,(0,0,0),(625,500,150,40))         #Vida
    pygame.draw.rect(ventana,(0,0,0),(625,465,150,20))
    pygame.draw.rect(ventana,(208,233,29),(625,465,150,20))    #Habilidad especial
    pygame.draw.rect(ventana,(255,0,0),(625,500,n1.vida,40))
    #if (Rectangulo.colliderect(n1.rect)and n1.vida>0):         #Función de colisión entre rectangulos
    #    n1.vida-=5
    if (n1.vida<=0):
        n1.vivo=False
        pygame.draw.rect(ventana,(0,0,0),(625,500,n1.vida,40))  #Negrada para sacar la linea roja
        ventana.blit(texto_muerte,(150,300))
        n1.delete_bullets()                                     #Borra todas las balas que haya en pantalla (En el objeto Nave)
        for i in ListaEnemigos:
            ListaEnemigos.remove(i)
        score=0
        n1.restart()
    if (n1.vivo):                                               #Verificar si la nave está viva
        n1.dibujar(ventana)
        n1.update(ventana)
        if (len(ListaEnemigos)<3):                             #Agregar enemigos a la pantalla siempre y cuando sea "< a"
            aux=NaveEnemiga()
            ListaEnemigos.append(aux)
        for i in ListaEnemigos:                                 #Dibujar los enemigos
            i.dibujar(ventana)
            if (i.rect.y>600):
                ListaEnemigos.remove(i)
        for i in ListaEnemigos:                                              #Verificar las colisiones de las balas con la nave y viceversa
            for j in i.ListaDisparo:
                if (j.rect.colliderect(n1.rect)):
                    i.ListaDisparo.remove(j)
                    #n1.vida-=30
                if (len(i.ListaDisparo)>0):                                      #Verificar que la lista tenga algo para que no se vaya de rango el If siguiente
                    if(i.ListaDisparo[len(i.ListaDisparo)-1]==j):                #Si el ListaDisparo del enemigo en I en la última posición (-1)
                        if (j.rect.y>=560):
                            ListaEnemigos.remove(i)
        for i in ListaEnemigos:                                              #Si una bala enemiga golpea la nave enemiga, quitarle vida.
            for j in n1.ListaDisparo:
                if (j.rect.colliderect(i)):
                    i.vida-=50
                    #verificarMuerte(ListaEnemigos)
                    if (i.vida>0):
                         n1.ListaDisparo.remove(j)
    segundos=fuente_sistema.render(("Seconds "+(str)(tiempo_juego)),0,(255,255,255)) #Creo los segundos para mostrarlos
    ventana.blit(segundos,(20,20))                                                    #Muestro los segundos
    pygame.display.update()                    #Actualiza la ventana
