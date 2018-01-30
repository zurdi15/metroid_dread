#!/usr/bin/python
# -*- coding: utf-8 -*-


# Modules
# ---------------------------------------------------------------------
import pygame
from pygame.locals import *
import scene
import config
import graphics
from kate import Kate
# ---------------------------------------------------------------------

class SceneTest(scene.Scene):

    def __init__(self, director):
        """Escena para testing"""
        scene.Scene.__init__(self, director)
        self.kate = Kate(config.width, config.height)

    def on_update(self):
        pass

    def on_event(self):
        self.kate.handle_event(self.director.time)

    def on_draw(self, screen):
        screen.fill(pygame.Color('gray'))
        screen.blit(self.kate.image, self.kate.rect)