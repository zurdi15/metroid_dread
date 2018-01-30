#!/usr/bin/python
# -*- coding: utf-8 -*-

# Modules
# ---------------------------------------------------------------------
# import os
# import sys
# BASE_DIR = os.path.dirname(os.path.dirname(__file__))
# sys.path.append(BASE_DIR + 'character')
# sys.path.append(BASE_DIR + 'handler')
# sys.path.append(BASE_DIR + 'handler/scene')
import pygame
from director import Director
from scene_start import SceneStart
from scene_main_menu import SceneMainMenu
from scene_game import SceneGame
import config
# ---------------------------------------------------------------------

def main():
    director = Director()
    scene = SceneStart(director)
    director.change_scene(scene)
    director.loop()


if __name__ == '__main__':
    pygame.init()
    pygame.mixer.pre_init(44100, -16, 2, 2048)
    pygame.mixer.init()
    pygame.mixer.music.load(config.main_menu_audio)
    pygame.mixer.music.play()
    main()