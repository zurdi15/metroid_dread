#!/usr/bin/python

# Modules
# ---------------------------------------------------------------------
import pygame
from pygame.locals import RLEACCEL
import config
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
    image = pygame.transform.scale(image, (image.get_size()[0]/config.device, image.get_size()[1]/config.device))
    return image

def load_text(text, posx, posy, color=(255, 255, 255)):
    source = pygame.font.Font("resources/fonts/DroidSans.ttf", 45)
    score_image = pygame.font.Font.render(source, text, 1, color)
    score_image_rect = score_image.get_rect()
    score_image_rect.centerx = posx
    score_image_rect.centery = posy
    return score_image, score_image_rect