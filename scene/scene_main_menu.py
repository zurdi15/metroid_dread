#!/usr/bin/python
# -*- coding: utf-8 -*-


# Modules
# ---------------------------------------------------------------------
import pygame
from pygame.locals import *
from handler import config
from handler import graphics
from scene import Scene
from scene_game import SceneGame
# ---------------------------------------------------------------------


class SceneMainMenu(Scene):
    """Escena del menu principal del juego"""

    def __init__(self, director):
        Scene.__init__(self, director)
        self.name = 'scene_main_menu'
        self.START = False
        self.GAME = False
        self.bg = graphics.load_image(config.bg_main_menu)

    def on_update(self):
        if self.START:
            self.START = False
            try:
                self.director.change_scene(self.director.scene_dict['scene_start'])
            except Exception:
                print 'Imposible cambiar de escena'
        if self.GAME:
            self.GAME = False
            scene = SceneGame(self.director)
            self.director.change_scene(scene)

    def on_event(self):
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_BACKSPACE:
                    self.START = True
                if event.key == pygame.K_RETURN:
                    self.GAME = True
                if event.key == pygame.K_m:
                    if self.director.music_flag:
                        pygame.mixer.music.pause()
                        self.director.music_flag = False
                    else:
                        pygame.mixer.music.unpause()
                        self.director.music_flag = True

    def on_draw(self, screen):
        screen.blit(self.bg, (0, 0))