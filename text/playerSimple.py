import pygame , sys
import mainVersion
from pygame.locals import *



class Executus(pygame.sprite.Sprite):
    def __init__(self):   #  initialize all the variables
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('I+S/gus 2.png')
        self.rect = self.image.get_rect()
        self.radius = 21

        self.main = mainVersion
        self.width_window = 1040
        self.height_window = 704

        self.rect.center = (self.width_window/2,self.height_window-48) 

        self.shield = 100
        self.player_lives = 3
        self.hidden = False
        self.hide_timer = pygame.time.get_ticks()

    
    # we will use this class to add movement to the player
    def update(self):
        self.speed = 4
        self.stop = 0
        self.xMove = 0
        self.yMove = 0    

      #  key = pygame.key.get_pressed()
        
        '''
        if event.type == pygame.KEYDOWN:                     
            if event.key == pygame.K_LEFT:
                self.rect.x -= 4
            if event.key == pygame.K_RIGHT:
                self.rect.x += 4
            if event.key == pygame.K_UP: 
                self.rect.y -= 4 
            if event.key == pygame.K_DOWN: 
                self.rect.y += 4

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                self.xMove -= self.stop
            if event.key == pygame.K_RIGHT:
                self.xMove += self.stop
            if event.key == pygame.K_UP:
                self.yMove -= self.stop
            if event.key == pygame.K_DOWN:
                self.yMove += self.stop   '''

        if self.hidden and pygame.time.get_ticks() -self.hide_timer > 1000:
                self.hidden = False
                self.rect.center = (self.width_window/2,self.height_window - 48) 

    
    def knock(self):   # use this to knock bottles
        breaks = self.main.Breaks(self.rect.x,self.rect.y)
        self.main.Game.allSprites.add(breaks)
        self.main.Game.broken.add(breaks)
        knockSound = pygame.mixer.Sound('I+S/swoosh.wav')
        knockSound.play()

    
    def hide(self): # use this to hide the player temproarily (dead)
        self.hidden = True
        self.hide_timer = pygame.time.get_ticks()
        self.rect.center = (self.width_window/2,self.height_window + 200)    


    '''
    # we will use this class to add movement to the player
    def update(self,event):
        self.speed = 4
        self.stop = 0
        self.xMove = 0
        self.yMove = 0 
        if event.type == pygame.KEYDOWN:                     
            if event.key == pygame.K_LEFT:
                self.rect.x -= 4
            if event.key == pygame.K_RIGHT:
                self.rect.x += 4
            if event.key == pygame.K_UP: 
                self.rect.y -= 4 
            if event.key == pygame.K_DOWN: 
                self.rect.y += 4

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                self.xMove -= self.stop
            if event.key == pygame.K_RIGHT:
                self.xMove += self.stop
            if event.key == pygame.K_UP:
                self.yMove -= self.stop
            if event.key == pygame.K_DOWN:
                self.yMove += self.stop

        if self.hidden and pygame.time.get_ticks() -self.hide_timer > 1000:
                self.hidden = False
                self.rect.center = (self.width_window/2, self.height_window - 48)    '''

