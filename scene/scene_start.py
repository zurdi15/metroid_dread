#!/usr/bin/python
# -*- coding: utf-8 -*-


# Modules
# ---------------------------------------------------------------------
import pygame
from pygame.locals import *
from handler import config
from scene import Scene
from handler import graphics
from scene_main_menu import SceneMainMenu
# ---------------------------------------------------------------------


class SceneStart(Scene):
    """Escena inicial del juego, esta es la primera que se carga cuando inicia"""

    def __init__(self, director):
        Scene.__init__(self, director)
        self.name = 'scene_start'
        self.main_menu = False
        self.bg = graphics.load_image(config.bg_start_game)

    def on_update(self):
        if self.main_menu:
            self.main_menu = False
            scene = SceneMainMenu(self.director)
            self.director.change_scene(scene)

    def on_event(self):
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    self.main_menu = True
            if event.type == KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.main_menu = True
                if event.key == pygame.K_m:
                    if self.director.music_flag:
                        pygame.mixer.music.pause()
                        self.director.music_flag = False
                    else:
                        pygame.mixer.music.unpause()
                        self.director.music_flag = True

    def on_draw(self, screen):
        screen.blit(self.bg, (0, 0))