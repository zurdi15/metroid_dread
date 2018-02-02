#!/usr/bin/python
# -*- coding: utf-8 -*-


# Modules
# ---------------------------------------------------------------------
import pygame
from pygame.locals import *
from handler import config
from handler import graphics
from scene import Scene
from character import Samus
# ---------------------------------------------------------------------


class SceneGame(Scene):

    def __init__(self, director):
        """Escena del juego"""
        Scene.__init__(self, director)
        pygame.mouse.set_visible(False)
        self.name = 'scene_game'
        self.main_menu = False
        self.screen_limit_x = (0, config.screen_width)
        self.screen_limit_y = (0, config.screen_height)
        self.sprites = pygame.sprite.Group()
        self.samus = Samus(100, 100, self)
        self.sprites.add(self.samus)
        # Controls
        self.controls_left, self.controls_left_rect = graphics.load_text("left: A", 50, 30, size=15)
        self.controls_right, self.controls_right_rect = graphics.load_text("right: D", 50, 50, size=15)
        self.controls_jump, self.controls_jump_rect = graphics.load_text("jump: space", 50, 70, size=15)
        self.controls_shot, self.controls_shot_rect = graphics.load_text("shot: left click", 50, 90, size=15)


    def on_event(self):
        # Controla todas las teclas
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    self.samus.shot()

            elif event.type == KEYUP:
                if event.key == K_d:
                    self.samus.move('stand_right')
                elif event.key == K_a:
                    self.samus.move('stand_left')

            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    self.director.quit()
                elif event.key == K_BACKSPACE:
                    self.main_menu = True
                elif event.key == K_SPACE:
                    self.samus.jump()
                elif event.key == K_m:
                    if self.director.music_flag:
                        pygame.mixer.music.pause()
                        self.director.music_flag = False
                    else:
                        pygame.mixer.music.unpause()
                        self.director.music_flag = True


    def on_update(self):
        if self.main_menu:
            self.main_menu = False
            try:
                self.director.change_scene(self.director.scene_dict['scene_main_menu'])
            except Exception:
                print 'Imposible cambiar de escena'

        self.samus.update()

        for shot in self.samus.shot_list:
            if shot.rect.right <= self.screen_limit_x[0] or shot.rect.left >= self.screen_limit_x[1]:
                self.samus.shot_list.remove(shot)
            shot.update()


    def on_draw(self, screen):
        screen.fill(config.black)
        self.sprites.draw(screen)
        self.draw_controls(screen)


    def draw_controls(self, screen):
        screen.blit(self.controls_left, self.controls_left_rect)
        screen.blit(self.controls_right, self.controls_right_rect)
        screen.blit(self.controls_jump, self.controls_jump_rect)
        screen.blit(self.controls_shot, self.controls_shot_rect)