import pygame, random, sys
from pygame.locals import *
from constantes import *


class Jugador(pygame.sprite.Sprite):
    # Sprite del jugador
    def __init__(self):
        # Heredamos el init de la clase Sprite de Pygame
        super().__init__()

        # Cargamos un cuadrado como jugador
        # self.image = pygame.surface((200,200))

        # Rellenamos el cuadrado con un color
        # self.image.fill(ROJO)

        # Cargamos la imagen que representa al jugador
        self.image = pygame.image.load("imagenes/Punk_idle.png").convert()
        # Ponemos el fondo verde como transparente
        self.image.set_colorkey(VERDE)
        # Obtenemos el rectángulo de la imagen del jugador. Esto nos permitirá manipularlo.
        self.rect = self.image.get_rect()
        # centra el rectangulo (sprite)
        self.rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        # Inicializo la Velocidad del personaje
        self.velocidad_x = 0
        self.velocidad_y = 0

    def update(self):
        # Esto se ejecuta cada vuelta de bucle

        # Cargamos velocidad a 0  cuando no se pulsa nada
        self.velocidad_x = 0
        self.velocidad_y = 0

        # definimos las teclas (get_pressed permite dejar las teclas pulsadas)
        teclas = pygame.key.get_pressed()

        # Mueve el personaje hacia la izquierda
        if teclas[pygame.K_a]:
            self.velocidad_x = -10

        # Mueve el personaje hacia la derecha
        if teclas[pygame.K_d]:
            self.velocidad_x = 10

        if teclas[pygame.K_w]:
            self.velocidad_y = -10
        if teclas[pygame.K_s]:
            self.velocidad_y = 10

        # actualiza la posicion del personaje
        self.rect.x += self.velocidad_x
        self.rect.y += self.velocidad_y
        # Controlamos que el jugador no salga de pantalla
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.bottom > SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT
        if self.rect.top < 0:
            self.rect.top = 0


class Enemigos(pygame.sprite.Sprite):
    # Sprite del enemigos
    def __init__(self):
        # Heredamos el init de la clase Sprite de Pygame
        super().__init__()

        # Cargamos la imagen que representa al jugador
        self.image = pygame.image.load("imagenes/IndustrialTile_35.png").convert()
        # Ponemos el fondo verde como transparente
        #self.image.set_colorkey(VERDE)
        # Obtenemos el rectángulo de la imagen del jugador. Esto nos permitirá manipularlo.
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(SCREEN_WIDTH // 2)
        self.rect.y = random.randrange(SCREEN_HEIGHT // 2)
        #self.rect.x = random.randrange(SCREEN_WIDTH - self.rect.width)
        #self.rect.y = random.randrange(SCREEN_HEIGHT - self.rect.height)
        self.velocidad_x = random.randint(-5, 5)
        self.velocidad_y = random.randint(-5, 5)

    def update(self):
        # paramos las ejecuciones
        #self.velocidad_x = 0
        #self.velocidad_y = 0

        # definimos las teclas (get_pressed permite dejar las teclas pulsadas)
        teclas = pygame.key.get_pressed()

        # Mueve el enemigo
        if teclas[pygame.K_m]:
            self.velocidad_x = random.randrange(5)
            self.velocidad_y = random.randrange(5)
        if teclas[pygame.K_n]:
            self.velocidad_x = random.randrange(5) * -1
            self.velocidad_y = random.randrange(5) * -1


        # actualiza la posicion del enemigo
        self.rect.x += self.velocidad_x
        self.rect.y += self.velocidad_y
        # Controlamos que el enemigo no salga de pantalla
        if self.rect.left < 0:
            #self.rect.left = 0
            #self.velocidad_x = self.velocidad_x * -1
            self.velocidad_x += 1
        if self.rect.right > SCREEN_WIDTH:
            #self.rect.right = SCREEN_WIDTH
            #self.velocidad_x = self.velocidad_x * -1
            self.velocidad_x -= 1
        if self.rect.bottom > SCREEN_HEIGHT:
            #self.rect.bottom = SCREEN_HEIGHT
            #self.velocidad_y = self.velocidad_y * -1
            self.velocidad_y -= 1
        if self.rect.top < 0:
            #self.rect.top = 0
            #self.velocidad_y = self.velocidad_y * -1
            self.velocidad_y += 1

# Inicialización de Pygame, creación de la ventana, título y control de reloj.
pygame.init()
PANTALLA = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Mi primer juego')
RELOJ = pygame.time.Clock()
# pongo la pantalla en blanco
PANTALLA.fill(BLANCO)

# Grupo de sprites, instanciación del objeto jugador.
sprites = pygame.sprite.Group()
enemigosSprites = pygame.sprite.Group()

# Genero un jugador
jugador = Jugador()
sprites.add(jugador)

# Genero enemigos
for x in range((random.randrange(5))+1):
    enemigo = Enemigos()
    enemigosSprites.add(enemigo)


# cargamos una imagen de fondo
PANTALLA.blit(pygame.image.load("imagenes/1.png").convert(), (0, 0))

fondo = pygame.image.load("imagenes/2.png").convert()
# PANTALLA.blit(fondo,(ejeX, ejeY))
x = 0

fondo2 = pygame.image.load("imagenes/3.png").convert()
# PANTALLA.blit(fondo,(x,0))


# cargo imagen en una variable
icono = pygame.image.load("imagenes/IndustrialTile_35.png").convert()
# uso variable como icono del juego
pygame.display.set_icon(icono)

# print(rectangulo1)
while True:
    # setear los FPS (Es lo que especifica la velocidad del bucle de juego)
    RELOJ.tick(FPS)
    # Eventos
    for event in pygame.event.get():
        if event.type == QUIT:
            # Se cierra y termina el bucle
            pygame.quit()
            sys.exit()


    PANTALLA.fill(BLANCO)
    PANTALLA.blit(pygame.image.load("imagenes/1.png").convert(), (0, 0))

    x_relativa = x % fondo.get_rect().width
    PANTALLA.blit(fondo, (x_relativa - fondo.get_rect().width, 0))
    if x_relativa < SCREEN_WIDTH:
        PANTALLA.blit(fondo, (x_relativa, 0))

    x_relativa = (x * 2) % fondo2.get_rect().width
    PANTALLA.blit(fondo2, (x_relativa - fondo2.get_rect().width, 0))
    if x_relativa < SCREEN_WIDTH:
        PANTALLA.blit(fondo2, (x_relativa, 0))
    x -= 1

    # Actualización de sprites
    sprites.update()
    enemigosSprites.update()

    colision = pygame.sprite.spritecollide(jugador, enemigosSprites,False)
    if colision:
        enemigo.image = pygame.Surface((20, 20))
        enemigo.image.fill(BLANCO)

    # Dibujo los sprites en la pantalla
    sprites.draw(PANTALLA)
    enemigosSprites.draw(PANTALLA)
    # Actualiza el contenido de la pantalla
    #pygame.display.update()
    pygame.display.flip()

