#!/usr/bin/python
# -*- coding: utf-8 -*-


# Modules
# ---------------------------------------------------------------------
import pygame
from handler import config
from handler import graphics
# ---------------------------------------------------------------------

class Shot(pygame.sprite.Sprite):
    def __init__(self, posx, posy, direction):
        pygame.sprite.Sprite.__init__(self)
        self.image = graphics.load_image(config.shot, True)
        self.posx = posx
        self.posy = posy
        self.direction = direction
        self.speed = 20


    def set_pos(self, posx, posy):
        self.posx = posx
        self.posy = posy


    def update(self):
        if self.direction == 'right':
            self.posx = self.posx + self.speed
        elif self.direction == 'left':
            self.posx = self.posx - self.speed