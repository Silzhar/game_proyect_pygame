import pygame

import settings
from models.enemies import Brooms


class Executus(pygame.sprite.Sprite):
    def __init__(self, position):  # initialize all the variables
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("{0}{1}".format(settings.ASSETS_PATH, "gus 2.png"))
        self.rect = self.image.get_rect()
        self.radius = 21

        self.shield = 100
        self.player_lives = 3
        self.hidden = False
        self.hide_timer = pygame.time.get_ticks()

        self.width_window = 1040
        self.height_window = 704
        self.rect.center = (self.width_window/2, self.height_window-48)

        self.knockSound = pygame.mixer.Sound("{0}{1}".format(settings.ASSETS_PATH, "swoosh.wav"))
        self.broomHit = pygame.mixer.Sound("{0}{1}".format(settings.ASSETS_PATH, "wail_cat.wav"))

        self.sheet = pygame.image.load("{0}{1}".format(settings.ASSETS_PATH, "spliteCat.png"))
        self.sheet.set_clip(pygame.Rect(0, 0, 30, 30))  # visual box of sprite
        self.image = self.sheet.subsurface(self.sheet.get_clip())
        self.rect = self.image.get_rect()

        self.frame = 0
        self.radius = 21
        self.rect.center = (self.width_window/2, self.height_window-48)

        self.shield = 100
        self.player_lives = 3
        self.hidden = False
        self.hide_timer = pygame.time.get_ticks()

        # Tour the sprite in frames to create animation.
        self.right_states = {0: (0, 0, 30, 28), 1: (32, 0, 30, 28), 2: (64, 0, 30, 28)}
        self.up_states = {0: (0, 30, 30, 30), 1: (32, 30, 30, 30), 2: (64, 30, 30, 30)}
        self.down_states = {0: (0, 60, 30, 30), 1: (32, 60, 30, 30), 2: (64, 60, 30, 30)}
        self.left_states = {0: (0, 90, 30, 50), 1: (32, 90, 30, 50), 2: (64, 90, 30, 50)}
        #   ( 0, 0, 50, 30 )    pos y , pos x, large ,alt


    def knock(self):  # Use this to knock bottles.
        self.knockSound.play()

    def hide(self):  # Use this to hide the player temporarily (dead).
        self.hidden = True
        self.hide_timer = pygame.time.get_ticks()
        self.rect.center = (self.width_window/2, self.height_window + 200)

    def get_frame(self, frame_set):
        self.frame += 1
        if self.frame > (len(frame_set) - 1):
            self.frame = 0
        return frame_set[self.frame]

    def clip(self, clipped_rect):
        if type(clipped_rect) is dict:
            self.sheet.set_clip(pygame.Rect(self.get_frame(clipped_rect)))
        else:
            self.sheet.set_clip(pygame.Rect(clipped_rect))
        return clipped_rect

    # we will use this class to add movement to the player

    def update(self, direction):
        if direction == 'left':
            self.clip(self.left_states)
            self.rect.x -= 4
        if direction == 'right':
            self.clip(self.right_states)
            self.rect.x += 4
        if direction == 'up':
            self.clip(self.up_states)
            self.rect.y -= 4
        if direction == 'down':
            self.clip(self.down_states)
            self.rect.y += 4

        if direction == 'stand_left':
            self.clip(self.left_states[0])
        if direction == 'stand_right':
            self.clip(self.right_states[0])
        if direction == 'stand_up':
            self.clip(self.up_states[0])
        if direction == 'stand_down':
            self.clip(self.down_states[0])

        self.image = self.sheet.subsurface(self.sheet.get_clip())
        if self.hidden and pygame.time.get_ticks() - self.hide_timer > 1000:
            self.hidden = False
            self.rect.center = (self.width_window/2, self.height_window-48)

    def handle_event(self, event):
        if event.type == pygame.QUIT:
            pass

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_LEFT:
                self.update('left')
            if event.key == pygame.K_RIGHT:
                self.update('right')
            if event.key == pygame.K_UP:
                self.update('up')
            if event.key == pygame.K_DOWN:
                self.update('down')

        if event.type == pygame.KEYUP:

            if event.key == pygame.K_LEFT:
                self.update('stand_left')
            if event.key == pygame.K_RIGHT:
                self.update('stand_right')
            if event.key == pygame.K_UP:
                self.update('stand_up')
            if event.key == pygame.K_DOWN:
                self.update('stand_down')
