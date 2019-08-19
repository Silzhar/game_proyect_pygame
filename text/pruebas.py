
import pygame as PG, sys
import player
from pygame.locals import *
import pygame.event as GAME_EVENTS



class Walls(PG.sprite.Sprite):
    def __init__(self, positionWall): 
        PG.sprite.Sprite.__init__(self)
        game = Game
        game.Collisions == False

        self.wallsBg = PG.image.load('walls.png')
        self.wallsSprite = PG.sprite.Sprite()
        self.wallsSprite.image = self.wallsBg
        self.wallsSprite.rect = self.wallsBg.get_rect()

        eventWalls = PG.event.poll()
        if eventWalls.type  == PG.ACTIVEEVENT:
            game.Collisions == True

        


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
        

        self.walls = Walls((width_window, height_window))
        
        
        
        self.wallsBg = PG.image.load('walls.png')
        self.wallsSprite = PG.sprite.Sprite()
        self.wallsSprite.image = self.wallsBg
        self.wallsSprite.rect = self.wallsBg.get_rect()   
        
        
      
    def Collisions(self, player, walls):
        self.collisionWallsSprite = PG.sprite.Group()
        self.collisionWallsSprite.add(self.walls.wallsSprite)
    #    self.collisionPlayer = PG.sprite.Group()
     #   self.collisionPlayer.add(self.player)

        self.spriteList = PG.sprite.Group()
        self.shock = PG.sprite.pygame.sprite.spritecollide(self.player, self.collisionWallsSprite, False) # collided = None
       
          



                         
  
    def start(self):
        self.game_over = False
        
        while self.game_over == False:
            for event in PG.event.get():
                if event.type == PG.QUIT:
                    self.game_over = True
                    PG.quit()
                    sys.exit()

                direction = self.player.handle_event(self.walls)  # repair 
                for self.player in self.shock: # go throug !
                    print("colision !!!!!!!")
                    if self.player == direction:        # .update
                        if self.shock == True:
                            if PG.KEYDOWN: 
                                if self.player.update: 
                                    if self.player == 'left':
                                        self.clip(self.left_states)
                                        self.rect.x -= 0
                                    if self.player  == 'right':
                                        self.clip(self.right_states)
                                        self.rect.x += 0
                                    if self.player == 'up':
                                        self.clip(self.up_states)
                                        self.rect.y -= 0
                                    if self.player  == 'down':
                                        self.clip(self.down_states)
                                        self.rect.y += 0 

        #    if (self.player.colliderect(self.wallsSprite.rect)):
                      
            
            
      #      self.Collisions(self.player, self.walls)
      #      self.player.update(self.Collisions(self.player, self.walls))   
            self.player.handle_event(event)
            self.screen.blit(self.background, (0, 0))    
        
          
            self.screen.blit(self.wallsSprite.image, self.walls.wallsSprite.rect)  # draw walls
            self.screen.blit(self.player.image, self.player.rect)
 
        
                
            PG.display.flip()
            self.clock.tick(20)
                    
        

if __name__ == '__main__':
    PG.init()
    game = Game()
    game.start()

'''


class Collisions(pygame.sprite.Sprite):  # is near !! search where it donesn't connect whith the debugger

    def __init__(self):
        width_window = 1040
        height_window = 704
        direction = 0

        self.player = player.Executus((width_window/10, height_window/4))
        self.player.update 

        self.wallsBg = pygame.image.load('walls.png')
        self.wallsSprite = pygame.sprite.Sprite()
        self.wallsSprite.image = self.wallsBg
        self.wallsSprite.rect = self.wallsBg.get_rect()
        
        self.collisionWallsSprite = pygame.sprite.Group()
        self.collisionWallsSprite.add(self.wallsSprite)
        self.collisionPlayer = pygame.sprite.Group()
        self.collisionPlayer.add(self.player) 

        self.shock = pygame.sprite.groupcollide(self.collisionPlayer, self.collisionWallsSprite,False,False, collided=None)

    

        if self.shock :
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
        
        
        def ScreenPresentation(self):
            width_window = 1020
            height_window = 680   

        
        self.initialScreen = pygame.display.set_mode((1020, 680)) 
        self.backgroundInitial = pygame.image.load('E&A relieve color.jpg')
        pygame.display.set_caption("PLAY !")
        self.clock = pygame.time.Clock()
        self.fontInitial = pygame.font.Font('font.ttf', 48)
        self.fontInitial.render("- PAUSE -",1,(255, 255, 0))   


    def handle_eventInital(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                sys.exit()
        
        
        
                   
  
    def start(self):
        self.game_over = False      

        while self.game_over == False:
            for event in pygame.event.get():  
                if event.type == pygame.QUIT:
                    self.game_over = True
                    pygame.quit()
                    sys.exit()


            
            Collisions()
            self.player.update(Collisions())  

            self.player.handle_event(event)
            self.screen.blit(self.background, (0, 0))    

            
            self.screen.blit(self.wallsSprite.image, self.wallsSprite.rect)    
            self.screen.blit(self.player.image, self.player.rect)
         #   self.initialScreen.blit(self.backgroundInitial, (80,80))
 
        
                
            pygame.display.flip()
            self.clock.tick(20)
                    
        

if __name__ == '__main__':
    pygame.init()
    game = Game()
    collisions = Collisions()
    game.start()
    


        
    def Pause(self, event):
        width_window = 1020
        height_window = 680
        
        self.pauseScreen = pygame.display.set_mode((width_window, height_window)) 
        self.backgroundPause = pygame.image.load('E&A relieve color.jpg')
        self.fontPause = pygame.font.Font('font.ttf', 48)
        self.fontPause.render("- PAUSE -",1,(255, 255, 0))
        
         self.Pause(pygame.K_SPACE)  
        
        '''

'''

    def reStart(self):
        
        self.screen.blit(self.background, (0, 0))

        self.screen.blit(self.wallsSprite.image, self.wallsSprite.rect)    
        self.screen.blit(self.player.image, self.player.rect)

        PG.display.flip()  # update all game screen
        self.clock.tick(20)

        if event.type == PG.KEYDOWN:
                if event.key == PG.K_SPACE:
                    if self.game_started == False:
                        self.reStart()
                        self.game_started = True

'''
