import pygame , sys , random
import player 
from pygame.locals import *
import pygame.event as GAME_EVENTS


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
        self.rect = position


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
        self.player = player.Executus() # ((self.width_window/10, self.height_window/4)) # add Executus to Game
        self.playerImageLives = pygame.image.load('I+S/gus 2.png')         #  pygame.transform.scale(player,(34,28))
        self.player.update  

        # BOTTLES
        self.positions = [(720,602),(868,600)]
        self.bottle1 = Bottle(self.positions[0])

        self.wallsBg = pygame.image.load('walls.png')
        self.wallsSprite = pygame.sprite.Sprite()
        self.wallsSprite.image = self.wallsBg
        self.wallsSprite.rect = self.wallsBg.get_rect()
        self.Xwalls = 520
        self.Ywalls = 352
        self.positionWalls = (self.Xwalls, self.Ywalls)

        # GROUPS SPRITES
        self.broken = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group() 
        self.allSprites = pygame.sprite.Group()
        self.allSprites.add(self.player)

        self.bottles = pygame.sprite.Group()
        self.bottles.add(self.bottle1)

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
        self.game_play = True # True ?? comprobar
        collisionFrame ={}
        collisionFrame['playerHit']=[]
        collisionFrame['player']=[]

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


                if event.type == pygame.KEYDOWN:                     
                    if event.key == pygame.K_LEFT:
                        self.player.rect.x -= 4
                    if event.key == pygame.K_RIGHT:
                        self.player.rect.x += 4
                    if event.key == pygame.K_UP: 
                        self.player.rect.y -= 4 
                    if event.key == pygame.K_DOWN: 
                        self.player.rect.y += 4

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT:
                        self.xMove -= self.stop
                    if event.key == pygame.K_RIGHT:
                        self.xMove += self.stop
                    if event.key == pygame.K_UP:
                        self.yMove -= self.stop
                    if event.key == pygame.K_DOWN:
                        self.yMove += self.stop

                if self.player.hidden and pygame.time.get_ticks() -self.hide_timer > 1000:
                        self.hidden = False
                        self.rect.center = (self.width_window/2,self.height_window - 48)
                        
            
            self.allSprites.update()
            # check whether broken hit
            hits = pygame.sprite.groupcollide(self.broken,self.bottles,True,True)
            if hits:
                self.hitSound.play()
            for hit in hits:
                score += 1
                expl = self.Collision(hit.rect.center,'playerHit')
                self.allSprites.add(expl)
                self.allSprites.add(self.bottles)
            
                

            # here we see whether it will hit or not
            hits = pygame.sprite.spritecollide(self.player,self.enemies,True,pygame.sprite.collide_circle)
            for hit in hits:
                self.broomHit.play() # change
                expl1 = self.Collision(hit.rect.center,'playerHit')
                self.allSprites.add(expl1)
                brooms = Brooms()
                self.allSprites.add(brooms)
                self.enemies.add(brooms)
                self.player.shield -= 50
                if self.player.shield <= 0:
                    death_explosion = self.Collision(self.player.rect.center,'player')
                    self.allSprites.add(death_explosion)
                    self.player.hide()
                    self.player.player_lives -= 1
                    self.player.shield = 100

                if hits == False:
                    pygame.sprite.Group.clear() 
                    hits = self.broken.pygame.sprite.empty()
        

            if self.player.player_lives == 0 and not death_explosion.alive():
                self.game_play = False


    
         #   self.player.handle_event(event)
            self.screen.blit(self.background,(0,0))
            self.text(self.screen,str(self.score),18,self.width_window/2,10)
            self.lifeBar(self.screen,5,5,self.player.shield)
            self.lives(self.screen,self.width_window-100,5,self.player.player_lives,self.playerImageLives)
        #    self.screen.blit(self.wallsSprite.image, self.wallsSprite.rect)    
            self.screen.blit(self.player.image, self.player.rect)
            self.allSprites.draw(self.screen)
       
 
        
                
            pygame.display.flip()
            self.clock.tick(20)
                    
        

if __name__ == '__main__':
    pygame.init()
    game = Game()
    game.start()
   
            