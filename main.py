#!/usr/bin/python
# -*- coding: utf-8 -*-


# Modules
# ---------------------------------------------------------------------
import pygame
from handler import Director
from scene import *
from handler import config
# ---------------------------------------------------------------------


# Functions
# ---------------------------------------------------------------------
def music_init():
    pygame.mixer.pre_init(44100, -16, 2, 2048)
    pygame.mixer.init()
    pygame.mixer.music.load(config.main_menu_audio)
    pygame.mixer.music.play()
# ---------------------------------------------------------------------


def main():
    music_init()
    director = Director()
    scene = SceneStart(director)
    director.change_scene(scene)
    director.loop()


if __name__ == '__main__':
    pygame.init()
    main()