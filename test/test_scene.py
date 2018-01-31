#!/usr/bin/python
# -*- coding: utf-8 -*-


# Modules
# ---------------------------------------------------------------------
import pygame
import scene
from samus import Samus
# ---------------------------------------------------------------------

class SceneTest(scene.Scene):

    def __init__(self, director):
        """Escena para testing"""
        scene.Scene.__init__(self, director)
        #self.character_test = Kate()
        self.character_test = Samus(100, 100)

    def on_update(self):
        pass

    def on_event(self):
        self.character_test.update(self.director.time)

    def on_draw(self, screen):
        screen.fill(pygame.Color('gray'))
        screen.blit(self.character_test.image, self.character_test.rect)
