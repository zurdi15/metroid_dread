#!/usr/bin/python
# -*- coding: utf-8 -*-


# Modules
# ---------------------------------------------------------------------
import pygame
from pygame.locals import *
from moviepy.editor import VideoFileClip
from moviepy.editor import AudioFileClip
from handler import config
from scene import Scene
from handler import graphics
from scene_main_menu import SceneMainMenu
# ---------------------------------------------------------------------


class SceneStart(Scene):
    """Escena inicial del juego, esta es la primera que se carga cuando inicia"""

    def __init__(self, director):
        Scene.__init__(self, director)
        pygame.mouse.set_visible(True)
        self.name = 'scene_start'
        self.main_menu_FLAG = False
        self.bg = graphics.load_image(config.bg_start_game)
        self.music_init()
        #self.intro_init()


    def on_event(self):
        for event in pygame.event.get():
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
                        pygame.mixer.music.pause()
                        self.director.music_flag = False
                    else:
                        pygame.mixer.music.unpause()
                        self.director.music_flag = True


    def on_update(self):
        if self.main_menu_FLAG:
            self.main_menu_FLAG = False
            scene = SceneMainMenu(self.director)
            self.director.change_scene(scene)


    def on_draw(self, screen):
        screen.blit(self.bg, (0, 0))


    @staticmethod
    def intro_init():
        pygame.mouse.set_visible(False)
        movie = VideoFileClip(config.intro_movie)
        audio = AudioFileClip(config.main_menu_audio)
        movie = movie.set_audio(audio)
        movie.preview()


    @staticmethod
    def music_init():
        pygame.mixer.pre_init(44100, -16, 2, 2048)
        pygame.mixer.init()
        pygame.mixer.music.load(config.main_menu_audio)
        pygame.mixer.music.play()