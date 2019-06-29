import pygame , sys
import player
import walls 
from pygame.locals import *


class Game(pygame.sprite.Sprite):
    
    def __init__(self, position): 
        width_window = 1040
        height_window = 704
             
        self.screen = pygame.display.set_mode((width_window, height_window))
        self.background = pygame.image.load('indoor.png')
        pygame.display.set_caption("Executus time !")
        self.clock = pygame.time.Clock() 

        player = player.Executus((width_window/10, height_window/4))


wallsBg = pygame.image.load('walls.png')
wallsSprite = pygame.sprite.Sprite()
wallsSprite.image = wallsBg
wallsSprite.rect = wallsBg.get_rect()

#wallsLimits = walls.Limits((0, 0))
wallsLimits = walls
wallsLimits = pygame.sprite.Sprite()
# wallsLimits = walls.get_rect()


collisions = pygame.sprite.collide_rect(wallsSprite, player)


def start(self):
    game_over = False
    
    while game_over == False:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
        
       # walls.Limits((0, 0))            
        player.handle_event(event)
        self.screen.blit(self.background, (0, 0))    # screen.blit(walls, (0, 0))
    
       # screen.blit(walls, walls.rect)
        self.screen.blit(wallsSprite.image, wallsSprite.rect)    
        self.screen.blit(player.image, player.rect)
        
        if collisions == True :
            player.update( player) == None
    
                    
        pygame.display.flip()
        self.clock.tick(20)
                    
    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    pygame.init()
    game = Game()
    game.start()
    
