#!/usr/bin/python
# -*- coding: utf-8 -*-

# Modules
# ---------------------------------------------------------------------
import pygame
from director import Director
from scene_start import SceneStart
# ---------------------------------------------------------------------

def main():
    director = Director()
    scene = SceneStart(director)
    director.change_scene(scene)
    director.loop()


if __name__ == '__main__':
    pygame.init()
    main()