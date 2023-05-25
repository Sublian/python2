import sys    # para usar exit()
import time   # para usar sleep()
import pygame
import os

#obtener directorio
dir=os.path.dirname(__file__)

ANCHO = 640 # Ancho de la pantalla.
ALTO = 480  # Alto de la pantalla.
color_azul=(0, 71, 100) #color azul para fondo
color_blanco = (255, 255, 255) # Color blanco, para textos.


class Escena:
    "Esqueleto para cada una de las escenas del videojuego."
    def __init__(self):
        self.proximaEscena = False
        self.jugando = True

    def leer_eventos(self, eventos):
        "Lee los eventos para interactuar con los objetos."
        pass

    def actualizar(self):
        "Actualiza los objetos en la pantalla."
        pass

    def dibujar(self, pantalla):
        "Dibuja los objetos en la pantalla."
        pass

    def cambiar_escena(self, escena):
        "Cambia la escena del juego."
        self.proximaEscena = escena

class Director:
    def __init__(self, titulo = "", res = (ANCHO, ALTO)):
        pygame.init()
        # Inicializando pantalla.
        self.pantalla = pygame.display.set_mode(res)
        # Configurar título de pantalla.
        pygame.display.set_caption(titulo)
        # Crear el reloj.
        self.reloj = pygame.time.Clock()
        self.escena = None
        self.escenas = {}

    def ejecutar(self, escena_inicial, fps = 60):
        self.escena = self.escenas[escena_inicial]
        jugando = True
        while jugando:
            self.reloj.tick(fps)
            eventos = pygame.event.get()
            # Revisar todos los eventos.
            for evento in eventos:
                # Si se presiona la tachita de la barra de título,
                if evento.type == pygame.QUIT:
                    # cerrar el videojuego.
                    jugando = False

            self.escena.leer_eventos(eventos)
            self.escena.actualizar()
            self.escena.dibujar(self.pantalla)

            self.elegirEscena(self.escena.proximaEscena)

            if jugando:
                jugando = self.escena.jugando

            pygame.display.flip()

        time.sleep(3)

    def elegirEscena(self, proximaEscena):
        if proximaEscena:
            if proximaEscena not in self.escenas:
                self.agregarEscena(proximaEscena)
            self.escena = self.escenas[proximaEscena]

    def agregarEscena(self, escena):
        escenaClase = 'Escena'+escena
        escenaObj = globals()[escenaClase]
        self.escenas[escena] = escenaObj();


class EscenaNivel1(Escena):
    def __init__(self):
        Escena.__init__(self)

        self.bolita = Bolita()
        self.jugador = Paleta()
        self.muro = Muro(48)

        self.puntuacion = 0
        self.vidas = 3
        self.esperando_saque = True

        # Ajustar repetición de evento de tecla presionada.
        pygame.key.set_repeat(30)

    def leer_eventos(self, eventos):
        for evento in eventos:
            if evento.type == pygame.KEYDOWN:
                self.jugador.update(evento)
                if self.esperando_saque == True and evento.key == pygame.K_SPACE:
                    self.esperando_saque = False
                    if self.bolita.rect.centerx < ANCHO / 2:
                        self.bolita.speed = [3, -3]
                    else:
                        self.bolita.speed = [-3, -3]

    def actualizar(self):
        # Actualizar posición de la bolita.
        if self.esperando_saque == False:
            self.bolita.update()
        else:
            self.bolita.rect.midbottom = self.jugador.rect.midtop

        # Colisión entre bolita y jugador.
        if pygame.sprite.collide_rect(self.bolita, self.jugador):
            self.bolita.speed[1] = -self.bolita.speed[1]

        # Colisión de la bolita con el muro.
        lista = pygame.sprite.spritecollide(self.bolita, self.muro, False)
        if lista:
            ladrillo = lista[0]
            cx = self.bolita.rect.centerx
            if cx < ladrillo.rect.left or cx > ladrillo.rect.right:
                self.bolita.speed[0] = -self.bolita.speed[0]
            else:
                self.bolita.speed[1] = -self.bolita.speed[1]
            self.muro.remove(ladrillo)
            self.puntuacion += 10

        # Revisar si bolita sale de la pantalla.
        if self.bolita.rect.top > ALTO:
            self.vidas -= 1
            self.esperando_saque = True

        if self.vidas <= 0:
            self.cambiar_escena('JuegoTerminado')

    def dibujar(self, pantalla):
        # Rellenar la pantalla.
        pantalla.fill(color_azul)
        # Mostrar puntuación
        self.mostrar_puntuacion(pantalla)
        # Mostrar vidas.
        self.mostrar_vidas(pantalla)
        # Dibujar bolita en pantalla.
        pantalla.blit(self.bolita.image, self.bolita.rect)
        # Dibujar jugador en pantalla.
        pantalla.blit(self.jugador.image, self.jugador.rect)
        # Dibujar los ladrillos.
        self.muro.draw(pantalla)

    def mostrar_puntuacion(self, pantalla):
        fuente = pygame.font.SysFont('Consolas', 20)
        texto = fuente.render(str(self.puntuacion).zfill(5), True, color_blanco)
        texto_rect = texto.get_rect()
        texto_rect.topleft = [0, 0]
        pantalla.blit(texto, texto_rect)

    def mostrar_vidas(self, pantalla):
        fuente = pygame.font.SysFont('Consolas', 20)
        cadena = "Vidas: " + str(self.vidas).zfill(2)
        texto = fuente.render(cadena, True, color_blanco)
        texto_rect = texto.get_rect()
        texto_rect.topright = [ANCHO, 0]
        pantalla.blit(texto, texto_rect)

class EscenaJuegoTerminado(Escena):
    def actualizar(self):
        self.jugando = False

    def dibujar(self, pantalla):
        fuente = pygame.font.SysFont('Arial', 72)
        texto = fuente.render('Juego terminado', True, color_blanco)
        texto_rect = texto.get_rect()
        texto_rect.center = [ANCHO / 2, ALTO / 2]
        pantalla.blit(texto, texto_rect)


class Bolita(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        # Cargar imagen
        self.image = pygame.image.load(dir+'/imagen/bolita.png')
        # Obtener rectángulo de la imagen
        self.rect = self.image.get_rect()
        # Posición inicial centrada en pantalla.
        self.rect.centerx = ANCHO / 2
        self.rect.centery = ALTO / 2
        # Establecer velocidad inicial.
        self.speed = [3, 3]

    def update(self):
        # Evitar que salga por debajo.
        if self.rect.top <= 0:
            self.speed[1] = -self.speed[1]
        # Evitar que salga por la derecha.
        elif self.rect.right >= ANCHO or self.rect.left <= 0:
            self.speed[0] = -self.speed[0]
        # Mover en base a posición actual y velocidad.
        self.rect.move_ip(self.speed)

class Paleta(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        # Cargar imagen
        self.image = pygame.image.load(dir+'/imagen/paleta.png')
        # Obtener rectángulo de la imagen
        self.rect = self.image.get_rect()
        # Posición inicial centrada en pantalla en X.
        self.rect.midbottom = (ANCHO / 2, ALTO - 20)
        # Establecer velocidad inicial.
        self.speed = [0, 0]

    def update(self, evento):
        # Buscar si se presionó flecha izquierda.
        if evento.key == pygame.K_LEFT and self.rect.left > 0:
            self.speed = [-5, 0]
        # Si se presionó flecha derecha.
        elif evento.key == pygame.K_RIGHT and self.rect.right < ANCHO:
            self.speed = [5, 0]
        else:
            self.speed = [0, 0]
        # Mover en base a posición actual y velocidad.
        self.rect.move_ip(self.speed)

class Ladrillo(pygame.sprite.Sprite):
    def __init__(self, posicion):
        pygame.sprite.Sprite.__init__(self)
        # Cargar imagen
        self.image = pygame.image.load(dir+'/imagen/ladrillo.png')
        # Obtener rectángulo de la imagen
        self.rect = self.image.get_rect()
        # Posición inicial, provista externamente.
        self.rect.topleft = posicion

class Muro(pygame.sprite.Group):
    def __init__(self, cantidadLadrillos):
        pygame.sprite.Group.__init__(self)

        pos_x = 0
        pos_y = 20
        for i in range(cantidadLadrillos):
            ladrillo = Ladrillo((pos_x, pos_y))
            self.add(ladrillo)

            pos_x += ladrillo.rect.width
            if pos_x >= ANCHO:
                pos_x = 0
                pos_y += ladrillo.rect.height

director = Director('Juego de ladrillos', (ANCHO, ALTO))
director.agregarEscena('Nivel1')
director.ejecutar('Nivel1')