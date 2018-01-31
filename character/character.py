#!/usr/python
# -*- coding: utf-8 -*-


# Modules
# ---------------------------------------------------------------------
import pygame
# ---------------------------------------------------------------------


class Character(pygame.sprite.Sprite):
    def __init__(self):
        super(Character, self).__init__()

        self.image = None
        self.rect = None
        self.dx = 0
        self.dy = 0
        self.jumping = False

    def impulse(self, dx, dy):
        self.dx = dx
        self.dy = dy

    def update(self):
        raise NotImplementedError("The update method must be called in any child class")