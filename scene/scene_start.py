#!/usr/bin/python
# -*- coding: utf-8 -*-


# Modules
# ---------------------------------------------------------------------
import pygame as pg
from pygame.locals import *
from moviepy.editor import VideoFileClip
from moviepy.editor import AudioFileClip
from config import *
from scene import Scene
from handler import graphics
from scene_main_menu import SceneMainMenu
# ---------------------------------------------------------------------


class SceneStart(Scene):
    """Escena inicial del juego, esta es la primera que se carga cuando inicia"""

    def __init__(self, director):
        Scene.__init__(self, director)
        self.name = 'scene_start'
        self.main_menu_FLAG = False
        self.bg = graphics.load_image(BG_START_GAME)
        self.press_start, self.press_start_rect = graphics.load_text("Press start", SCREEN_WIDTH/2, SCREEN_HEIGHT/4*3)
        self.music_init()
        #self.intro_init()
        pg.mouse.set_visible(True)
        pg.mouse.set_pos(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)


    def on_event(self):
        for event in pg.event.get():
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    self.main_menu_FLAG = True

            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    self.director.quit()
                elif event.key == K_RETURN:
                    self.main_menu_FLAG = True
                elif event.key == K_m:
                    if self.director.music_flag:
                        pg.mixer.music.pause()
                        self.director.music_flag = False
                    else:
                        pg.mixer.music.unpause()
                        self.director.music_flag = True


    def on_update(self):
        if self.main_menu_FLAG:
            self.main_menu_FLAG = False
            scene = SceneMainMenu(self.director)
            self.director.change_scene(scene)


    def on_draw(self, screen):
        screen.blit(self.bg, (0, 0))
        screen.blit(self.press_start, self.press_start_rect)


    @staticmethod
    def intro_init():
        pg.mouse.set_visible(False)
        movie = VideoFileClip(INTRO_MOVIE)
        audio = AudioFileClip(MAIN_MENU_AUDIO)
        movie = movie.set_audio(audio)
        movie.preview()


    @staticmethod
    def music_init():
        pg.mixer.pre_init(44100, -16, 2, 2048)
        pg.mixer.init()
        pg.mixer.music.load(MAIN_MENU_AUDIO)
        pg.mixer.music.play()