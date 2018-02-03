#!/usr/bin/python
# -*- coding: utf-8 -*-


# Modules
# ---------------------------------------------------------------------
import pygame
from pygame.locals import *
from config import *
from handler import graphics
from scene import Scene
from scene_game import SceneGame
# ---------------------------------------------------------------------


class SceneMainMenu(Scene):
    """Escena del menu principal del juego"""

    def __init__(self, director):
        Scene.__init__(self, director)
        pygame.mouse.set_visible(True)
        self.name = 'scene_main_menu'
        self.start_flag = False
        self.game_flag = False
        self.bg = graphics.load_image(BG_MAIN_MENU)
        self.element_opacity = 170
        self.element_opacity_selected = 100
        # Element 1
        self.menu_element_1 = graphics.load_image(ELEMENT_MAIN_MENU, True)
        self.menu_element_1_rect = self.menu_element_1.get_rect()
        self.menu_element_1_rect.centerx = SCREEN_WIDTH / 2
        self.menu_element_1_rect.centery = SCREEN_HEIGHT / 4
        self.menu_element_1.set_alpha(self.element_opacity)
        self.menu_element_1_selected = False
        # Element 2
        self.menu_element_2 = graphics.load_image(ELEMENT_MAIN_MENU, True)
        self.menu_element_2_rect = self.menu_element_2.get_rect()
        self.menu_element_2_rect.centerx = SCREEN_WIDTH / 2
        self.menu_element_2_rect.centery = SCREEN_HEIGHT / 4 * 2
        self.menu_element_2.set_alpha(self.element_opacity)
        self.menu_element_2_selected = False
        # Element 3
        self.menu_element_3 = graphics.load_image(ELEMENT_MAIN_MENU, True)
        self.menu_element_3_rect = self.menu_element_3.get_rect()
        self.menu_element_3_rect.centerx = SCREEN_WIDTH / 2
        self.menu_element_3_rect.centery = SCREEN_HEIGHT / 4 * 3
        self.menu_element_3.set_alpha(self.element_opacity)
        self.menu_element_3_selected = False
        # Element selected
        self.menu_element_selected = graphics.load_image(ELEMENT_MAIN_MENU_SELECTED, True)
        self.menu_element_selected.set_alpha(self.element_opacity_selected)


    def on_event(self):
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    if self.menu_element_1_selected:
                        self.game_flag = True

            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    self.director.quit()
                elif event.key == K_BACKSPACE:
                    self.start_flag = True
                elif event.key == pygame.K_RETURN:
                    self.game_flag = True
                elif event.key == pygame.K_m:
                    if self.director.music_flag:
                        pygame.mixer.music.pause()
                        self.director.music_flag = False
                    else:
                        pygame.mixer.music.unpause()
                        self.director.music_flag = True


    def on_update(self):
        if self.start_flag:
            self.start_flag = False
            try:
                self.director.change_scene(self.director.scene_dict['scene_start'])
            except Exception:
                print 'Imposible cambiar de escena'
        if self.game_flag:
            self.game_flag = False
            scene = SceneGame(self.director)
            self.director.change_scene(scene)
        self.check_menu()


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

        graphics.load_text(screen, "New game", SCREEN_WIDTH / 4, SCREEN_HEIGHT / 4-20, size=25)



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