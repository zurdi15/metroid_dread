#!/usr/bin/python
# -*- coding: utf-8 -*-

"""General configuration of the project"""

import os

# Name
name = 'Metroid: Dread'

# Resolution
width = 800
height = 480
os.environ['SDL_VIDEO_CENTERED'] = '1'

# Directories
characters = 'resources/images/characters'
menu = 'resources/images/menu'
start_game = 'resources/images/start_game'
audio = 'resources/audio'