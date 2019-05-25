import pygame, sys
import random
import textwrap


class Game():
    players = []
    __init = (40) # start position 
    __names = ("Executus")
    __startLine = 4
    __finishLine = 620
    
    def __init__(self):
        self.__screen = pygame.display.set_mode((1040, 704))
        self.__background = pygame.image.load('indoor.png')
        pygame.display.set_caption("Executus time !")
        
        
        
        
        self.__screen.blit(self.__background, (0, 0)) # refresh background
        
        pygame.display.flip()
    
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()    
    
    
if __name__ =='__main__':
    game = Game()
    pygame.font.init()