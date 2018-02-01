#!/usr/bin/python


# Modules
# ---------------------------------------------------------------------
import pygame
from pygame.locals import RLEACCEL
from handler import config
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
    image = pygame.transform.scale(image, (image.get_size()[0], image.get_size()[1]))
    return image


def load_text(text, posx, posy, color=config.white, size=45):
    source = pygame.font.Font(config.droid_sans, size)
    text_image = pygame.font.Font.render(source, text, 1, color)
    text_image_rect = text_image.get_rect()
    text_image_rect.centerx = posx
    text_image_rect.centery = posy
    return text_image, text_image_rect