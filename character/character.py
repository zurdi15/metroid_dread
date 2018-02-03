#!/usr/python
# -*- coding: utf-8 -*-


# Modules
# ---------------------------------------------------------------------
import pygame as pg
vec = pg.math.Vector2
# ---------------------------------------------------------------------


class Character(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.scene = None
        self.image = None
        self.rect = None
        self.radius = 0
        self.pos = vec(0, 0)
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)
        self.jumping = False


    def update(self):
        raise NotImplementedError("The update method must be called in any child class")