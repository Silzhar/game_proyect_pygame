import pygame as PG, sys
import player
from pygame.locals import *
import pygame.event as GAME_EVENTS



class Game(PG.sprite.Sprite):
    
    def __init__(self): 
        width_window = 1040
        height_window = 704
 
        
        PG.mixer.init()
        PG.mixer.music.load('gameLoops.mp3')   #  background music
        PG.mixer.music.play(-1)
        
        self.executusMeow = PG.mixer.Sound('Cat_Meow.wav')    #  cat sound
    

        # GAME SCREEN  
        self.screen = PG.display.set_mode((width_window, height_window))   
        self.background = PG.image.load('indoor.png')
        PG.display.set_caption("Executus time !")
        self.clock = PG.time.Clock() 

        self.player = player.Executus((width_window/10, height_window/4))
        self.player.update  
        

        self.wallsBg = PG.image.load('walls.png')
        self.wallsSprite = PG.sprite.Sprite()
        self.wallsSprite.image = self.wallsBg
        self.wallsSprite.rect = self.wallsBg.get_rect()
        
        
        
#    def Collisions(self, direction):
        
        
        
                   
  
    def start(self):
        self.game_over = False
        
        
        self.collisionWallsSprite = PG.sprite.Group()
        self.collisionWallsSprite.add(self.wallsSprite)
        self.collisionPlayer = PG.sprite.Group()
        self.collisionPlayer.add(self.player)

        self.spriteList = PG.sprite.Group()
        self.shock = PG.sprite.spritecollide(self.player, self.collisionWallsSprite, False, collided = None) # collided = None
        

        while self.game_over == False:
            for event in PG.event.get():
                if event.type == PG.QUIT:
                    self.game_over = True
                    PG.quit()
                    sys.exit()
            

            if self.shock :
                print("colision")

            self.player.handle_event(event)
            self.screen.blit(self.background, (0, 0))    
        
            
            self.screen.blit(self.wallsSprite.image, self.wallsSprite.rect)    
            self.screen.blit(self.player.image, self.player.rect)
 
        
                
            PG.display.flip()
            self.clock.tick(20)
                    
        

if __name__ == '__main__':
    PG.init()
    game = Game()
    game.start()
   
            
            

'''
(self.player.left_states, self.player.topleft) = self.player.handle_event(event)
(xAnt, yAnt) = (self.player.left_states, self.player.right_states)

if self.player.spritecollide(self.wallsSprite.rect):
    (self.player.left_states, self.player.topleft) = (xAnt, yAnt)   '''