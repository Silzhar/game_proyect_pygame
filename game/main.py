import pygame, sys
import textwrap
from pygame.locals import *


class Executus():
    __customes= ("Executus")
    
    def __init__(self, x=0, y= 0):
        self.custome = pygame.image.load("executus.png")
        self.position = [x, y]
    

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
        
        self.executus = Executus()
        
        

        
        self.__screen.blit(self.__background, (0, 0)) # refresh background
        self.__screen.blit(self.executus.custome, self.executus.position)
        
        pygame.display.flip()

        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()



              
            
if __name__ =='__main__':
    game = Game()
    pygame.font.init()
    