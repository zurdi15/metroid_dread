import sys
import pygame
import random
from pygame.locals import *
from pygame.color import *
import pymunk


def add_ball(space): # Esta funcion agrega una esfera
    mass = 1
    radius = 14
    inertia = pymunk.moment_for_circle(mass, 0, radius) # Por lo general la inercia se saca por la forma aproximada del cuerpo
    body = pymunk.Body(mass, inertia) # Creamos el cuerpo
    x = random.randint(120,380)
    body.position = x, 550 # Le asignamos una posicion al azar en el eje horizontal
    shape = pymunk.Circle(body, radius) # Al cuerpo le asignamos una forma
    space.add(body, shape) # Tnato el cuerpo como su forma se agregan al espacio
    return shape


def draw_ball(screen, ball): # Esta funcion dibuja la esfera en pantalla
    p = int(ball.body.position.x), 600-int(ball.body.position.y)
    pygame.draw.circle(screen, THECOLORS["blue"], p, int(ball.radius), 2)


def main():

    screen = pygame.display.set_mode((600, 600))
    pygame.display.set_caption("Pymunk test")
    clock = pygame.time.Clock()
    running = True
    space = pymunk.Space() # Creamos el Space
    space.gravity = (0.0, -900.0) # Colocamos gravedad: una fuerza constante en el tiempo
    balls = []
    ticks_to_next_ball = 10

    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            elif event.type == KEYDOWN and event.key == K_ESCAPE:
                running = False

        ticks_to_next_ball -= 1

        if ticks_to_next_ball <= 0:
            ticks_to_next_ball = 25
            ball_shape = add_ball(space)
            balls.append(ball_shape)

        screen.fill(THECOLORS["white"])

        for ball in balls:
            draw_ball(screen, ball)
        space.step(1/50.0)
        pygame.display.update()
        clock.tick(50)

if __name__ == '__main__':
    pygame.init()
    sys.exit(main())