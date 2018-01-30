#!/usr/python
# -*- coding: utf-8 -*-

# Modules
import os
import sys
import pygame
from pygame.locals import *

PYTROID_DIR = os.path.dirname(os.path.realpath(__file__)) + '/'
sys.path.append(PYTROID_DIR + 'handler')
from image_loader import load_image
sys.path.append(PYTROID_DIR + 'character')
from pymus import Pymus

os.environ['SDL_VIDEO_CENTERED'] = '1'

# Const
WIDTH = 800
HEIGHT = 600
FPS = 60
# Classes
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------

# Functions
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------

def main():
    pygame.display.set_caption("Pytroid")
    master = pygame.display.set_mode((WIDTH, HEIGHT))
    bg_image = load_image('resources/images/background.gif')
    pymus = Pymus(WIDTH, HEIGHT)

    clock = pygame.time.Clock()

    while True:
        time = clock.tick(FPS)
        keys = pygame.key.get_pressed()

        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit(0)

        pymus.move(time, keys)
        master.blit(bg_image, (0, 0))
        master.blit(pymus.sprite, pymus.sprite_collide)

        pygame.display.update()


if __name__ == '__main__':
    pygame.init()
    main()
