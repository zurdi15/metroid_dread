#!/usr/bin/python
# -*- coding: utf-8 -*-


# Modules
# ---------------------------------------------------------------------
import pygame
from pygame.locals import *
from handler import config
from handler import graphics
from scene import Scene
from scene_game import SceneGame
# ---------------------------------------------------------------------


class SceneMainMenu(Scene):
    """Escena del menu principal del juego"""

    def __init__(self, director):
        Scene.__init__(self, director)
        self.name = 'scene_main_menu'
        self.start = False
        self.game = False
        self.bg = graphics.load_image(config.bg_main_menu)
        self.element_opacity = 170
        self.element_opacity_selected = 100
        # Element 1
        self.menu_element_1 = graphics.load_image(config.element_main_menu, True)
        self.menu_element_1_rect = self.menu_element_1.get_rect()
        self.menu_element_1_rect.x = 50
        self.menu_element_1_rect.y = config.screen_height / 4 - 105 / 2
        self.menu_element_1.set_alpha(self.element_opacity)
        self.menu_element_1_selected = False
        # Element 2
        self.menu_element_2 = graphics.load_image(config.element_main_menu, True)
        self.menu_element_2_rect = self.menu_element_2.get_rect()
        self.menu_element_2_rect.x = 50
        self.menu_element_2_rect.y = config.screen_height / 4 * 2 - 105 / 2
        self.menu_element_2.set_alpha(self.element_opacity)
        self.menu_element_2_selected = False
        # Element 3
        self.menu_element_3 = graphics.load_image(config.element_main_menu, True)
        self.menu_element_3_rect = self.menu_element_3.get_rect()
        self.menu_element_3_rect.x = 50
        self.menu_element_3_rect.y = config.screen_height / 4 * 3 - 105 / 2
        self.menu_element_3.set_alpha(self.element_opacity)
        self.menu_element_3_selected = False
        # Element selected
        self.menu_element_selected = graphics.load_image(config.element_main_menu_selected, True)
        self.menu_element_selected.set_alpha(self.element_opacity_selected)


    def on_update(self):
        pygame.mouse.set_visible(True)
        if self.start:
            self.start = False
            try:
                self.director.change_scene(self.director.scene_dict['scene_start'])
            except Exception:
                print 'Imposible cambiar de escena'
        if self.game:
            self.game = False
            scene = SceneGame(self.director)
            self.director.change_scene(scene)
        self.check_menu()


    def on_event(self):
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    if self.menu_element_1_selected:
                        self.game = True
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    self.director.quit()
                elif event.key == K_BACKSPACE:
                    self.start = True
                elif event.key == pygame.K_RETURN:
                    self.game = True
                elif event.key == pygame.K_m:
                    if self.director.music_flag:
                        pygame.mixer.music.pause()
                        self.director.music_flag = False
                    else:
                        pygame.mixer.music.unpause()
                        self.director.music_flag = True


    def on_draw(self, screen):
        screen.blit(self.bg, (0, 0))
        if self.menu_element_1_selected:
            screen.blit(self.menu_element_selected, self.menu_element_1_rect)
        else:
            screen.blit(self.menu_element_1, self.menu_element_1_rect)

        if self.menu_element_2_selected:
            screen.blit(self.menu_element_selected, self.menu_element_2_rect)
        else:
            screen.blit(self.menu_element_2, self.menu_element_2_rect)

        if self.menu_element_3_selected:
            screen.blit(self.menu_element_selected, self.menu_element_3_rect)
        else:
            screen.blit(self.menu_element_3, self.menu_element_3_rect)


    def check_menu(self):
        if self.menu_element_1_rect.collidepoint(pygame.mouse.get_pos()):
            self.menu_element_1_selected = True
        else:
            self.menu_element_1_selected = False

        if self.menu_element_2_rect.collidepoint(pygame.mouse.get_pos()):
            self.menu_element_2_selected = True
        else:
            self.menu_element_2_selected = False

        if self.menu_element_3_rect.collidepoint(pygame.mouse.get_pos()):
            self.menu_element_3_selected = True
        else:
            self.menu_element_3_selected = False