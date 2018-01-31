#!/usr/bin/python
# -*- coding: utf-8 -*-


# Modules
# ---------------------------------------------------------------------
import pygame
from pygame.locals import *
from handler import config
import scene
from handler import graphics
from scene_main_menu import SceneMainMenu
# ---------------------------------------------------------------------


class SceneStart(scene.Scene):
    """Escena inicial del juego, esta es la primera que se carga cuando inicia"""

    def __init__(self, director):
        scene.Scene.__init__(self, director)
        self.bg = graphics.load_image(config.bg_start_game)
        self.ENTER = False

    def on_update(self):
        if self.ENTER:
            scene = SceneMainMenu(self.director)
            self.director.change_scene(scene)

    def on_event(self):
        for event in pygame.event.get(KEYDOWN):
            if event.key == pygame.K_RETURN:
                self.ENTER = True
            if event.key == pygame.K_m:
                if self.director.music_flag:
                    pygame.mixer.music.pause()
                    self.director.music_flag = False
                else:
                    pygame.mixer.music.unpause()
                    self.director.music_flag = True

    def on_draw(self, screen):
        screen.blit(self.bg, (0, 0))