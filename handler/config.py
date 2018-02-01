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

samus_transparent = (153, 179, 193)

# Parameters
gravity = 0.7 / device

# Colors
black = (0,0,0)
white = (255, 255, 255)

# Directories
# Start game
start_game = 'resources/images/start_game'
bg_start_game = start_game+'/bg_start.png'

# Main menu
menu = 'resources/images/menu'
bg_main_menu = menu+'/bg_main_menu.png'
element_main_menu = menu+'/main_menu_slot_0.png'
element_main_menu_selected = menu+'/main_menu_slot_1.png'

# Characters
characters = 'resources/images/character'
zero_suit_stand_sheet = characters+'/zero_suit_stand_sheet.png'
zero_suit_move_right_sheet = characters+'/zero_suit_move_right_sheet.png'
zero_suit_move_left_sheet = characters+'/zero_suit_move_left_sheet.png'

# Ammo
ammo = 'resources/images/ammo'
shot = ammo+'/shot.png'

# Audio
audio = 'resources/audio'
main_menu_audio = audio+'/music_menu.ogg'

# Video
video = 'resources/video'
intro_movie = video+'/intro_movie.mepg'

# Fonts
fonts = 'resources/fonts'
droid_sans = fonts+'/droid_sans.ttf'

# TEST
test_bg = 'resources/test/test_bg.png'
test_sprites_kate = 'resources/test/test_sprites_kate.png'