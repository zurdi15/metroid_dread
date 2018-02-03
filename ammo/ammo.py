#!/usr/bin/python
# -*- coding: utf-8 -*-


# Modules
# ---------------------------------------------------------------------
import pygame as pg
# ---------------------------------------------------------------------


class Ammo(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.scene = None
        self.image = None
        self.rect = None
        self.radius = 0
        self.pos = None
        self.direction = ''
        self.speed = 0

    def update(self):
        raise NotImplementedError("The update method must be called in any child class")