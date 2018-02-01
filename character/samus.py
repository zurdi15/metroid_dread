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

        # Cargamos el sheet
        self.sheet = load_image(config.samus_zero_move_sheet, True)

        # Definimos medidas
        self.width = 93
        self.height = 111

        # Definimos el tamaño de cada clip del sheet
        self.sheet.set_clip(pygame.Rect(0, 0, self.width, self.height))

        # Recogemos la imagen inicial del sheet
        self.image = self.sheet.subsurface(self.sheet.get_clip())

        # Recogemos el rect de la imagen
        self.rect = self.image.get_rect()

        # Establecemos el primer frame de la animacion a 0 (hay 4)
        self.frame = 0

        # Definimos cada estado con sus coordenadas
        self.right_states = {0: (0, 0, self.width, self.height),
                             1: (self.width, 0, self.width*2, self.height),
                             2: (self.width*2, self.height, self.width*3, self.height),
                             3: (self.width*3, self.height, self.width*4, self.height),
                             4: (0, self.height, self.width, self.height*2),
                             5: (self.width, self.height, self.width*2, self.height*2),
                             6: (self.width*2, self.height, self.width*3, self.height*2)}

        self.left_states = {0: (0, 0, self.width, self.height),
                            1: (self.width, 0, self.width * 2, self.height),
                            2: (self.width * 2, self.height, self.width * 3, self.height),
                            3: (self.width * 3, self.height, self.width * 4, self.height),
                            4: (0, self.height, self.width, self.height * 2),
                            5: (self.width, self.height, self.width * 2, self.height * 2),
                            6: (self.width * 2, self.height, self.width * 3, self.height * 2)}

        # Definimos el delay de la animacion
        self.updated = pygame.time.get_ticks()

        # Variables de movimiento
        self.rect.x = px
        self.rect.y = py
        self.dx = 0
        self.dy = 0
        self.speed = [10 / config.device, 10 / config.device]
        self.jump_force = 15
        self.jumping = True
        self.updated = pygame.time.get_ticks()


    # Funcion para recoger el sprite marcado por self.frame
    def get_frame(self, frame_set):
        print self.frame
        self.frame += 1
        if self.frame > (len(frame_set) - 1):
            self.frame = 0
        return frame_set[self.frame]


    def clip(self, clipped_rect):
        if type(clipped_rect) is dict:
            self.sheet.set_clip(pygame.Rect(self.get_frame(clipped_rect)))
        else:
            self.sheet.set_clip(pygame.Rect(clipped_rect))


    def move(self, direction):
        if direction == 'left':
            self.clip(self.left_states)
            if self.rect.x >= 0:
                self.dx = -self.speed[0]
            else:
                self.dx = 0
                self.rect.x = 0
        elif direction == 'right':
            self.clip(self.right_states)
            if self.rect.x <= config.screen_width-self.width:
                self.dx = self.speed[0]
            else:
                self.dx = 0
                self.rect.x = config.screen_width - self.width
        elif direction == 'stand_left':
            self.clip(self.left_states[0])
            self.dx = 0
        elif direction == 'stand_right':
            self.clip(self.right_states[0])
            self.dx = 0

        self.image = self.sheet.subsurface(self.sheet.get_clip())


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

        if self.updated + config.fps <= pygame.time.get_ticks():
            keys = pygame.key.get_pressed()
            if keys[K_RIGHT]:
                self.move('right')
            elif keys[K_LEFT]:
                self.move('left')
            self.updated = pygame.time.get_ticks()