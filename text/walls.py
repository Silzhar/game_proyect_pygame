import pygame

pygame.init()

class Walls(pygame.sprite.Sprite):
    def __init__(self, position):
        self.wall = pygame.Color("white")
        

    def dimensions(self, limits):
        wall1 = pygame.draw.poligon(self.wall, )
        
        
        self.height = 53
        self.width = 495
        self.x = 492
        self.y = 529
        