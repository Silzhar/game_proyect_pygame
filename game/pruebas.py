import pygame, sys
import textwrap
from pygame.locals import *

pygame.init()
windowText = pygame.display.set_mode((400,300))
pygame.display.set_caption("text")


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
        

    def intro(self):
        myFont = pygame.font.Font(None, 30)
        myText = myFont.render("Miles de años llevan los gatos preparando la conquista del planeta.\n"
                                "Han sido laboriosos los esfuerzos por encontrar las debilidades de otras espécies\n"
                                "Después de la reunión del Clan de la Zarpa de este año salieron dos conclusiones\n"
                                "1:Se determina el comienzo para someter a la raza humana\n"
                                "2:Los designados para el comienzo de tal función son Executus y Apocalipsis",0,(200,60,80),(80,80,10)) 
                                # (100,70,120)  background color 
        rectText = myText.get_rect()
        rectText.centerx = windowText.get_rect().centerx
        rectText.centery = 520        

        
        self.__screen.blit(self.__background, (0, 0)) # refresh background
        
        pygame.display.flip()

        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                        

            windowText.blit(myText,(100,100))
            pygame.display.update()


              
            
if __name__ =='__main__':
    game = Game()
    pygame.font.init()
    