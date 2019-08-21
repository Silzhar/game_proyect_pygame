import pygame as  sys
# import player
from pygame.locals import *
import pygame.event as GAME_EVENTS


import pygame
import text2

class Executus(pygame.sprite.Sprite):
    def __init__(self, position):
        pygame.sprite.Sprite.__init__(self)
        self.sheet = pygame.image.load('spliteCat.png')
        self.sheet.set_clip(pygame.Rect(0, 0, 30, 30))  # visual box of sprite
        self.image = self.sheet.subsurface(self.sheet.get_clip())
        self.rect = self.image.get_rect()
        self.rect.topleft = position
        self.frame = 0

        
       
         
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
            self.rect.x -= 8
        if direction == 'right':
            self.clip(self.right_states)
            self.rect.x += 8
        if direction == 'up':
            self.clip(self.up_states)
            self.rect.y -= 8
        if direction == 'down':
            self.clip(self.down_states)
            self.rect.y += 8

        if direction == 'stand_left':
            self.clip(self.left_states[0])
        if direction == 'stand_right':
            self.clip(self.right_states[0])
        if direction == 'stand_up':
            self.clip(self.up_states[0])
        if direction == 'stand_down':
            self.clip(self.down_states[0])

        self.image = self.sheet.subsurface(self.sheet.get_clip())


    def move(self,xMove ,yMove):
        self.eventMove = xMove ,yMove
        self.rect.move_ip(self.eventMove)

        '''
        xMove = 4 
        yMove = 4
        self.eventMove = xMove ,yMove
        self.rect.move_ip(self.eventMove)   '''


    def updateImage(self,playerSurface):
        playerSurface.blit(self.image ,self.rect)   

    
    def collision(self,player, shocks):
        for shockPlayer in self.collisionWallsSprite:
            if Executus.rect.colliderect(shockPlayer):
                return True
        return False


class Broom(pygame.sprite.Sprite):
    def __init__(self, position):
        pygame.sprite.Sprite.__init__(self)
        self.sheetBroom = pygame.image.load('broonGame.png')
        self.sheetBroom.set_clip(pygame.Rect(0, 0, 13, 32)) # box of broom / crop image
        self.imageBroom = self.sheetBroom.subsurface(self.sheetBroom.get_clip())
        self.rect = self.imageBroom.get_rect()
        self.rect.topleft = position
        self.frame = 0

        # tour the sprite in frames to create animation                                       
        self.right_states = { 0: ( 0, 0, 13, 32 ), 1: (0 , 0, 13, 32)}  #, 2: (24 , 0, 4, 8)
        self.left_states = { 0: ( 0, 13, 13, 32 ), 1: (0 , 13, 13, 32)}  #, 2: (64 , 90, 30, 50)
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

        self.player = Executus((width_window/10, height_window/4))
        self.player.update  

        self.enemy = Broom((width_window/3, height_window/4))
        self.enemy.update
        
        self.wallsBg = pygame.image.load('walls.png')
        self.wallsSprite = pygame.sprite.Sprite()
        self.wallsSprite.image = self.wallsBg
        self.wallsSprite.rect = self.wallsBg.get_rect()
        self.Xwalls = 520
        self.Ywalls = 352
        self.positionWalls = (self.Xwalls, self.Ywalls)
        
        

        
        
                   
  
    def start(self):
        self.game_over = False

        self.shock = False

        self.leftPress = False
        self.rightPress = False
        self.upPress = False
        self.downPress = False


     #   self.player.rect = self.player.image.get_rect()
     #   self.player.rect.top = 100
     #   self.player.rect.left = 140
        
        
        self.collisionWallsSprite = pygame.sprite.Group()
        self.collisionWallsSprite.add(self.wallsSprite)
    #    self.collisionPlayer = pygame.sprite.Group()
    #    self.collisionPlayer.add(self.player)

        self.spriteList = pygame.sprite.Group()
    #    self.shock = pygame.sprite.spritecollide(self.player, self.collisionWallsSprite, False, collided = None) # collided = None
        

        while self.game_over == False:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game_over = True
                    pygame.quit()
                    sys.exit()

                 
                if event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_LEFT:
                        self.player.update('left')
                    if event.key == pygame.K_RIGHT:
                        self.player.update('right')
                    if event.key == pygame.K_UP:
                        self.player.update('up')
                    if event.key == pygame.K_DOWN:
                        self.player.update('down')
                    
                        
                if event.type == pygame.KEYUP:

                    if event.key == pygame.K_LEFT:
                        self.player.update('stand_left')
                    if event.key == pygame.K_RIGHT:
                        self.player.update('stand_right')
                    if event.key == pygame.K_UP:
                        self.player.update('stand_up')
                    if event.key == pygame.K_DOWN:
                        self.player.update('stand_down')

                    
            if self.player.collision(self.player, self.collisionWallsSprite):
                self.shock = True
                print("colision !")
            if self.shock == False:
                self.player.move(self.xMove, self.yMove)



         #   self.player.move
            self.player.update
         #   self.handle_event(self.player.update)
            self.screen.blit(self.background, (0, 0))    
        
            
            self.screen.blit(self.wallsSprite.image, self.wallsSprite.rect)    
            self.screen.blit(self.player.image, self.player.rect)
            self.screen.blit(self.enemy.imageBroom, self.enemy.rect)
 
        
                
            pygame.display.flip()
            self.clock.tick(20)
                    
        

if __name__ == '__main__':
    pygame.init()
    game = Game()
    game.start()
   