#!/usr/python
# -*- coding: utf-8 -*-


# Modules
# ---------------------------------------------------------------------
import pygame as pg
from handler.graphics import load_image
vec = pg.math.Vector2
import random
from config import *
from character import Character
# ---------------------------------------------------------------------


class Mob(Character):
    def __init__(self):
        Character.__init__(self)
        self.image = load_image(MOB, True)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(-200, SCREEN_WIDTH+200)
        self.rect.y = random.randrange(-100, -40)
        self.pos = vec(self.rect.x, self.rect.y)
        self.radius = 18
        self.speed = vec(0, random.randrange(1, 4))
        self.damage = 25


    def update(self):
        self.pos.y += self.speed.y
        self.rect.x = self.pos.x
        self.rect.y = self.pos.y

        if self.rect.top > SCREEN_HEIGHT:
            self.pos.x = random.randrange(-300, SCREEN_WIDTH+300)
            self.pos.y = random.randrange(-100, -40)
            self.speed.y = random.randrange(1, 8)