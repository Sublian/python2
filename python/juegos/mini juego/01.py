import pygame
import sys
import os

#obtener directorio
dir=os.path.dirname(__file__)

#definiendo tamaño
ancho=640
alto=480
color_azul=(0,0,64) #color azul para fondo


class Paleta(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        #cargar imagen
        self.image=pygame.image.load(dir+"/imagen/paleta.png")
        #obtener rectangulo
        self.rect=self.image.get_rect()
        #posicion inicial centrada en pantalla en X
        self.rect.midbottom =(ancho/2,ancho-80)
    
        #establecer velocidad inicial
        self.speed=[0,0]

class Bolita(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        #cargar imagen
        self.image=pygame.image.load(dir+"/imagen/bolita.png")
        #obtener rectangulo
        self.rect=self.image.get_rect()
        #posicion inicial
        self.rect.centerx =ancho/2
        self.rect.centery =alto/2
        #establecer velocidad inicial
        self.speed=[3,3]
        
    def update(self):
        #evitar que se salga por debajo
        if self.rect.bottom >= alto or self.rect.top <= 0:
            self.speed[1] = -self.speed[1]
        #evitar que se salga por debajo
        if self.rect.right >= ancho or self.rect.left <= 0:
            self.speed[0] = -self.speed[0]
        
        #mover en base a posicion actual y velocidad
        self.rect.move_ip(self.speed)
             
        
#iniciando pantalla
pantalla=pygame.display.set_mode((ancho,alto))

#configurar titulo de pantalla
pygame.display.set_caption("Juego de ladrillos")

#crear reloj
reloj=pygame.time.Clock()
bolita=Bolita()
jugador=Paleta()

while True:
    #establecer fps
    reloj.tick(60)
    #revisar eventos
    for evento in pygame.event.get():
        if evento.type==pygame.QUIT:
            sys.exit()
            
    #actualizar posicion bolita 
    bolita.update()
    
    #rellenar pantalla
    pantalla.fill(color_azul)
    # dibujar bolita
    pantalla.blit(bolita.image, bolita.rect)
    pantalla.blit(jugador.image, jugador.rect)
    pygame.display.flip()