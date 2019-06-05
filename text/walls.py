import pygame

pygame.init()

class Walls(pygame.sprite.Sprite):
    def __init__(self, position):
        self.wall = pygame.Color("white")
        

    def status(self, positions):        
        self.height = 53
        self.width = 495
        self.x = 492
        self.y = 529
        