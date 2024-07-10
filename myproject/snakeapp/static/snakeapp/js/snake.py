# Juego SNAKE

import pygame
import random

# Inicializar Pygame
pygame.init()

# Definición de variables
cuadrado = 20
ancho, alto = 400, 400
pantalla = pygame.display.set_mode((ancho, alto))

# Colores
verde = (125, 255, 90)
rojo = (255, 0, 0)
blanco = (255, 255, 255)
negro = (0, 0, 0)

# Función para inicializar variables del juego
def iniciar_juego():
    global serpiente, dx, dy, manzana, puntos, juego_activo, juego_terminado, velocidad
    serpiente = [{'x': ancho // 2, 'y': alto // 2}]
    dx, dy = cuadrado, 0
    manzana = nueva_manzana()
    puntos = 0
    juego_activo = False
    juego_terminado = False
    velocidad = 5

# Asignación aleatoria de coordenadas para la manzana
def nueva_manzana():
    return {'x': random.randint(0, (ancho // cuadrado) - 1) * cuadrado, 
            'y': random.randint(0, (alto // cuadrado) - 1) * cuadrado}

# Inicializar variables del juego
iniciar_juego()

# Fuente para la puntuación
fuente = pygame.font.SysFont('Arial', 25)

# Función para dibujar texto en la pantalla
def mostrar_texto(superficie, texto, color, x, y):
    superficie_texto = fuente.render(texto, True, color)
    pantalla.blit(superficie_texto, (x, y))

# Función para dibujar la serpiente y la manzana
def dibujar():
    pantalla.fill(verde)
    
    pygame.draw.rect(pantalla, rojo, (manzana['x'], manzana['y'], cuadrado, cuadrado))
    pygame.draw.rect(pantalla, negro, (manzana['x'], manzana['y'], cuadrado, cuadrado), 1)
    
    for segment in serpiente:
        pygame.draw.rect(pantalla, blanco, (segment['x'], segment['y'], cuadrado, cuadrado))
        pygame.draw.rect(pantalla, negro, (segment['x'], segment['y'], cuadrado, cuadrado), 1)
        sf = "   Score: %s                Level: %s   " % (puntos, (velocidad - 4))
        pygame.display.set_caption(sf)

    if juego_terminado:
        mostrar_texto(pantalla, 'GAME OVER!!', rojo, ancho // 2 - 70, alto // 2 - 20)
        mostrar_texto(pantalla, 'Presiona ESPACIO para reiniciar.', rojo, ancho // 2 - 140, alto // 2 + 10)
    elif not juego_activo:
        mostrar_texto(pantalla, 'Presiona ESPACIO para empezar !!', rojo, ancho // 2 - 157, alto // 2 - 25)
        
    pygame.display.flip()

# Función para comprobar colisiones
def colision():
    cabeza = serpiente[0]
    return (cabeza['x'] < 0 or cabeza['x'] >= ancho or 
            cabeza['y'] < 0 or cabeza['y'] >= alto or
            any(segment == cabeza for segment in serpiente[1:]))

# Bucle principal del juego
tiempo = pygame.time.Clock()
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_LEFT and dx != cuadrado:
                dx, dy = -cuadrado, 0
            elif evento.key == pygame.K_RIGHT and dx != -cuadrado:
                dx, dy = cuadrado, 0
            elif evento.key == pygame.K_UP and dy != cuadrado:
                dx, dy = 0, -cuadrado
            elif evento.key == pygame.K_DOWN and dy != -cuadrado:
                dx, dy = 0, cuadrado
            elif evento.key == pygame.K_SPACE:
                if juego_terminado:
                    iniciar_juego()
                else:
                    juego_activo = not juego_activo
    
    if juego_activo:
        cabeza = {'x': serpiente[0]['x'] + dx, 'y': serpiente[0]['y'] + dy}
        serpiente.insert(0, cabeza)
        
        if cabeza == manzana:
            manzana = nueva_manzana()
            puntos += 1
            # Incrementar la velocidad cada 10 puntos
            if puntos % 10 == 0:
                velocidad += 1
        else:
            serpiente.pop()
        
        if colision():
            juego_activo = False
            juego_terminado = True
    
    dibujar()
    tiempo.tick(velocidad)