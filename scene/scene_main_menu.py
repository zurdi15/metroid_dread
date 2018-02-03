#!/usr/bin/python
# -*- coding: utf-8 -*-


# Modules
# ---------------------------------------------------------------------
import pygame as pg
from pygame.locals import *
from config import *
from handler.graphics import *
from scene import Scene
from scene_game import SceneGame
# ---------------------------------------------------------------------


class MainMenuElement(pg.sprite.Sprite):
    def __init__(self, posx, posy):
        pg.sprite.Sprite.__init__(self)
        self.image = load_image(ELEMENT_MAIN_MENU, True)
        self.image.set_alpha(170)
        self.rect = self.image.get_rect()
        self.rect.centerx = posx
        self.rect.centery = posy
        self.selected = False


    def update(self):
        if self.selected:
            self.image = load_image(ELEMENT_MAIN_MENU_SELECTED, True)
            self.image.set_alpha(100)
        else:
            self.image = load_image(ELEMENT_MAIN_MENU, True)
            self.image.set_alpha(170)




class SceneMainMenu(Scene):
    """Escena del menu principal del juego"""

    def __init__(self, director):
        Scene.__init__(self, director)
        pg.mouse.set_visible(True)
        self.name = 'scene_main_menu'
        self.start_flag = False
        self.game_flag = False
        self.bg = load_image(BG_MAIN_MENU)
        self.elements = pg.sprite.Group()
        # Elements
        self.element_1 = MainMenuElement(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 4)
        self.elements.add(self.element_1)
        self.element_2 = MainMenuElement(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 4 * 2)
        self.elements.add(self.element_2)
        self.element_3 = MainMenuElement(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 4 * 3)
        self.elements.add(self.element_3)


    def on_event(self):
        for event in pg.event.get():
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    if self.element_1.selected:
                        self.game_flag = True

            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    self.director.quit()
                elif event.key == K_BACKSPACE:
                    self.start_flag = True
                elif event.key == pg.K_RETURN:
                    self.game_flag = True
                elif event.key == pg.K_m:
                    if self.director.music_flag:
                        pg.mixer.music.pause()
                        self.director.music_flag = False
                    else:
                        pg.mixer.music.unpause()
                        self.director.music_flag = True


    def on_update(self):
        self.elements.update()

        for element in self.elements:
            if element.rect.collidepoint(pg.mouse.get_pos()):
                element.selected = True
            else:
                element.selected = False

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


    def on_draw(self, screen):
        screen.blit(self.bg, (0, 0))
        self.elements.draw(screen)
        load_text(screen, "New game", SCREEN_WIDTH / 4, SCREEN_HEIGHT / 4-20, size=25)