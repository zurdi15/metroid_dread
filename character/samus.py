#!/usr/python
# -*- coding: utf-8 -*-


# Modules
# ---------------------------------------------------------------------
import pygame
from pygame.locals import *
from handler.graphics import load_image
from handler import config
from character import Character
from ammo import Shot
# ---------------------------------------------------------------------


class Samus(Character):
    def __init__(self, posx, posy, scene):
        Character.__init__(self)
        # Escena actual
        self.scene = scene
        # Cargamos el sheet
        self.sheet = load_image(config.zero_suit_stand_sheet, True)
        # Definimos medidas
        self.width_stand = 69
        self.height_stand = 108
        self.width_move = 105
        self.height_move = 118
        # Definimos el tamaño de cada clip del sheet
        self.sheet.set_clip(pygame.Rect(self.width_stand, 0, self.width_stand, self.height_stand))
        # Recogemos la imagen inicial del sheet
        self.image = self.sheet.subsurface(self.sheet.get_clip())
        # Recogemos el rect de la imagen
        self.rect = self.image.get_rect()
        self.rect.center = (posx, posy)
        # Establecemos el primer frame de la animacion a 0 (hay 4)
        self.frame = 0
        # Definimos cada estado con sus coordenadas
        self.stand_states =  {0: (self.width_stand, 0, self.width_stand, self.height_stand),
                              1: (0, 0, self.width_stand, self.height_stand),}
        self.right_move_states = {0: (0, 0, self.width_move, self.height_move),
                                  1: (self.width_move, 0, self.width_move, self.height_move),
                                  2: (self.width_move * 2, 0, self.width_move, self.height_move),
                                  3: (self.width_move * 3, 0, self.width_move, self.height_move),
                                  4: (self.width_move * 4, 0, self.width_move, self.height_move),
                                  5: (self.width_move * 5, 0, self.width_move, self.height_move),
                                  6: (self.width_move * 6, 0, self.width_move, self.height_move),
                                  7: (self.width_move * 7, 0, self.width_move, self.height_move),
                                  8: (self.width_move * 8, 0, self.width_move, self.height_move),
                                  9: (self.width_move * 9, 0, self.width_move, self.height_move), }
        self.left_move_states = {0: (self.width_move * 9, 0, self.width_move, self.height_move),
                                 1: (self.width_move * 8, 0, self.width_move, self.height_move),
                                 2: (self.width_move * 7, 0, self.width_move, self.height_move),
                                 3: (self.width_move * 6, 0, self.width_move, self.height_move),
                                 4: (self.width_move * 5, 0, self.width_move, self.height_move),
                                 5: (self.width_move * 4, 0, self.width_move, self.height_move),
                                 6: (self.width_move * 3, 0, self.width_move, self.height_move),
                                 7: (self.width_move * 2, 0, self.width_move, self.height_move),
                                 8: (self.width_move, 0, self.width_move, self.height_move),
                                 9: (0, 0, self.width_move, self.height_move), }
        # Definimos el delay de la animacion
        self.updated = pygame.time.get_ticks()
        # Variables de movimiento
        self.direction = 'right'
        self.dx = 0
        self.dy = 0
        self.speed = [10, 10]
        self.jump_force = 15
        self.jumping = True
        self.moving = False
        self.shot_list = []
        self.updated = pygame.time.get_ticks()


    def calculate_gravity(self):
        if self.dy == 0:
            self.dy = 1
        else:
            self.dy = self.dy + config.gravity


    # Funcion para recoger el sprite marcado por self.frame
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


    def move(self, direction):
        if direction == 'right':
            self.direction = 'right'
            self.moving = True
            self.sheet = load_image(config.zero_suit_move_right_sheet, True)
            self.clip(self.right_move_states)
            if self.rect.right <= config.screen_width:
                self.dx = self.speed[0]
            else:
                self.dx = 0
        elif direction == 'left':
            self.direction = 'left'
            self.moving = True
            self.sheet = load_image(config.zero_suit_move_left_sheet, True)
            self.clip(self.left_move_states)
            if self.rect.left >= 0:
                self.dx = -self.speed[0]
            else:
                self.dx = 0
        elif direction == 'stand_right':
            self.direction = 'right'
            self.sheet = load_image(config.zero_suit_stand_sheet, True)
            self.clip(self.stand_states[0])
            self.dx = 0
        elif direction == 'stand_left':
            self.direction = 'left'
            self.sheet = load_image(config.zero_suit_stand_sheet, True)
            self.clip(self.stand_states[1])
            self.dx = 0
        self.image = self.sheet.subsurface(self.sheet.get_clip())


    def jump(self):
        if not self.jumping:
            self.impulse(self.dx, -self.jump_force)
            self.jumping = True


    def shot(self):
        if self.direction == 'right':
            shot = Shot(self.rect.centerx+15, self.rect.centery-27, self.direction)
        elif self.direction == 'left':
            shot = Shot(self.rect.centerx-15, self.rect.centery-27, self.direction)
        self.shot_list.append(shot)
        self.scene.sprites.add(shot)


    def update(self):
        self.calculate_gravity()

        self.rect.centerx = self.rect.centerx + self.dx
        self.rect.centery = self.rect.centery + self.dy

        if self.rect.bottom > config.screen_height:
            self.rect.bottom = config.screen_height
            self.jumping = False
            self.dy = 0

        if self.updated + config.fps <= pygame.time.get_ticks():
            keys = pygame.key.get_pressed()
            if keys[K_d]:
                self.move('right')
            elif keys[K_a]:
                self.move('left')
            self.updated = pygame.time.get_ticks()