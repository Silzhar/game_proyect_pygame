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
        
        self.executusMeow = pygame.mixer.Sound('Cat_Meow.wav')
    
             
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
        
        
        
    def Collisions(self):  # is near !! search where it donesn't connect whith the debugger
        direction = 0
        
        self.collisionWallsSprite = pygame.sprite.Group()
        self.collisionWallsSprite.add(self.wallsSprite)
        self.collisionPlayer = pygame.sprite.Group()
        self.collisionPlayer.add(self.player)   
        self.shock = pygame.sprite.groupcollide(self.collisionPlayer, self.collisionWallsSprite,False,False, collided=None)
        if self.shock:
            if self.player.update:
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
                    
        return self.shock
                   
  
    def start(self):
        self.game_over = False
        
        while self.game_over == False:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game_over = True
                    pygame.quit()
                    sys.exit()
             
            
            self.Collisions()
            self.player.update(self.Collisions())   
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
    
'''

        
    def Pause(self, event):
        width_window = 1020
        height_window = 680
        
        self.pauseScreen = pygame.display.set_mode((width_window, height_window)) 
        self.backgroundPause = pygame.image.load('E&A relieve color.jpg')
        self.fontPause = pygame.font.Font('font.ttf', 48)
        self.fontPause.render("- PAUSE -",1,(255, 255, 0))
        
         self.Pause(pygame.K_SPACE)  
        
        '''