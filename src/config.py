#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
General configuration of the project:
    - device:
        1 = pc
        2 = 3ds
"""

import os

# Name
name = 'Metroid: Dread'

# Resolution
device = 1
width = 800/device
height = 480/device
fps = 60
os.environ['SDL_VIDEO_CENTERED'] = '1'

# Parameters
gravity = 0.35

# Directories
start_game = 'resources/images/start_game'
bg_start_game = start_game+'/bg_start.png'

menu = 'resources/images/menu'
bg_main_menu = menu+'/bg_main_menu.png' \
                    ''
characters = 'resources/images/characters'
samus_front = characters+'/samus_front.png'
samus_zero_sheet = characters+'/zero_suit_sheet.png'

audio = 'resources/audio'
main_menu_audio = audio+'/music_menu.ogg'

# TEST
test_bg = 'resources/test/test_bg.png'
test_sprites_kate = 'resources/test/test_sprites_kate.png'