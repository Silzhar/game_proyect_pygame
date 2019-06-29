import pygame , sys
import player
#import walls 
from pygame.locals import *


class Game(pygame.sprite.Sprite):
    
    def __init__(self): 
        width_window = 1040
        height_window = 704
             
        self.screen = pygame.display.set_mode((width_window, height_window))
        self.background = pygame.image.load('indoor.png')
        pygame.display.set_caption("Executus time !")
        self.clock = pygame.time.Clock() 

        self.player = player.Executus((width_window/10, height_window/4))

        self.wallsBg = pygame.image.load('walls.png')
        self.wallsSprite = pygame.sprite.Sprite()
        self.wallsSprite.image = self.wallsBg
        self.wallsSprite.rect = self.wallsBg.get_rect()
        
        

#wallsLimits = walls.Limits((0, 0))
#wallsLimits = walls
#wallsLimits = pygame.sprite.Sprite()
# wallsLimits = walls.get_rect()


#collisions = pygame.sprite.collide_rect(self.wallsSprite, player)

    
    def start(self):
        self.game_over = False
        
        while self.game_over == False:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game_over = True
                    pygame.quit()
                    sys.exit()
                    
            
           # walls.Limits((0, 0))            
            self.player.handle_event(event)
            self.screen.blit(self.background, (0, 0))    # screen.blit(walls, (0, 0))
        
           # screen.blit(walls, walls.rect)
            self.screen.blit(self.wallsSprite.image, self.wallsSprite.rect)    
            self.screen.blit(self.player.image, self.player.rect)
            
           # if collisions == True :
            #    player.update( player) == None
        
                
            pygame.display.flip()
            self.clock.tick(20)
                    
        

if __name__ == '__main__':
    pygame.init()
    game = Game()
    game.start()

    
