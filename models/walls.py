import pygame


class Walls(pygame.sprite.Sprite):
    def __init__(self, position):
        pygame.sprite.Sprite.__init__(self)
        self.green = (0,   255,   0)
        self.rect1 = pygame.Rect(12, 60, 981, 60)
        self.imageRect1 = pygame.draw.rect(self.screen,self.green, self.rect1, 1)
        self.rect2 = pygame.draw.rect(self.screen,self.green, (200, 130, 84, 184), 1)