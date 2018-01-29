#!/usr/bin/python
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
def load_image(filename, transparent=False):
    try:
        image = pygame.image.load(filename)
    except pygame.error, message:
        raise SystemExit, message
    image = image.convert()
    if transparent:
        color = image.get_at((0, 0))
        image.set_colorkey(color, RLEACCEL)
    return image
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

    return 0


if __name__ == '__main__':
    pygame.init()
    main()