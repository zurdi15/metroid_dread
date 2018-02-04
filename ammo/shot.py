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
    def __init__(self, posx, posy, direction, vertical_shot, ammo_type, scene):
        Ammo.__init__(self)
        self.scene = scene
        self.ammo_type = ammo_type
        if self.ammo_type == 'normal':
            self.image = graphics.load_image(SHOT, True)
        elif self.ammo_type == 'plasma':
            self.image = graphics.load_image(SHOT_PLASMA, True)
        self.rect = self.image.get_rect()
        self.rect.center = (posx, posy)
        self.radius = self.rect.width/2
        self.pos = vec(posx, posy)
        self.direction = direction
        self.vertical_shot = vertical_shot
        self.speed = 20


    def update(self):
        if not self.vertical_shot:
            if self.direction == 'right' or self.direction == 'stand_right':
                self.image = pg.transform.flip(self.image, True, False)
                self.pos.x += self.speed
            elif self.direction == 'left' or self.direction == 'stand_left':
                self.image = pg.transform.flip(self.image, True, False)
                self.pos.x -= self.speed
        else:
            self.pos.y -= self.speed

        if self.ammo_type == 'normal':
            self.radius = self.rect.width/2
        elif self.ammo_type == 'plasma':
            self.radius = self.rect.width / 3

        if self.pos.x < 0 or self.pos.x > SCREEN_WIDTH or self.pos.y < 0:
            self.kill()

        self.rect.center = self.pos