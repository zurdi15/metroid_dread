#!/usr/bin/python
# -*- coding: utf-8 -*-


# Modules
# ---------------------------------------------------------------------
import pygame
from handler import Director
from scene import SceneStart, SceneMainMenu,SceneGame
# ---------------------------------------------------------------------


def main():
    pygame.init()
    #pygame.event.set_grab(True)
    director = Director()
    scene = SceneGame(director)
    director.change_scene(scene)
    director.loop()


if __name__ == '__main__':
    main()