import pygame

class Map(pygame.sprite.Sprite):
    def __init__(self, position):
        self.sheet = pygame.image.load('walls.png')
        self.sheet.set_clip(pygame.Rect(0, 0, 130, 130))
        self.image = self.sheet.subsurface(self.sheet.get_clip())
        self.rect = self.image.get_rect()
        self.rect.topleft = position
        self.frame = 0


    
        