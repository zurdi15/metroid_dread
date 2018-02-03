#!/usr/bin/python
# -*- coding: utf-8 -*-


"""
General configuration of the project:
"""


# Modules
# ---------------------------------------------------------------------
import os
# ---------------------------------------------------------------------


# Name
TITLE = 'Metroid: Dread'

# Resolution
SCREEN_WIDTH = 800#1366
SCREEN_HEIGHT = 480#768
FPS = 60
os.environ['SDL_VIDEO_CENTERED'] = '1'

# Parameters
# Enviroment
GRAVITY = 0.98

# Samus
SAMUS_ACC = 0.9
SAMUS_JUMP = 22
SAMUS_FRIC = -0.2

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Directories
# Start game
START_GAME = 'resources/images/start_game'
BG_START_GAME = START_GAME + '/bg_start.png'

# Main menu
MENU = 'resources/images/menu'
BG_MAIN_MENU = MENU + '/bg_main_menu.png'
ELEMENT_MAIN_MENU = MENU + '/main_menu_slot_0.png'
ELEMENT_MAIN_MENU_SELECTED = MENU + '/main_menu_slot_1.png'

# Characters
CHARACTERS = 'resources/images/character'
ZERO_SUIT_STAND_SHEET = CHARACTERS + '/zero_suit_stand_sheet.png'
ZERO_SUIT_MOVE_RIGHT_SHEET = CHARACTERS + '/zero_suit_move_right_sheet.png'
ZERO_SUIT_MOVE_LEFT_SHEET = CHARACTERS + '/zero_suit_move_left_sheet.png'

# Ammo
AMMO = 'resources/images/ammo'
SHOT = AMMO + '/shot.png'

# Audio
AUDIO = 'resources/audio'
MAIN_MENU_AUDIO = AUDIO + '/music_menu.ogg'
APPEAR_JINGLE = AUDIO +'/appear_jingle.ogg'
AREA_1_MUSIC = AUDIO+'/area_1_music.ogg'

# Video
VIDEO = 'resources/video'
INTRO_MOVIE = VIDEO + '/intro_movie.mp4'

# Fonts
FONTS = 'resources/fonts'
DROID_SANS = FONTS + '/droid_sans.ttf'

# TEST
TEST_BG = 'resources/test/test_bg.png'
TEST_SPRITES_KATE = 'resources/test/test_sprites_kate.png'