#!/usr/bin/python
# -*- coding: utf-8 -*-


"""
General configuration of the project:
    - device:
        1 = pc
        2 = 3ds
"""


# Modules
# ---------------------------------------------------------------------
import os
# ---------------------------------------------------------------------


# Name
name = 'Metroid: Dread'

# Resolution
device = 1
screen_width = 800 / device
screen_height = 480 / device
fps = 60
os.environ['SDL_VIDEO_CENTERED'] = '1'

# Parameters
gravity = 0.7

# Directories
# Start game
start_game = 'resources/images/start_game'
bg_start_game = start_game+'/bg_start.png'

# Main menu
menu = 'resources/images/menu'
bg_main_menu = menu+'/bg_main_menu.png' \

# Characters                    ''
characters = 'resources/images/character'
samus_front = characters+'/samus_front.png'
samus_move_sheet = characters+'/samus_move_sheet.png'
samus_zero_move_sheet = characters+'/zero_suit_move_sheet.png'

# Audio
audio = 'resources/audio'
main_menu_audio = audio+'/music_menu.ogg'

# TEST
test_bg = 'resources/test/test_bg.png'
test_sprites_kate = 'resources/test/test_sprites_kate.png'