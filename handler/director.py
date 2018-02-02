#!/usr/bin/python
# -*- coding: utf-8 -*-


# Modules
# ---------------------------------------------------------------------
import pygame
from pygame.locals import *
from handler import config
# ---------------------------------------------------------------------


class Director:
    """Representa el objeto principal del juego.

    El objeto Director mantiene en funcionamiento el juego, se
    encarga de actualizar, dibuja y propagar eventos.

    Tiene que utilizar este objeto en conjunto con objetos
    derivados de Scene."""

    def __init__(self):
        self.screen = pygame.display.set_mode((config.screen_width, config.screen_height))
        pygame.display.set_caption(config.name)
        self.clock = pygame.time.Clock()
        self.time = 0
        self.scene = None
        self.scene_dict = {}
        self.music_flag = True
        self.running = True


    def loop(self):
        """Pone en funcionamiento el juego."""
        while self.running:
            self.time = self.clock.tick(config.fps)

            # Eventos
            for event in pygame.event.get(QUIT):
                self.quit()

            # Detecta eventos
            self.scene.on_event()

            # Actualiza la escena
            self.scene.on_update()

            # Dibuja la pantalla
            self.scene.on_draw(self.screen)
            pygame.display.update()


    def change_scene(self, scene):
        """Altera la escena actual."""
        self.scene_dict[scene.name] = scene
        self.scene = scene


    def quit(self):
        self.running = False