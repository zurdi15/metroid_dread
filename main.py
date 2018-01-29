import pygame
import sys

from pygame.locals import *

pygame.init()

pygame.display.set_caption("Pytroid")
win = pygame.display.set_mode((600,400))


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()