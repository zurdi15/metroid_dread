#!/usr/bin/python
# -*- coding: utf-8 -*-


# Modules
# ---------------------------------------------------------------------
import pygame
from pygame.locals import *
import scene
import config
import graphics
from samus import Samus
# ---------------------------------------------------------------------

class SceneGame(scene.Scene):

    def __init__(self, director):
        """Escena del juego"""
        scene.Scene.__init__(self, director)
        self.samus = Samus(config.width, config.height)
        self.bg = graphics.load_image(config.bg_start_game)

    def on_update(self):
        pass

    def on_event(self):
        for event in pygame.event.get(KEYDOWN):
            if event.key == pygame.K_m:
                if self.director.music_flag:
                    pygame.mixer.music.pause()
                    self.director.music_flag = False
                else:
                    pygame.mixer.music.unpause()
                    self.director.music_flag = True
        keys = pygame.key.get_pressed()
        self.samus.move(self.director.time, keys)

    def on_draw(self, screen):
        screen.fill([0, 0, 0])
        screen.blit(self.samus.sprite, self.samus.sprite_collide)