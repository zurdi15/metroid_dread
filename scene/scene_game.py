#!/usr/bin/python
# -*- coding: utf-8 -*-


# Modules
# ---------------------------------------------------------------------
import pygame as pg
from pygame.locals import *
from config import *
from handler.graphics import *
from scene import Scene
from character import Samus
from character import Mob
from map import Structure
# ---------------------------------------------------------------------


class SceneGame(Scene):

    def __init__(self, director):
        """Escena del juego"""
        Scene.__init__(self, director)
        pg.mouse.set_visible(False)
        #self.set_music()
        self.name = 'scene_game'
        self.main_menu = False
        # Game elements
        self.sprites = pg.sprite.Group()
        self.structures = pg.sprite.Group()
        self.mobs = pg.sprite.Group()
        self.generate_samus()
        self.generate_structures()
        #self.generate_mobs()



# Events
# -----------------------------------------------------------------------------------------------------------------------
    def on_event(self):
        for event in pg.event.get():

            # - Check mouse
            # -- Check shooting
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    self.samus.shot()
                # -- Ckeck ammo change
                elif event.button == 3:
                    self.samus.ammo_change()

            # - Check keyboard
            elif event.type == KEYDOWN:
                # -- Check quiting
                if event.key == K_ESCAPE:
                    self.director.quit()
                # -- Check going main menu
                elif event.key == K_BACKSPACE:
                    self.main_menu = True
                # -- Check jumping
                elif event.key == K_SPACE:
                    self.samus.jump()
                # -- Check enable/disable music
                elif event.key == K_m:
                    if self.director.music_flag:
                        pg.mixer.music.pause()
                        self.director.music_flag = False
                    else:
                        pg.mixer.music.unpause()
                        self.director.music_flag = True
            # -- Check stop moving
            elif event.type == KEYUP:
                if event.key == K_a:
                    self.samus.direction = 'stand_left'
                if event.key == K_d:
                    self.samus.direction = 'stand_right'
# ----------------------------------------------------------------------------------------------------------------------


# Updates
# ----------------------------------------------------------------------------------------------------------------------
    def on_update(self):

        # ------------- DEBUG SECTION -------------
        if DEBUG:
            pass
        # ------------- DEBUG SECTION -------------

        self.sprites.update()

        # - Colissions
        # -- Ground
        if self.samus.vel.y > 0:
            hits = pg.sprite.spritecollide(self.samus, self.structures, False)
            if hits:
                self.samus.pos.y = hits[0].rect.top
                self.samus.vel.y = 0

        # -- Shots
        if self.samus.ammo_type == 'normal':
            hits = pg.sprite.groupcollide(self.mobs, self.samus.shots, True, True)
            for hit in hits:
                m = Mob()
                self.sprites.add(m)
                self.mobs.add(m)
        elif self.samus.ammo_type == 'plasma':
            hits = pg.sprite.groupcollide(self.mobs, self.samus.shots, True, False)
            for hit in hits:
                m = Mob()
                self.sprites.add(m)
                self.mobs.add(m)

        # -- Mobs
        if not self.samus.invulnerable:
            hits = pg.sprite.spritecollide(self.samus, self.mobs, False, pg.sprite.collide_circle)
            for hit in hits:
                self.samus.lifes -= 1
                self.samus.invulnerable = True

        # - Moving camera
        self.samus.pos.x -= self.samus.vel.x
        #self.samus.pos.y -= self.samus.vel.y
        for struc in self.structures:
            struc.pos.x -= self.samus.vel.x
         #   struc.pos.y -= self.samus.vel.y
        for mob in self.mobs:
            mob.rect.x -= int(self.samus.vel.x)
            mob.rect.y -= int(self.samus.vel.y)


        # Checking going main menu
        if self.main_menu:
            self.main_menu = False
            try:
                self.director.change_scene(self.director.scene_dict['scene_main_menu'])
            except Exception:
                print 'Imposible cambiar de escena'

        # Checking samus if out of lifes to end
        if self.samus.lifes < 1:
            self.director.quit()
# ----------------------------------------------------------------------------------------------------------------------


# Drawing
# ----------------------------------------------------------------------------------------------------------------------
    def on_draw(self, screen):
        screen.fill(BGCOLOR)

        if DEBUG:
        # ------------- DEBUG SECTION -------------
            pg.draw.circle(screen, RED, self.samus.rect.center, self.samus.radius)
            for mob in self.mobs:
                pg.draw.circle(screen, RED, mob.rect.center, mob.radius)
            for shot in self.samus.shots:
                pg.draw.circle(screen, RED, shot.rect.center, shot.radius)

            load_text(screen, "pos: " + str(self.samus.pos), SCREEN_WIDTH-200, 30, size=15)
            load_text(screen, "vel: " + str(self.samus.vel), SCREEN_WIDTH-200, 50, size=15)
            load_text(screen, "acc: " + str(self.samus.acc), SCREEN_WIDTH-200, 70, size=15)
        # ------------- DEBUG SECTION -------------

        # - Inv samus
        if self.samus.invulnerable:
            pg.draw.rect(screen, BLUE, self.samus.rect)

        # - Sprites
        self.sprites.draw(screen)
        self.draw_UI(screen)

    def draw_UI(self, screen):
        load_text(screen, "move left: A", 30, 30, size=15)
        load_text(screen, "move right: D", 30, 60, size=15)
        load_text(screen, "jump: space", 30, 90, size=15)
        load_text(screen, "shot: mouse_left", 30, 120, size=15)
        load_text(screen, "change ammo: mouse_right", 30, 150, size=15)
        load_text(screen, "run: left shift", 30, 180, size=15)
        load_text(screen, "ammo: " + self.samus.ammo_type, self.samus.rect.right, self.samus.rect.y-20, size=15)
        load_text(screen, "lifes: " + str(self.samus.lifes), self.samus.rect.right, self.samus.rect.y, size=15)
# ----------------------------------------------------------------------------------------------------------------------


# Generators
# ----------------------------------------------------------------------------------------------------------------------
    def generate_samus(self):
        self.samus = Samus(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, self)
        self.sprites.add(self.samus)

    def generate_structures(self):
        self.ground = Structure(-600, SCREEN_HEIGHT - 40, SCREEN_WIDTH + 5000, 40, self)
        self.sprites.add(self.ground)
        self.structures.add(self.ground)
        self.platform_1 = Structure(SCREEN_WIDTH/2, SCREEN_HEIGHT/2, 100, 15, self)
        self.sprites.add(self.platform_1)
        self.structures.add(self.platform_1)

    def generate_mobs(self):
        for i in range(4):
            m = Mob()
            self.sprites.add(m)
            self.mobs.add(m)

# ----------------------------------------------------------------------------------------------------------------------


# Music
# ----------------------------------------------------------------------------------------------------------------------
    @staticmethod
    def set_music():
        pg.mixer.stop()

        # pg.mixer.music.load(APPEAR_JINGLE)
        # pg.mixer.music.play()

        pg.mixer.music.load(AREA_1_MUSIC)
        pg.mixer.music.play(-1)
# ----------------------------------------------------------------------------------------------------------------------