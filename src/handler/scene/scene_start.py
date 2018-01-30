#!/usr/bin/python
# -*- coding: utf-8 -*-


# Modules
# ---------------------------------------------------------------------
import scene
# ---------------------------------------------------------------------


# Clases
# ---------------------------------------------------------------------
class SceneStart(scene.Scene):
    """Escena inicial del juego, esta es la primera que se carga cuando inicia"""

    def __init__(self, director):
        scene.Scene.__init__(self, director)

    def on_update(self):
        pass

    def on_event(self):
        pass

    def on_draw(self, screen):
        pass
# ---------------------------------------------------------------------