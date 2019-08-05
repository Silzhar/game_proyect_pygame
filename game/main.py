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

        self.initialScreen = PG.display.set_mode((1020, 680)) 
        self.backgroundInitial = PG.image.load('E&A relieve color.jpg')
        self.initialScreen = self.backgroundInitial
    

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
        
        
        
    def Collisions(self, direction):
        self.collisionWallsSprite = PG.sprite.Group()
        self.collisionWallsSprite.add(self.wallsSprite)
        self.collisionPlayer = PG.sprite.Group()
        self.collisionPlayer.add(self.player)
        
        '''
        for self.collisionPlayer in self.collisionWallsSprite:
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
                    self.rect.y += 0   '''

                    
    def reStart(self):
        
        self.screen.blit(self.background, (0, 0))

        self.screen.blit(self.wallsSprite.image, self.wallsSprite.rect)    
        self.screen.blit(self.player.image, self.player.rect)

        PG.display.flip()  # update all game screen
        self.clock.tick(20)

                   
  
    def start(self):
        self.game_over = False
        self.game_started = False
        
        while self.game_over == False:
            for event in PG.event.get():
                if event.type == PG.QUIT:
                    self.game_over = True
                    PG.quit()
                    sys.exit()

            if event.type == PG.KEYDOWN:
                if event.key == PG.K_SPACE:
                    if self.game_started == False:
                        self.reStart()
                        self.game_started = True
                



            if self.Collisions(self.player.update):
                direction = self.player.handle_event
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

        #    PG.sprite.pygame.sprite.spritecollide(self.player,self.wallsSprite, False, collided = None)
            self.player.update(self.Collisions(self.player))  
            self.player.handle_event(event) 
                
        
          
            
            PG.surface.blit(self.initialScreen)
            self.reStart()
                
            PG.display.flip()  # update all game screen
            self.clock.tick(20)
                    
        

if __name__ == '__main__':
    PG.init()
    game = Game()
    game.start()
