#!/usr/python
# -*- coding: utf-8 -*-


# Modules
# ---------------------------------------------------------------------
import pygame as pg
vec = pg.math.Vector2
from handler.graphics import load_image
from config import *
from character import Character
from ammo import Shot
# ---------------------------------------------------------------------


class Samus(Character):
    def __init__(self, posx, posy, scene):
        Character.__init__(self)
        # Escena actual
        self.scene = scene
        # Cargamos el sheet
        self.sheet = load_image(ZERO_SUIT_STAND_SHEET, True)
        # Definimos medidas
        self.width_stand = 69
        self.height_stand = 108
        self.width_move = 105
        self.height_move = 118
        # Definimos el tamaño de cada clip del sheet
        self.sheet.set_clip(pg.Rect(self.width_stand, 0, self.width_stand, self.height_stand))
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
        self.updated = pg.time.get_ticks()
        self.anim_delay = 60
        # Variables de movimiento
        self.direction = 'stand_right'
        self.pos = vec(posx, posy)
        self.gun_offset = vec(25, -27)
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)
        self.jumping = False
        self.moving = False
        self.shot_list = []


    # Funcion para recoger el sprite marcado por self.frame
    def get_frame(self, frame_set):
        self.frame += 1
        if self.frame > (len(frame_set) - 1):
            self.frame = 0
        return frame_set[self.frame]


    def clip(self, clipped_rect):
        if type(clipped_rect) is dict:
            self.sheet.set_clip(pg.Rect(self.get_frame(clipped_rect)))
        else:
            self.sheet.set_clip(pg.Rect(clipped_rect))


    def animation(self):
        if self.direction == 'right':
            self.sheet = load_image(ZERO_SUIT_MOVE_RIGHT_SHEET, True)
            self.clip(self.right_move_states)
        elif self.direction == 'left':
            self.sheet = load_image(ZERO_SUIT_MOVE_LEFT_SHEET, True)
            self.clip(self.left_move_states)
        elif self.direction == 'stand_right':
            self.sheet = load_image(ZERO_SUIT_STAND_SHEET, True)
            self.clip(self.stand_states[0])
        elif self.direction == 'stand_left':
            self.sheet = load_image(ZERO_SUIT_STAND_SHEET, True)
            self.clip(self.stand_states[1])

        self.image = self.sheet.subsurface(self.sheet.get_clip())


    def jump(self):
        if not self.jumping:
            self.vel.y = -SAMUS_JUMP


    def shot(self):
        if self.direction == 'right' or self.direction == 'stand_right':
            shot = Shot(self.rect.centerx+self.gun_offset.x, self.rect.centery+self.gun_offset.y, self.direction, self.scene)
        elif self.direction == 'left' or self.direction == 'stand_left':
            shot = Shot(self.rect.centerx-self.gun_offset.x, self.rect.centery+self.gun_offset.y, self.direction, self.scene)
        else:
            shot = None
        self.shot_list.append(shot)
        self.scene.sprites.add(shot)


    def update(self):
        self.acc = vec(0, GRAVITY)

        keys = pg.key.get_pressed()
        if keys[pg.K_d]:
            self.acc.x = SAMUS_ACC
            self.direction = 'right'
        if keys[pg.K_a]:
            self.acc.x = -SAMUS_ACC
            self.direction = 'left'

        if self.updated + self.anim_delay <= pg.time.get_ticks():
            self.animation()
            self.updated = pg.time.get_ticks()

        # apply friction
        self.acc.x += self.vel.x * SAMUS_FRIC
        # equations of motion
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc


        self.rect.midbottom = self.pos