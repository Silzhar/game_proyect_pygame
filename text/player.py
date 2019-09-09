import pygame , sys
import mainVersion

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
        for event in pygame.event.get():
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

class Executus(pygame.sprite.Sprite):
    def __init__(self, position):   #  initialize all the variables
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('I+S/gus 2.png')
        self.rect = self.image.get_rect()
        self.radius = 21
     #   self.rect.center = (screen_width/2,screen_height-48)

        self.shield = 100
        self.player_lives = 3
        self.hidden = False
        self.hide_timer = pygame.time.get_ticks()

        self.main = mainVersion
        self.width_window = 1040
        self.height_window = 704

        self.rect.center = (self.width_window/2,self.height_window-48)  
      

        
  
        self.sheet = pygame.image.load('spliteCat.png')
        self.sheet.set_clip(pygame.Rect(0, 0, 30, 30))  # visual box of sprite
        self.image = self.sheet.subsurface(self.sheet.get_clip())
        self.rect = self.image.get_rect()
     #   self.rect.topleft = position

        self.main = mainVersion
        self.width_window = 1040
        self.height_window = 704

        self.frame = 0
        self.radius = 21
        self.rect.center = (self.width_window/2,self.height_window-48)

        self.shield = 100
        self.player_lives = 3
        self.hidden = False
        self.hide_timer = pygame.time.get_ticks()

        
         
        # tour the sprite in frames to create animation                                       
        self.right_states = { 0: ( 0, 0, 30, 28 ), 1: (32 , 0, 30, 28), 2: (64 , 0, 30, 28)}
        self.up_states = { 0: ( 0, 30, 30, 30 ), 1: (32 , 30, 30, 30), 2: (64 , 30, 30, 30)}
        self.down_states = { 0: ( 0, 60, 30, 30 ), 1: (32 , 60, 30, 30), 2: (64 , 60, 30, 30)}
        self.left_states = { 0: ( 0, 90, 30, 50 ), 1: (32 , 90, 30, 50), 2: (64 , 90, 30, 50)}
        #   ( 0, 0, 50, 30 )    pos y , pos x, large ,alt   

 
    def knock(self):   # use this to knock bottles
        breaks = self.main.Breaks(self.rect.x,self.rect.y)
        self.allSprites.add(breaks)
        self.broken.add(breaks)
        self.main.Game.knockSound.play()

    
    def hide(self): # use this to hide the player temproarily (dead)
        self.hidden = True
        self.hide_timer = pygame.time.get_ticks()
        self.rect.center = (self.width_window/2,self.height_window + 200)  
     
             

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
                self.rect.center = (self.width_window/2, self.height_window - 48)   

   


    # we will use this class to add movement to the player
    def update(self, direction):
        self.speed = 4
        self.stop = 0
        self.xMove = 0
        self.yMove = 0 
        if direction == 'left':
            self.rect.x -= 4
        if direction == 'right':
            self.rect.x += 4
        if direction == 'up':
            self.rect.y -= 4
        if direction == 'down':
            self.rect.y += 4

        if direction == 'stand_left':
             self.xMove -= self.stop
        if direction == 'stand_right':
             self.xMove -= self.stop
        if direction == 'stand_up':
            self.yMove -= self.stop
        if direction == 'stand_down':
            self.yMove -= self.stop

     #   self.image = self.sheet.subsurface(self.sheet.get_clip())
        if self.hidden and pygame.time.get_ticks() -self.hide_timer > 1000:
                self.hidden = False
                self.rect.center = (self.width_window/2, self.height_window-48)

 
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
                self.update('stand_down')       '''
                
                
                