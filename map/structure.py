#!/usr/python
# -*- coding: utf-8 -*-


# Modules
# ---------------------------------------------------------------------
import pygame as pg
vec = pg.math.Vector2
from config import *
# ---------------------------------------------------------------------


class Structure(pg.sprite.Sprite):
    def __init__(self, posx, posy, w, h, scene):
        pg.sprite.Sprite.__init__(self)
        self.scene = scene
        self.image = pg.Surface((w, h))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = posx
        self.rect.y = posy
        self.pos = vec(posx, posy)


    def update(self):
        self.rect.midtop = self.pos
        # self.rect.x = self.pos.x
        # self.rect.y = self.pos.y