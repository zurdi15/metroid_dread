#!/usr/bin/python
# -*- coding: utf-8 -*-


# Modules
# ---------------------------------------------------------------------
import pygame
from pygame.locals import *
from scene import Scene
from character import Samus
# ---------------------------------------------------------------------


class SceneGame(Scene):

    def __init__(self, director):
        """Escena del juego"""
        Scene.__init__(self, director)
        self.name = 'scene_game'
        self.MAIN_MENU = False
        self.samus = Samus(400, 100)

    def on_update(self):
        if self.MAIN_MENU:
            self.MAIN_MENU = False
            self.director.change_scene(self.director.scene_dict['scene_main_menu'])
        self.samus.update()

    def on_event(self):

        # Controla todas las teclas
        for event in pygame.event.get():
            if event.type == KEYUP:
                pass
                if event.key == K_RIGHT:
                    self.samus.move('stand_right')
                elif event.key == K_LEFT:
                    self.samus.move('stand_left')
            elif event.type == KEYDOWN:
                if event.key == K_BACKSPACE:
                    self.MAIN_MENU = True
                if event.key == K_SPACE:
                    self.samus.jump()
                if event.key == K_m:
                    if self.director.music_flag:
                        pygame.mixer.music.pause()
                        self.director.music_flag = False
                    else:
                        pygame.mixer.music.unpause()
                        self.director.music_flag = True

    def on_draw(self, screen):
        screen.fill([0, 0, 0])
        screen.blit(self.samus.image, (self.samus.posx, self.samus.posy))