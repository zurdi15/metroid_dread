#!/usr/python
# -*- coding: utf-8 -*-


# Modules
# ---------------------------------------------------------------------
import pygame
from pygame.locals import *
from handler.graphics import load_image
from character import Character
from handler import config
# ---------------------------------------------------------------------


class Samus(Character):
    def __init__(self, px, py):
        Character.__init__(self)

        # self.image = load_image(config.samus_front, True)
        # self.width = self.image.get_width()
        # self.height = self.image.get_height()

        self.sheet = load_image(config.samus_move_sheet, True)
        self.width = 25
        self.height = 48
        self.sheet.set_clip(pygame.Rect(0, 0, self.width, self.height))
        self.image = self.sheet.subsurface(self.sheet.get_clip())

        self.rect = self.image.get_rect()
        self.rect.x = px
        self.rect.y = py
        self.dx = 0
        self.dy = 0
        self.speed = [10 / config.device, 10 / config.device]
        self.jump_force = 15
        self.jumping = True
        self.updated = pygame.time.get_ticks()


    def move(self, direction):
        if direction == 'left':
            if self.rect.x >= 0:
                self.dx = -self.speed[0]
            else:
                self.dx = 0
                self.rect.x = 0
        elif direction == 'right':
            if self.rect.x <= config.screen_width-self.width:
                self.dx = self.speed[0]
            else:
                self.dx = 0
                self.rect.x = config.screen_width - self.width
        elif direction == 'stand_left':
            self.dx = 0
        elif direction == 'stand_right':
            self.dx = 0


    def calculate_gravity(self):
        if self.dy == 0:
            self.dy = 1
        else:
            self.dy = self.dy + config.gravity


    def jump(self):
        if not self.jumping:
            self.impulse(self.dx, -self.jump_force)
            self.jumping = True


    def update(self):
        self.calculate_gravity()

        self.rect.x = self.rect.x + self.dx
        self.rect.y = self.rect.y + self.dy

        if self.rect.y + self.rect.height > config.screen_height:
            self.rect.y = config.screen_height - self.rect.height
            self.jumping = False
            self.dy = 0

        keys = pygame.key.get_pressed()
        if keys[K_RIGHT]:
            self.move('right')
        elif keys[K_LEFT]:
            self.move('left')