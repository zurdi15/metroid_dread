#!/usr/bin/python
# -*- coding: utf-8 -*-


# Modules
# ---------------------------------------------------------------------
import pygame as pg
from pygame.locals import *
from config import *
from handler import graphics
from scene import Scene
from character import Samus
from map import Structure
# ---------------------------------------------------------------------


class SceneGame(Scene):

    def __init__(self, director):
        """Escena del juego"""
        Scene.__init__(self, director)
        pg.mouse.set_visible(False)
        self.name = 'scene_game'
        self.main_menu = False
        self.sprites = pg.sprite.Group()
        self.structures = pg.sprite.Group()
        self.ground = Structure(-200, SCREEN_HEIGHT - 40, SCREEN_WIDTH+200, 40, self)
        self.sprites.add(self.ground)
        self.structures.add(self.ground)
        self.samus = Samus(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, self)
        self.sprites.add(self.samus)
        # Controls
        self.controls_left, self.controls_left_rect = graphics.load_text("left: A", 50, 30, size=15)
        self.controls_left_rect.left = 30
        self.controls_right, self.controls_right_rect = graphics.load_text("right: D", 50, 60, size=15)
        self.controls_right_rect.left = 30
        self.controls_jump, self.controls_jump_rect = graphics.load_text("jump: space", 50, 90, size=15)
        self.controls_jump_rect.left = 30
        self.controls_shot, self.controls_shot_rect = graphics.load_text("shot: mouse_1", 50, 120, size=15)
        self.controls_shot_rect.left = 30


    def on_event(self):
        # Controla todas las teclas
        for event in pg.event.get():
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    self.samus.shot()

            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    self.director.quit()
                elif event.key == K_BACKSPACE:
                    self.main_menu = True
                elif event.key == K_SPACE:
                    self.samus.jump()
                elif event.key == K_m:
                    if self.director.music_flag:
                        pg.mixer.music.pause()
                        self.director.music_flag = False
                    else:
                        pg.mixer.music.unpause()
                        self.director.music_flag = True

            elif event.type == KEYUP:
                if event.key == K_a:
                    self.samus.direction = 'stand_left'
                if event.key == K_d:
                    self.samus.direction = 'stand_right'


    def on_update(self):
        self.sprites.update()

        # check if player hits a platform - only if falling
        if self.samus.vel.y > 0:
            hits = pg.sprite.spritecollide(self.samus, self.structures, False)
            if hits:
                self.samus.pos.y = hits[0].rect.top
                self.samus.vel.y = 0

        print self.samus.vel.x
        # Running right - moving camera
        if self.samus.direction == 'right':
            self.samus.pos.x -= self.samus.vel.x
            self.ground.rect.x -= self.samus.vel.x
            for shot in self.samus.shot_list:
                shot.pos.x -= self.samus.vel.x
                if shot.pos.x < -10 or shot.pos.x > SCREEN_WIDTH:
                    shot.kill()

        # Running left - moving camera
        if self.samus.direction == 'left':
            self.samus.pos.x -= self.samus.vel.x
            self.ground.rect.x += abs(self.samus.vel.x)
            for shot in self.samus.shot_list:
                shot.pos.x += self.samus.vel.x


        # Comprueba que vayamos al menu principal
        if self.main_menu:
            self.main_menu = False
            try:
                self.director.change_scene(self.director.scene_dict['scene_main_menu'])
            except Exception:
                print 'Imposible cambiar de escena'


    def on_draw(self, screen):
        screen.fill(BLACK)
        #self.draw_samus_rect(screen)
        self.sprites.draw(screen)
        self.draw_controls(screen)


    def draw_controls(self, screen):
        screen.blit(self.controls_left, self.controls_left_rect)
        screen.blit(self.controls_right, self.controls_right_rect)
        screen.blit(self.controls_jump, self.controls_jump_rect)
        screen.blit(self.controls_shot, self.controls_shot_rect)


    def draw_samus_rect(self, screen):
        r = pg.Surface((self.samus.rect.width, self.samus.rect.height))
        r.fill((255, 255, 255))
        screen.blit(r, self.samus.rect)