import pygame , sys
#import player
#import walls 
from pygame.locals import *


class Executus(pygame.sprite.Sprite):
    def __init__(self, position):
        pygame.sprite.Sprite.__init__(self)
        self.sheet = pygame.image.load('spliteCat.png')
        self.sheet.set_clip(pygame.Rect(0, 0, 30, 30))
        self.image = self.sheet.subsurface(self.sheet.get_clip())
        self.rect = self.image.get_rect()
        self.rect.topleft = position
        self.frame = 0
        
        
         
                                                    
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
        
        
            
        


    def handle_event(self, event):
        if event.type == pygame.QUIT:
            game_over = True
            self.pause= False

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

        self.player = Executus((width_window/10, height_window/4))
        self.player.update  # asi deberia encontrar el rectangulo del player
        

        self.wallsBg = pygame.image.load('walls.png')
        self.wallsSprite = pygame.sprite.Sprite()
        self.wallsSprite.image = self.wallsBg
        self.wallsSprite.rect = self.wallsBg.get_rect()
        

                    
    def Collisions(self, spriteGroup):
        direction = Executus
        self.collisionWallsSprite = pygame.sprite.Group()
        self.collisionWallsSprite.add(self.wallsSprite.rect)
        self.collisionPlayer = pygame.sprite.Group()
        self.collisionPlayer.add(self.player)
        
        self.allSprites = pygame.sprite.Group()
        self.allSprites.add(self.collisionWallsSprite)
        self.allSprites.add(self.collisionPlayer)
        
        if pygame.sprite.spritecollide(self, spriteGroup, True):
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
                    
        
    def Pause(self):
        self.pause == True
        width_window = 1000
        height_window = 680
        
        while self.pause == True:
            self.screen = pygame.display.set_mode((width_window, height_window))
            self.background = pygame.image.load('E&A relieve color.jpg')
            pygame.display.set_caption("PAUSE")
            self.fuente = pygame.font.Font('font.ttf', 48) 
            self.fuente.render(" - PAUSE - ", 1, (255, 255, 0))
            
            pygame.display.update()
            
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.pause = False
                    if event.key == pygame.K_SPACE:
                       self.Pause()
                
  
 #   def start(self):
        self.game_over = False
        
        while self.game_over == False:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game_over = True
                    pygame.quit()
                    sys.exit()
                    self.Pause()
                
           # self.Collisions(self.player.update )
          #  self.player.update(self.Collisions(self.player))   
            self.player.handle_event(event)
            self.screen.blit(self.background, (0, 0))    # screen.blit(walls, (0, 0))
          #  self.player.Collisions(self.allSprites)
        
           # screen.blit(walls, walls.rect)
           # walls.Limits((0, 0)) 
       #     self.Pause()
            self.screen.blit(self.wallsSprite.image, self.wallsSprite.rect)    
            self.screen.blit(self.player.image, self.player.rect)
 
        
                
            pygame.display.flip()
            self.clock.tick(20)
                
        

if __name__ == '__main__':
    pygame.init()
    game = Game()
#    game.start()
    game.Pause()

    
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