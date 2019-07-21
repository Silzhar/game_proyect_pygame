import pygame , sys
import player
from pygame.locals import *


class Game(pygame.sprite.Sprite):
    
    def __init__(self): 
        width_window = 1040
        height_window = 704
        
        pygame.mixer.init()
        pygame.mixer.music.load('gameLoops.mp3')
        pygame.mixer.music.play(-1)
    
             
        self.screen = pygame.display.set_mode((width_window, height_window))
        self.background = pygame.image.load('indoor.png')
        pygame.display.set_caption("Executus time !")
        self.clock = pygame.time.Clock() 

        self.player = player.Executus((width_window/10, height_window/4))
        self.player.update  
        

        self.wallsBg = pygame.image.load('walls.png')
        self.wallsSprite = pygame.sprite.Sprite()
        self.wallsSprite.image = self.wallsBg
        self.wallsSprite.rect = self.wallsBg.get_rect()
        
        
        
    def Collisions(self, direction):
        self.collisionWallsSprite = pygame.sprite.Group()
        self.collisionWallsSprite.add(self.wallsSprite)
        self.collisionPlayer = pygame.sprite.Group()
        self.collisionPlayer.add(self.player)
        
        while self.collisionPlayer in self.collisionWallsSprite:
            if self.player.update == direction:
                if direction == 'left':
                    self.clip(self.left_states)
                    self.rect.x -= 0
                if direction == 'right':
                    self.clip(self.right_states)
                    self.rect.x += 0
                if direction == 'up':
                    self.clip(self.up_states)
                    self.rect.y -= 0
                if direction == 'down':
                    self.clip(self.down_states)
                    self.rect.y += 0
                    
        
                   
  
    def start(self):
        self.game_over = False
        
        while self.game_over == False:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game_over = True
                    pygame.quit()
                    sys.exit()
                    
            self.Collisions(self.player.update )
            self.player.update(self.Collisions(self.player))   
            self.player.handle_event(event)
            self.screen.blit(self.background, (0, 0))    
        
          
            self.screen.blit(self.wallsSprite.image, self.wallsSprite.rect)    
            self.screen.blit(self.player.image, self.player.rect)
 
        
                
            pygame.display.flip()
            self.clock.tick(20)
                    
        

if __name__ == '__main__':
    pygame.init()
    game = Game()
    game.start()
