import random , sys
import pygame
from pygame.locals import *


class Breaks(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.attackImage = pygame.image.load('I+S/attack.png')
        self.image = pygame.transform.scale(self.attackImage,(10,10))
        self.rect = self.image.get_rect()
        self.radius = int(self.rect.width/2)
        self.rect.bottom = y
        self.rect.centerx = x+24
        self.attackImage = -2

    def update(self):
        self.rect.y + self.attackImage
        if self.rect.y < 0:
            self.kill()
              

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
    
        self.width_window = 1040
        self.height_window = 704

        self.rect.center = (self.width_window/2,self.height_window-48)     

        self.sheet = pygame.image.load('spliteCat.png')
        self.sheet.set_clip(pygame.Rect(0, 0, 30, 30))  # visual box of sprite
        self.image = self.sheet.subsurface(self.sheet.get_clip())
        self.rect = self.image.get_rect()
     #   self.rect.topleft = position

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
        self.knockSound = pygame.mixer.Sound('I+S/swoosh.wav')
        self.knockSound.play()


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
        if self.hidden and pygame.time.get_ticks() -self.hide_timer > 1000:
                self.hidden = False
                self.rect.center = (self.width_window/2, self.height_window-48)

 
    def handle_event(self, event):
        if event.type == pygame.QUIT:
            game_over = True


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


                

class Collision(pygame.sprite.Sprite):
    def __init__(self,center,size):
        pygame.sprite.Sprite.__init__(self)
        self.game = Game()

        self.size = size
        self.image = self.game.collisionFrame[size][0]
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.frame = 0
        self.last_update = pygame.time.get_ticks()
        self.frame_rate = 75

    def update(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > self.frame_rate:
            self.last_update = now
            self.frame +=1
            if self.frame == len(self.game.collisionFrame[self.size]):
                self.kill()
            else :
                center = self.rect.center
                self.image = self.game.collisionFrame[self.size][self.frame]
                self.rect = self.image.get_rect()
                self.rect.center = center   


# we create the class for moving enemies 
class Brooms(pygame.sprite.Sprite):
    def __init__(self): 
        pygame.sprite.Sprite.__init__(self)
        self.width_window = 1040
        self.height_window = 704

        broom = pygame.image.load('I+S/broom.png')
        self.imageOrigin = pygame.transform.scale(broom,(13,32))
        self.image = self.imageOrigin.copy()
        self.rect = self.image.get_rect()
        self.radius = int(self.rect.width*0.9/2)

        self.rect.x = random.randrange(0,self.width_window-8)
        self.rect.y = random.randrange(100,self.height_window-400)
        self.speedBrooms = random.randrange(1,4)
        self.rot = 0

        self.rot_speed = random.randrange(-8,8)
        self.last_update = pygame.time.get_ticks()

    def rotation(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > 50:
            self.last_update = now
            self.rot += (self.rot_speed)%360
            new_img = pygame.transform.rotate(self.imageOrigin,self.rot)
            oldCenter = self.rect.center
            self.image = new_img
            self.rect =self.image.get_rect()
            self.rect.center = oldCenter

    def update(self): # this will be used to move the object
        self.rotation()
        self.rect.y += self.speedBrooms
        if self.rect.y > self.height_window:
            self.rect.x = random.randrange(0,self.width_window-500)
            self.rect.y = random.randrange(-100,-40)
            self.speedBrooms = random.randrange(1,4)


class Bottle(pygame.sprite.Sprite):
    def __init__(self, position):  
        pygame.sprite.Sprite.__init__(self)
        bottleOne = pygame.image.load('I+S/bottle.png')
        self.image = pygame.transform.scale(bottleOne,(12,30))   
        self.rect = self.image.get_rect()
        self.rect.topleft = position # take the coordinates of the rect (upper left corner)

    def update(self):
        newPossition = self.rect.topleft   
        return newPossition


class Game(pygame.sprite.Sprite):
    
    def __init__(self): 
        self.width_window = 1040
        self.height_window = 704

        self.white = (255, 255, 255)
        self.black = (  0,   0,   0)
        self.green = (0,   255,   0)

        self.score = 0 # this will keep track of the score
        
        # load all the sound
        pygame.mixer.init()
        pygame.mixer.music.load('I+S/gameLoops.mp3')  #  background music
        self.knockSound = pygame.mixer.Sound('I+S/swoosh.wav')
        self.hitSound = pygame.mixer.Sound('I+S/glass_break.wav')
        self.broomHit = pygame.mixer.Sound('I+S/wail_cat.wav')
        pygame.mixer.music.play(-1)
        
        self.executusMeow = pygame.mixer.Sound('Cat_Meow.wav')    #  cat sound
    
        # GAME SCREEN  
        self.screen = pygame.display.set_mode((self.width_window, self.height_window))   
        self.background = pygame.image.load('indoor.png')
        pygame.display.set_caption("Executus time !")
        self.font_name = pygame.font.match_font('Arial')
        self.clock = pygame.time.Clock() 

        # PLAYER
        self.player = Executus((self.width_window/10, self.height_window/4))   #  add Executus to Game
        self.playerImageLives = pygame.image.load('I+S/gus 2.png')     # lives (3), upper right of the screen
        self.player.update  

        # BOTTLES creation and position
        self.positions = [(720,602),(868,600)]
        self.bottle1 = Bottle(self.positions[0])
        self.bottle2 = Bottle(self.positions[1])

        self.wallsBg = pygame.image.load('walls.png')
        self.wallsSprite = pygame.sprite.Sprite()
        self.wallsSprite.image = self.wallsBg
        self.wallsSprite.rect = self.wallsBg.get_rect()
        self.Xwalls = 520
        self.Ywalls = 352
        self.positionWalls = (self.Xwalls, self.Ywalls)

        # GROUPS SPRITES import from interactions
     #   self.sprites = interactions
        self.broken = pygame.sprite.Group()  # add sprites in (def knock) to breack bottles
        self.enemies = pygame.sprite.Group() # ad brooms to the sprites group


        self.allSprites = pygame.sprite.Group()
        self.allSprites.add(self.player)

        self.bottles = pygame.sprite.Group()
        self.bottles.add(self.bottle1)
        self.bottles.add(self.bottle2)
        self.allSprites.add(self.bottles)
        
        # class , definitions
        self.brooms = Brooms()
    #    self.breacks = Breaks()

        # collisions loop : player & objets 
        self.collisionFrame ={}
        self.collisionFrame['playerHit']=[]
        self.collisionFrame['player']=[]

        for i in range(0,8):
            breackBottle = pygame.image.load('I+S/breackBottle.png')
            img = (breackBottle) 

            tombstoneOrigin = pygame.image.load('I+S/Tombstone.png')
            tombstone = pygame.transform.scale(tombstoneOrigin,(70,60))
            self.collisionFrame['player'].append(tombstone)

            img_playerHit = pygame.transform.scale(breackBottle,(32,32))
            self.collisionFrame['playerHit'].append(img_playerHit)


        # as we need multiple eneimies we will use a for loop
        for i in range(8):
            brooms = Brooms()
            self.enemies.add(brooms)
            self.allSprites.add(brooms)    


    def text(self,surface,text,size,x,y):  # function to draw text
        font = pygame.font.SysFont(self.font_name,size)
        textSurface = font.render(text,True, self.white)
        textRect = textSurface.get_rect()
        textRect.midtop =(x, y)
        surface.blit(textSurface,textRect)


    def lives(self,surf,x,y,lives,img):  # total lives (3) 
        for i in range(lives):
            img_rect = img.get_rect()
            img_rect.x = x + 30*i
            img_rect.y = y
            surf.blit(img,img_rect)


    def lifeBar(self,surf,x,y,total):   # life : status / position 
        if total < 0:
            total = 0
        bar_length = 100
        bar_height = 10
        fill =(total/100)*bar_length
        exteriorLifeRect = pygame.Rect(x,y,bar_length,bar_height)
        insideLifeRect = pygame.Rect(x,y,fill,bar_height)
        pygame.draw.rect(surf,self.green,insideLifeRect)  # life points (green)
        pygame.draw.rect(surf,self.white,exteriorLifeRect,2) # outer rectangle (whilte) ,life frame

 
        


    def start(self):
        self.game_play = True 

    # we will use this class to add movement to the player
        self.speed = 4
        self.stop = 0
        self.xMove = 0
        self.yMove = 0 

      
        while self.game_play == True:
            for event in pygame.event.get():
                          
                if event.type == pygame.QUIT:
                    self.game_play = False
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.player.knock()
                        breaks = Breaks(self.player.rect.x,self.player.rect.y)
                        self.allSprites.add(breaks)
                        self.broken.add(breaks)
                    
            
        
            # check whether broken hit
            
            hits = pygame.sprite.groupcollide(self.broken,self.bottles,True,True)  # groupcollide   collided = None
            if hits:
                self.hitSound.play()
            for hit in hits:
                self.score += 1
                expl = Collision(hit.rect.center,'playerHit')
                self.allSprites.add(expl)
                self.allSprites.add(self.bottles)   
                      

            # here we see whether it will hit or not
            hits = pygame.sprite.spritecollide(self.player,self.enemies,True,pygame.sprite.collide_circle)
            for hit in hits:
                self.broomHit.play() # change
                expl1 = Collision(hit.rect.center,'playerHit')
                self.allSprites.add(expl1)
                brooms = Brooms()
                self.allSprites.add(brooms)
                self.enemies.add(brooms)
                self.player.shield -= 50

                if self.player.shield <= 0:
                    self.death_explosion = Collision(self.player.rect.center,'player')
                    self.allSprites.add(self.death_explosion)
                    self.player.hide()
                    self.player.player_lives -= 1
                    self.player.shield = 100
                   
                if hits == False:
                    pygame.sprite.Group.clear() 
                    hits = self.allSprites.empty()
        
            if self.player.player_lives == 0 and not self.death_explosion.alive():
                self.game_play = False
                

            self.screen.blit(self.background,(0,0))
            self.text(self.screen,str(self.score),18,self.width_window/2,10)
            self.lifeBar(self.screen,5,5,self.player.shield)
            self.lives(self.screen,self.width_window-100,5,self.player.player_lives,self.playerImageLives)
        
            self.screen.blit(self.player.image, self.player.rect)
            self.allSprites.draw(self.screen)

            self.enemies.update()
            self.bottles.update()
            self.player.handle_event(event)
                  
            pygame.display.flip()
            self.clock.tick(20)
                    
           

if __name__ == '__main__':
    pygame.init()
    game = Game()
    game.start()
