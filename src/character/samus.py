#!/usr/python
# -*- coding: utf-8 -*-

# Modules
# ---------------------------------------------------------------------
import pygame
from pygame.locals import *
import graphics
import config
# ---------------------------------------------------------------------

class Samus(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.sprite = graphics.load_image(config.samus_front, True)
        self.sprite_collide = self.sprite.get_rect()
        self.sprite_collide.centerx = 0 + self.sprite_collide[0]/2
        self.sprite_collide.centery = config.height/2 - self.sprite_collide[1]
        self.speed = [0.5/config.device, 0.2/config.device]


    def move(self, time, keys):
        if self.sprite_collide.left >= 0:
            if keys[K_LEFT]:
                self.sprite_collide.centerx -= self.speed[0] * time
        if self.sprite_collide.right <= config.width:
            if keys[K_RIGHT]:
                self.sprite_collide.centerx += self.speed[0] * time