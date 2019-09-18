import random

import pygame

import settings

# Brooms  create the class for moving enemies

class Brooms(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.width_window = 1040
        self.height_window = 704

        broom = pygame.image.load("{0}{1}".format(settings.ASSETS_PATH, "broom.png"))
        self.imageOrigin = pygame.transform.scale(broom, (13, 32))
        self.image = self.imageOrigin.copy()
        self.rect = self.image.get_rect()
        self.radius = int(self.rect.width*0.9/2)

        self.rect.x = random.randrange(0, self.width_window-8)
        self.rect.y = random.randrange(100, self.height_window-400)
        self.speedBrooms = random.randrange(1, 4)
        self.rot = 0

        self.rot_speed = random.randrange(-8, 8)
        self.last_update = pygame.time.get_ticks()

    def rotation(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > 50:
            self.last_update = now
            self.rot += (self.rot_speed) % 360
            new_img = pygame.transform.rotate(self.imageOrigin, self.rot)
            oldCenter = self.rect.center
            self.image = new_img
            self.rect = self.image.get_rect()
            self.rect.center = oldCenter

    def update(self):  # This will be used to move the object.
        self.rotation()
        self.rect.y += self.speedBrooms
        if self.rect.y > self.height_window:
            self.rect.x = random.randrange(0, self.width_window-500)
            self.rect.y = random.randrange(-100, -40)
            self.speedBrooms = random.randrange(1, 4)
