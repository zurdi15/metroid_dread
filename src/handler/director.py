#!/usr/bin/python
# -*- coding: utf-8 -*-

# Modules
# ---------------------------------------------------------------------
import pygame
from pygame.locals import *
import config
# ---------------------------------------------------------------------


class Director:
    """Representa el objeto principal del juego.

    El objeto Director mantiene en funcionamiento el juego, se
    encarga de actualizar, dibuja y propagar eventos.

    Tiene que utilizar este objeto en conjunto con objetos
    derivados de Scene."""

    def __init__(self):
        self.screen = pygame.display.set_mode((config.width, config.height))
        pygame.display.set_caption(config.name)
        self.scene = None
        self.clock = pygame.time.Clock()
        self.music_flag = False
        self.quit_flag = False

    def loop(self):
        """Pone en funcionamiento el juego."""

        while not self.quit_flag:
            self.time = self.clock.tick(config.fps)

            # Eventos
            for event in pygame.event.get(QUIT):
                if event.type == pygame.QUIT:
                    self.quit()

            # detecta eventos
            self.scene.on_event()

            # actualiza la escena
            self.scene.on_update()

            # dibuja la pantalla
            self.scene.on_draw(self.screen)
            pygame.display.update()

    def change_scene(self, scene):
        """Altera la escena actual."""
        self.scene = scene

    def quit(self):
        self.quit_flag = True