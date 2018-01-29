#!/usr/python
# -*- coding: utf-8 -*-

# Modules
import sys
import pygame
from pygame.locals import *

# Const
WIDTH = 640
HEIGHT = 480

# Classes
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------

# Functions
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------

def main():
    pygame.display.set_caption("Pytroid")
    master = pygame.display.set_mode((WIDTH, HEIGHT))
    bg_image = load_image('resources/images/background.jpg')

    while True:

        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit(0)

        master.blit(bg_image, (0, 0))
        pygame.display.update()


if __name__ == '__main__':
    pygame.init()
    main()
