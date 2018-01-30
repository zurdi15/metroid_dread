#!/usr/python
# -*- coding: utf-8 -*-

import pygame
from pygame.locals import *
from image_loader import load_image

class Pymus(pygame.sprite.Sprite):
    def __init__(self, SCREEN_WIDHT, SCREEN_HEIGHT):
        pygame.sprite.Sprite.__init__(self)
        self.SCREEN_WIDHT = SCREEN_WIDHT
        self.SCREEN_HEIGHT = SCREEN_HEIGHT
        self.WIDHT = 5
        self.HEIGHT = 15
        self.sprite = load_image("resources/images/pymus_real.png", True)
        self.sprite_collide = self.sprite.get_rect()
        self.sprite_collide.centerx = 0
        self.sprite_collide.centery = SCREEN_HEIGHT-self.HEIGHT
        self.speed = [0.5, 0.2]


    def move(self, time, keys):
        if self.sprite_collide.left >= 0 and keys[K_LEFT]:
            self.sprite_collide.centerx -= self.speed[0] * time
        if self.sprite_collide.right <= self.SCREEN_WIDHT and keys[K_RIGHT]:
            self.sprite_collide.centerx += self.speed[0] * time