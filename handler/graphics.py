#!/usr/bin/python


# Modules
# ---------------------------------------------------------------------
import pygame as pg
from pygame.locals import RLEACCEL
from config import *
# ---------------------------------------------------------------------


def load_image(filename, transparent=False):
    try:
        image = pg.image.load(filename)
    except pg.error, message:
        raise SystemExit, message
    image = image.convert()
    if transparent:
        color = image.get_at((0, 0))
        image.set_colorkey(color, RLEACCEL)
    image = pg.transform.scale(image, (image.get_size()[0], image.get_size()[1]))
    return image


def load_text(text, posx, posy, color=WHITE, size=45):
    source = pg.font.Font(DROID_SANS, size)
    text_image = pg.font.Font.render(source, text, 1, color)
    text_image_rect = text_image.get_rect()
    text_image_rect.centerx = posx
    text_image_rect.centery = posy
    return text_image, text_image_rect