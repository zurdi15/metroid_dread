#!/usr/python
# -*- coding: utf-8 -*-

# Modules
# ---------------------------------------------------------------------
import pygame
from pygame.locals import *
from image_loader import load_image
# ---------------------------------------------------------------------

class Samus(pygame.sprite.Sprite):
    def __init__(self, SCREEN_WIDHT, SCREEN_HEIGHT):
        pygame.sprite.Sprite.__init__(self)

        self.SCREEN_WIDHT = SCREEN_WIDHT
        self.SCREEN_HEIGHT = SCREEN_HEIGHT
        image_path = "resources/images/characters/samus_front.png"
        self.sprite = load_image(image_path, True)
        self.sprite_collide = self.sprite.get_rect()
        self.WIDTH = self.sprite_collide[2]
        self.HEIGHT = self.sprite_collide[3]
        self.sprite_collide.centerx = 0 + self.WIDTH/2
        self.sprite_collide.centery = SCREEN_HEIGHT - self.HEIGHT/2
        self.speed = [0.5, 0.2]


    def move(self, time, keys):
        if self.sprite_collide.left >= 0:
            if keys[K_LEFT]:
                self.sprite_collide.centerx -= self.speed[0] * time
        if self.sprite_collide.right <= self.SCREEN_WIDHT:
            if keys[K_RIGHT]:
                self.sprite_collide.centerx += self.speed[0] * time