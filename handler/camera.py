#!/usr/bin/python
# -*- coding: utf-8 -*-


# Modules
# ---------------------------------------------------------------------
# ---------------------------------------------------------------------


class Camera:
    def __init__(self):
        self.posx = 0
        self.posy = 0

    def move(self, posx, posy):
        self.posx = posx
        self.posy = posy