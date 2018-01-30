#!/usr/bin/python
# -*- coding: utf-8 -*-


# Modules
# ---------------------------------------------------------------------
import pygame
from pygame.locals import *
import config
import scene
import graphics
from scene_game import SceneGame
# ---------------------------------------------------------------------


# Clases
# ---------------------------------------------------------------------
class SceneMainMenu(scene.Scene):
    """Escena del menu principal del juego"""

    def __init__(self, director):
        scene.Scene.__init__(self, director)
        self.bg = graphics.load_image(config.bg_main_menu)
        self.ENTER = False

    def on_update(self):
        if self.ENTER:
            scene = SceneGame(self.director)
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
# ---------------------------------------------------------------------