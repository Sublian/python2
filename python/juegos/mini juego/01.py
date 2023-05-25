import time
import pygame
import sys
import os

#obtener directorio
dir=os.path.dirname(__file__)

#definiendo tamaño
ancho=640
alto=480
color_azul=(0, 71, 100) #color azul para fondo
color_blanco=(255,255,255) #color blanco
pygame.init()
     

class Ladrillo(pygame.sprite.Sprite):
    def __init__(self, posicion):
        pygame.sprite.Sprite.__init__(self)
        #cargar imagen
        self.image=pygame.image.load(dir+"/imagen/ladrillo.png")
        #obtener rectangulo
        self.rect=self.image.get_rect()
        #posicion inicial
        self.rect.topleft=posicion

class Muro(pygame.sprite.Group):
    def __init__(self, cantidad_ladrillos):
        pygame.sprite.Group.__init__(self)
        pos_x=0
        pos_y=20
        for i in range(cantidad_ladrillos):
            ladrillo=Ladrillo((pos_x, pos_y))
            self.add(ladrillo)
            pos_x +=ladrillo.rect.width
            if pos_x>ancho:
                pos_x=0
                pos_y+=ladrillo.rect.height
                

class Paleta(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        #cargar imagen
        self.image=pygame.image.load(dir+"/imagen/paleta.png")
        #obtener rectangulo
        self.rect=self.image.get_rect()
        #posicion inicial centrada en pantalla en X
        self.rect.midbottom =(ancho/2,alto-20)    
        #establecer velocidad inicial
        self.speed=[0,0]

    def update(self, evento):
        #buscar si se presiona flecha izquierda
        if evento.key== pygame.K_LEFT and self.rect.left>0:
            self.speed=[-5,0]
        elif evento.key== pygame.K_RIGHT and self.rect.right<ancho:
            self.speed=[5,0]
        else:
            self.speed=[0,0]    
        #mover en base a posicion actual y velocidad
        self.rect.move_ip(self.speed) 
           

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


def juego_terminado():    
    fuente = pygame.font.SysFont("arial", 72)
    texto = fuente.render("Juego Terminado!", True, color_blanco)
    texto_rect = texto.get_rect()
    texto_rect.center = [ancho/2,alto/2]
    pantalla.blit(texto, texto_rect)
    pygame.display.flip()
    #pausa por 3 segundos
    time.sleep(3)
    #salida
    sys.exit()
    
def mostrar_puntuacion():    
    fuente = pygame.font.SysFont("consolas", 20)
    texto = fuente.render(str(puntuacion).zfill(5), True, color_blanco)
    texto_rect = texto.get_rect()
    texto_rect.topleft=[0,0]
    pantalla.blit(texto, texto_rect)
    
def mostrar_vidas():
    fuente = pygame.font.SysFont("consolas", 20)
    cadena = "Vidas: "+ str(vidas).zfill(2)
    texto = fuente.render(cadena, True, color_blanco)
    texto_rect = texto.get_rect()
    texto_rect.topright = [ancho,0]
    pantalla.blit(texto, texto_rect)
           
#iniciando pantalla
pantalla=pygame.display.set_mode((ancho,alto))

#configurar titulo de pantalla
pygame.display.set_caption("Juego de ladrillos")

#crear reloj
reloj=pygame.time.Clock()
#ajustar repeticion  de vento de tecla presionada
pygame.key.set_repeat(30)
bolita=Bolita()
jugador=Paleta()
muro= Muro(50)
puntuacion = 0
vidas = 3
esperando= True

while True:
    #establecer fps
    reloj.tick(60)
    #revisar eventos
    for evento in pygame.event.get():
        #si se presiona la "X" se sale del juego
        if evento.type==pygame.QUIT:
            sys.exit()
        #buscar eventos por teclado            
        elif evento.type==pygame.KEYDOWN:
            jugador.update(evento)
            if esperando==True and evento.key==pygame.K_SPACE:
                esperando=False
                if bolita.rect.centerx < ancho/2:
                    bolita.speed=[3,-3]
                else:
                    bolita.speed=[-3,-3]
            
    #actualizar posicion bolita 
    if esperando==False:
        bolita.update()
    else:
        bolita.rect.midbottom = jugador.rect.midtop
    
    #colision bolita - jugador
    if pygame.sprite.collide_rect(bolita, jugador):
        bolita.speed[1]=-bolita.speed[1]
    
    #colision bolita - ladrillo
    lista=pygame.sprite.spritecollide(bolita, muro, False)
    if lista:
        ladrillo=lista[0]
        cx = bolita.rect.centerx
        if cx < ladrillo.rect.left or cx > ladrillo.rect.right:
            bolita.speed[0]= -bolita.speed[0]
        else:
            bolita.speed[1]= -bolita.speed[1]
        muro.remove(ladrillo)    
        puntuacion+=10        
    
    if bolita.rect.bottom > alto:
        vidas-=1
        esperando=True        
      
    #rellenar pantalla
    pantalla.fill(color_azul)
    #mostrar puntuacion
    mostrar_puntuacion()
    #mostrar vidas
    mostrar_vidas()
    # dibujar bolita
    pantalla.blit(bolita.image, bolita.rect)
    # dibujar jugador
    pantalla.blit(jugador.image, jugador.rect)
    # dibujar ladrillos
    muro.draw(pantalla)
    pygame.display.flip()
    
    if vidas<=0:        
        juego_terminado()
    