#!/usr/bin/python
# -*- coding: utf-8 -*-


# Modules
# ---------------------------------------------------------------------
import pygame as pg
vec = pg.math.Vector2
from config import *
from handler import graphics
from ammo import Ammo
# ---------------------------------------------------------------------

class Shot(Ammo):
    def __init__(self, posx, posy, direction, scene):
        Ammo.__init__(self)
        self.scene = scene
        self.image = graphics.load_image(SHOT, True)
        self.rect = self.image.get_rect()
        self.rect.center = (posx, posy)
        self.pos = vec(posx, posy)
        self.direction = direction
        self.speed = 20


    def update(self):
        if self.direction == 'right' or self.direction == 'stand_right':
            self.pos.x += self.speed
        elif self.direction == 'left' or self.direction == 'stand_left':
            self.pos.x -= self.speed

        if self.pos.x < 0 or self.pos.x > SCREEN_WIDTH:
            self.kill()

        self.rect.center = self.pos