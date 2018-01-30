#!/usr/python
# -*- coding: utf-8 -*-

# Modules
# ---------------------------------------------------------------------
import pygame
from pygame.locals import *
import graphics
import config
# ---------------------------------------------------------------------

class Kate(pygame.sprite.Sprite):
    def __init__(self, SCREEN_WIDHT, SCREEN_HEIGHT):
        pygame.sprite.Sprite.__init__(self)

        self.SCREEN_WIDHT = SCREEN_WIDHT
        self.SCREEN_HEIGHT = SCREEN_HEIGHT

        self.sheet = graphics.load_image(config.test_sprite, True)
        self.sheet.set_clip(pygame.Rect(0, 0, 52, 76))
        self.image = self.sheet.subsurface(self.sheet.get_clip())
        self.rect = self.image.get_rect()
        self.frame = 0
        self.left_states = {0: (0, 76, 52, 76), 1: (52, 76, 52, 76), 2: (156, 76, 52, 76)}
        self.right_states = {0: (0, 152, 52, 76), 1: (52, 152, 52, 76), 2: (156, 152, 52, 76)}
        self.up_states = {0: (0, 228, 52, 76), 1: (52, 228, 52, 76), 2: (156, 228, 52, 76)}
        self.down_states = {0: (0, 0, 52, 76), 1: (52, 0, 52, 76), 2: (156, 0, 52, 76)}
        self.WIDTH = self.rect[2]
        self.HEIGHT = self.rect[3]
        self.speed = [0.3/config.device, 0.3/config.device]


    def get_frame(self, frame_set):
        self.frame += 1
        if self.frame > (len(frame_set) - 1):
            self.frame = 0
        return frame_set[self.frame]


    def clip(self, clipped_rect):
        if type(clipped_rect) is dict:
            self.sheet.set_clip(pygame.Rect(self.get_frame(clipped_rect)))
        else:
            self.sheet.set_clip(pygame.Rect(clipped_rect))
        return clipped_rect


    def update(self, direction, time):
        if direction == 'left':
            self.clip(self.left_states)
            if self.rect.x >= 0:
                self.rect.x -= self.speed[0] * time
        if direction == 'right':
            self.clip(self.right_states)
            if self.rect.x <= self.SCREEN_WIDHT-self.WIDTH:
                self.rect.x += self.speed[0] * time
        if direction == 'up':
            self.clip(self.up_states)
            if self.rect.y >= 0:
                self.rect.y -= self.speed[1] * time
        if direction == 'down':
            self.clip(self.down_states)
            if self.rect.y <= self.SCREEN_HEIGHT-self.HEIGHT:
                self.rect.y += self.speed[1] * time

        if direction == 'stand_left':
            self.clip(self.left_states[0])
        if direction == 'stand_right':
            self.clip(self.right_states[0])
        if direction == 'stand_up':
            self.clip(self.up_states[0])
        if direction == 'stand_down':
            self.clip(self.down_states[0])

        self.image = self.sheet.subsurface(self.sheet.get_clip())


    def handle_event(self, time):
        keys = pygame.key.get_pressed()
        if keys[K_LEFT]:
            self.update('left', time)
        if keys[K_RIGHT]:
            self.update('right', time)
        if keys[K_UP]:
            self.update('up', time)
        if keys[K_DOWN]:
            self.update('down', time)
