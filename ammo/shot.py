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
        self.rect = self.image.get_rect()
        self.rect.centerx = posx
        self.rect.centery = posy
        self.direction = direction
        self.speed = 20


    def set_pos(self, posx, posy):
        self.rect.centerx = posx
        self.rect.centery = posy


    def update(self):
        if self.direction == 'right':
            self.rect.centerx = self.rect.centerx + self.speed
        elif self.direction == 'left':
            self.rect.centerx = self.rect.centerx - self.speed