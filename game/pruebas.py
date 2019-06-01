import pygame, sys
import textwrap
from pygame.locals import *

pygame.init()
clock = pygame.time.Clock()

class Executus(pygame.sprite.Sprite):
    __customes= ("Executus")
    
    def __init__(self, x=0, y= 0):  # x=0, y= 0
        self.sheet = pygame.image.load("spliteCat.png")
        self.sheet.set_clip(pygame.Rect(0, 0, 50, 30))
        self.image = self.sheet.subsurface(self.sheet.get_clip()) # get image nº1 of sprites
        self.rect = self.image.get_rect()
       # self.rect.topleft = position
        self.frame = 0
        self.position = [x, y]
                                                    
        self.right_states = { 0: ( 0, 0, 50, 30 ), 1: (32 , 0, 30, 50), 2: (64 , 0, 30, 50)}
        self.up_states = { 0: ( 0, 30, 30, 50 ), 1: (32 , 30, 30, 50), 2: (64 , 30, 30, 50)}
        self.down_states = { 0: ( 0, 60, 30, 50 ), 1: (32 , 60, 30, 50), 2: (64 , 60, 30, 50)}
        self.left_states = { 0: ( 0, 90, 30, 50 ), 1: (32 , 90, 30, 50), 2: (64 , 90, 30, 50)}
        #   ( 0, 0, 50, 30 )    pos y , pos x, large ,alt
        
    
    def get_frame(self, frame_set):  # loop state 
        self.frame += 1
        if self.frame > (len(frame_set) -1 ):
            self.frame = 0
        return frame_set(self.frame)
    
    
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
            self.clip(self.donw_states)
            self.rect.y += 4            
        
        
        if direction == 'stand_left':
            self.clip(self.left_states[0])
            
        if direction == 'stand_right':
            self.clip(self.right_states[0])
            
        if direction == 'stand_up':
            self.clip(self.up_states[0])
            
        if direction == 'stand_donw':
            self.clip(self.donw_states[0])
            
        self.image = self.sheet.subsurface(self.sheet.get_clip()) 
        
        
        
    def handle_event(self, event):
        if event.type == pygame.QUIT:
            game_over = True
                
            if event.type == pygame.KEYDOWN:

                if event.type == pygame.K_LEFT:
                    self.update('left')               
                if event.type == pygame.RIGHT:
                    self.update('right')                
                if event.type == pygame.K_UP:
                    self.update('up')
                if event.type == pygame.K_DOWN:
                    self.update('down')
                    
            if event.type == pygame.KEYUP: # necessary for position of sprites
                
                if event.key == pygame.K_LEFT:
                    self.update('stand_left')
                if event.type == pygame.RIGHT:
                    self.update('stand_right')                
                if event.type == pygame.K_UP:
                    self.update('stand_up')
                if event.type == pygame.K_DOWN:
                    self.update('stand_down')
                    


class Game():   
    __name = ("Executus")
    moveX = 0
    moveY = 0

    
    def __init__(self):
        self.__screen = pygame.display.set_mode((1040, 704))
        self.__background = pygame.image.load('indoor.png')
        pygame.display.set_caption("Executus time !")
        pygame.key.set_repeat(1,8)  # automatic move 
        
        self.executus = Executus(320, 240)  # 320, 240
        
        
    
                       
        
    def start(self):
        gameOver = False
        while not gameOver:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                    
                '''elif event.type == pygame.KEYDOWN:
                    keys = pygame.key.get_pressed()
                    if keys[pygame.K_UP]:
                        self.executus.position[1] -= 4
                                
                    elif keys[pygame.K_DOWN]:
                        self.executus.position[1] += 4
                                
                    elif keys[pygame.K_LEFT]:
                        self.executus.position[0] -= 4
                                
                    elif keys[pygame.K_RIGHT]:
                        self.executus.position[0] += 4
                                
                    else:
                        pass'''
                    

                
            self.executus.handle_event(event)
            self.__screen.blit(self.__background, (0, 0)) # refresh background
            self.__screen.blit(self.executus.sheet, self.executus.position)
            self.__screen.blit(self.executus.image, self.executus.rect)
            
            pygame.display.flip()
            clock.tick(20)
            
            

            
            
if __name__ =='__main__':
    game = Game()
    pygame.font.init()
    game.start()