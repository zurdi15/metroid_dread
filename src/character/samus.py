#!/usr/python
# -*- coding: utf-8 -*-

# Modules
# ---------------------------------------------------------------------
import pygame
from pygame.locals import *
import graphics
import config
# ---------------------------------------------------------------------

class Samus(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.WIDHT = 70
        self.HEIGHT = 117
        self.sheet = graphics.load_image(config.samus_zero_sheet, True)
        self.sheet.set_clip(pygame.Rect(0, 0, self.WIDHT, self.HEIGHT))
        self.image = self.sheet.subsurface(self.sheet.get_clip())
        self.rect = self.image.get_rect()
        self.frame = 0
        self.left_states = {0: (0, 0, self.WIDHT, self.HEIGHT), 1: (self.WIDHT, 0, self.WIDHT, self.HEIGHT), 2: (self.WIDHT*2, 0, self.WIDHT, self.HEIGHT), 3: (self.WIDHT*3, 0, self.WIDHT, self.HEIGHT), 4: (self.WIDHT*4, 0, self.WIDHT, self.HEIGHT), 5: (self.WIDHT*5, 0, self.WIDHT, self.HEIGHT), 6: (self.WIDHT*6, 0, self.WIDHT, self.HEIGHT)}
        self.right_states = {0: (0, 152, 52, 76), 1: (52, 152, 52, 76), 2: (156, 152, 52, 76)}
        self.up_states = {0: (0, 228, 52, 76), 1: (52, 228, 52, 76), 2: (156, 228, 52, 76)}
        self.down_states = {0: (0, 0, 52, 76), 1: (52, 0, 52, 76), 2: (156, 0, 52, 76)}
        self.updated = pygame.time.get_ticks()
        self.speed = [2 / config.device, 2 / config.device]

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
            if self.rect.x <= config.width - self.WIDHT:
                self.rect.x += self.speed[0] * time

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
        if self.updated + 50 <= pygame.time.get_ticks():
            keys = pygame.key.get_pressed()
            if keys[K_LEFT]:
                self.update('left', time)
            if keys[K_RIGHT]:
                self.update('right', time)
            self.updated = pygame.time.get_ticks()

        for event in pygame.event.get(KEYUP):
            if event.key == pygame.K_LEFT:
                self.update('stand_left', time)
            if event.key == pygame.K_RIGHT:
                self.update('stand_right', time)