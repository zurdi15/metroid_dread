#!/usr/python
# -*- coding: utf-8 -*-

# Modules
# ---------------------------------------------------------------------
import os
import sys
import pygame
from pygame.locals import *
PYTROID_DIR = os.path.dirname(os.path.realpath(__file__)) + '/'
sys.path.append(PYTROID_DIR + 'handler')
from image_loader import load_image
from director import Director
from scene_start import SceneStart
sys.path.append(PYTROID_DIR + 'character')
from samus import Samus
# ---------------------------------------------------------------------

# Variables
# ---------------------------------------------------------------------
os.environ['SDL_VIDEO_CENTERED'] = '1'
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 480
FPS = 60
# ---------------------------------------------------------------------

def main():
    director = Director()
    scene = SceneStart(director)
    director.change_scene(scene)
    director.loop()

    # Init
    # ---------------------------------------------------------------------
    pygame.display.set_caption("Metroid: Dread")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    samus = Samus(SCREEN_WIDTH, SCREEN_HEIGHT)
    bg_start_image = load_image('resources/images/start_game/bg_start.png')
    bg_start_image = pygame.transform.scale(bg_start_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
    # ---------------------------------------------------------------------
	
    # ---------------------------------------------------------------------

    # Flags
    # ---------------------------------------------------------------------
    INTRO = True
    # ---------------------------------------------------------------------

	# Main loop
    # ---------------------------------------------------------------------
    while True:
        time = clock.tick(FPS)
        keys = pygame.key.get_pressed()

        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit(0)

        if INTRO:
            screen.blit(bg_start_image, (0, 0))
            if keys[K_RETURN]:
                INTRO = False

        else:
            # Update
            # -----------------------------------------------------------
            samus.move(time, keys)
            # -----------------------------------------------------------

            # Render
            # -----------------------------------------------------------
            screen.blit(samus.sprite, samus.sprite_collide)
            # -----------------------------------------------------------

        pygame.display.update()
    # ---------------------------------------------------------------------
if __name__ == '__main__':
    def platform():
        platform = raw_input()
        if platform == 'pc':
            return 800, 480
        elif platform == '3ds':
            return 400, 240
        else:
            return 800, 480
    #SCREEN_WIDTH, SCREEN_HEIGHT = platform()
    pygame.init()
    main()

