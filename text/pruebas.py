import pygame , sys
from pygame.locals import *
import pygame.event as GAME_EVENTS


class Executus(pygame.sprite.Sprite):
    def __init__(self, position):
        pygame.sprite.Sprite.__init__(self)  
        self.sheet = pygame.image.load('spliteCat.png')
        self.sheet.set_clip(pygame.Rect(0, 0, 30, 30))  # visual box of sprite
        self.image = self.sheet.subsurface(self.sheet.get_clip())
        self.rect = self.image.get_rect()
        self.rect.topleft = position
        self.frame = 0

        self.X = 100
        self.Y = 140
        self.positionPlayer = (self.X, self.Y)
        
        
        # tour the sprite in frames to create animation                                       
        self.right_states = { 0: ( 0, 0, 30, 28 ), 1: (32 , 0, 30, 28), 2: (64 , 0, 30, 28)}
        self.up_states = { 0: ( 0, 30, 30, 30 ), 1: (32 , 30, 30, 30), 2: (64 , 30, 30, 30)}
        self.down_states = { 0: ( 0, 60, 30, 30 ), 1: (32 , 60, 30, 30), 2: (64 , 60, 30, 30)}
        self.left_states = { 0: ( 0, 90, 30, 50 ), 1: (32 , 90, 30, 50), 2: (64 , 90, 30, 50)}
        #   ( 0, 0, 50, 30 )    pos y , pos x, large ,alt

    def get_frame(self, frame_set):
        self.frame += 1
        if self.frame > (len(frame_set) - 1):
            self.frame = 0
        return frame_set[self.frame]


    def clip(self, clipped_rect):
        if type(clipped_rect) is dict:
            self.sheet.set_clip(pygame.Rect(self.get_frame(clipped_rect)))
        else:
            self.sheet.set_clip(pygame.Rect(clipped_rect))
        return clipped_rect


    def update(self, direction):       
        if direction == 'left':
            self.clip(self.left_states)
            self.rect.x -= 4
        if direction == 'right':
            self.clip(self.right_states)
            self.rect.x += 4
        if direction == 'up':
            self.clip(self.up_states)
            self.rect.y -= 4
        if direction == 'down':
            self.clip(self.down_states)
            self.rect.y += 4

        if direction == 'stand_left':
            self.clip(self.left_states[0])
        if direction == 'stand_right':
            self.clip(self.right_states[0])
        if direction == 'stand_up':
            self.clip(self.up_states[0])
        if direction == 'stand_down':
            self.clip(self.down_states[0])

        self.image = self.sheet.subsurface(self.sheet.get_clip())


class Game(pygame.sprite.Sprite):
    
    def __init__(self): 
        width_window = 1040
        height_window = 704
        
        
        pygame.mixer.init()
        pygame.mixer.music.load('gameLoops.mp3')   #  background music
        pygame.mixer.music.play(-1)
        
        self.executusMeow = pygame.mixer.Sound('Cat_Meow.wav')    #  cat sound
    

        # GAME SCREEN  
        self.screen = pygame.display.set_mode((width_window, height_window))   
        self.background = pygame.image.load('indoor.png')
        pygame.display.set_caption("Executus time !")
        self.clock = pygame.time.Clock() 
  
        
        self.wallsBg = pygame.image.load('walls.png')
        self.wallsSprite = pygame.sprite.Sprite()
        self.wallsSprite.image = self.wallsBg
        self.wallsSprite.rect = self.wallsBg.get_rect()
        self.Xwalls = 520
        self.Ywalls = 352
        self.positionWalls = (self.Xwalls, self.Ywalls)
        
        self.player = Executus((width_window/10, height_window/4))


        
        
                  
  
    def start(self):
        self.game_over = False 
      #  self.player.update
        direction = self.player
        
        self.collisionWallsSprite = pygame.sprite.Group()
        self.collisionWallsSprite.add(self.wallsSprite)
    #    self.collisionPlayer = pygame.sprite.Group()
    #    self.collisionPlayer.add(self.player)

        self.spriteList = pygame.sprite.Group()
        self.shock = pygame.sprite.spritecollide(self.player, self.collisionWallsSprite, False, collided = None) # collided = None
        

        while self.game_over == False:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game_over = True
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_LEFT:
                        self.update('left')
                    if event.key == pygame.K_RIGHT:
                        self.update('right')
                    if event.key == pygame.K_UP:
                        self.update('up')
                    if event.key == pygame.K_DOWN:
                        self.update('down')
                    
                if event.type == pygame.KEYUP:

                    if event.key == pygame.K_LEFT:
                        self.update('stand_left')
                    if event.key == pygame.K_RIGHT:
                        self.update('stand_right')
                    if event.key == pygame.K_UP:
                        self.update('stand_up')
                    if event.key == pygame.K_DOWN:
                        self.update('stand_down')


            

    

            if self.shock :
                print("colision")

        #    self.Executus.handle_event(event)
            
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
