
import pygame

import settings


class Bottle(pygame.sprite.Sprite):
    def __init__(self, position):
        pygame.sprite.Sprite.__init__(self)
        bottleOne = pygame.image.load("{0}{1}".format(settings.ASSETS_PATH, "bottle.png"))
        self.image = pygame.transform.scale(bottleOne, (12, 30))
        self.rect = self.image.get_rect()
        # take the coordinates of the rect (upper left corner)
        self.rect.topleft = position

    def update(self):
        newPossition = self.rect.topleft
        return newPossition
