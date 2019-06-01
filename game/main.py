import pygame, sys
import textwrap
from pygame.locals import *

pygame.init()


class Executus():
    __customes= ("Executus")
    
    def __init__(self, x=0, y= 0):
        self.custome = pygame.image.load("executus.png")
        self.position = [x, y]
    

class Game():   
    __name = ("Executus")
    moveX = 0
    moveY = 0

    
    def __init__(self):
        self.__screen = pygame.display.set_mode((1040, 704))
        self.__background = pygame.image.load('indoor.png')
        pygame.display.set_caption("Executus time !")
        pygame.key.set_repeat(1,8)  # automatic move 
        
        self.executus = Executus(320, 240)
        
        
    def start(self):
        gameOver = False
        while not gameOver:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    keys = pygame.key.get_pressed()
                    if keys[pygame.K_UP]:
                        self.executus.position[1] -= 4
                                
                    elif keys[pygame.K_DOWN]:
                        self.executus.position[1] += 4
                                
                    elif keys[pygame.K_LEFT]:
                        self.executus.position[0] -= 4
                                
                    elif keys[pygame.K_RIGHT]:
                        self.executus.position[0] += 4
                                
                    else:
                        pass
                    

            
        
            self.__screen.blit(self.__background, (0, 0)) # refresh background
            self.__screen.blit(self.executus.custome, self.executus.position)
            
            pygame.display.flip()
            

            
            
if __name__ =='__main__':
    game = Game()
    pygame.font.init()
    game.start()