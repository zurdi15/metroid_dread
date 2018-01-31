#!/usr/bin/python
# -*- coding: utf-8 -*-


# Modules
# ---------------------------------------------------------------------
import pygame
import scene
import config
from graphics import load_image
from kate import Kate
from samus import Samus
# ---------------------------------------------------------------------

class SceneTest(scene.Scene):

    def __init__(self, director):
        """Escena para testing"""
        scene.Scene.__init__(self, director)
        self.character_test = Samus()
        self.bg = load_image(config.test_bg)

    def on_update(self):
        pass

    def on_event(self):
        self.character_test.handle_event(self.director.time)

    def on_draw(self, screen):
        screen.blit(self.bg, (0, 0))
        screen.blit(self.character_test.image, self.character_test.rect)
