import pygame as PG, sys
import player
from pygame.locals import *
import pygame.event as GAME_EVENTS


class Broom(PG.sprite.Sprite):
    def __init__(self, position):
        PG.sprite.Sprite.__init__(self)
        self.sheetBroom = PG.image.load('broonGame.png')
        self.sheetBroom.set_clip(PG.Rect(0, 0, 13, 32)) # box of broom / crop image
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
            self.sheet.set_clip(PG.Rect(self.get_frame(clipped_rect)))
        else:
            self.sheet.set_clip(PG.Rect(clipped_rect))
        return clipped_rect



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

        self.player = player.Executus((width_window/10, height_window/4)) # add Executus to Game
        self.player.update  

        self.enemy = Broom((width_window/3, height_window/4))
        self.enemy.update
        

        self.wallsBg = PG.image.load('walls.png')
        self.wallsSprite = PG.sprite.Sprite()
        self.wallsSprite.image = self.wallsBg
        self.wallsSprite.rect = self.wallsBg.get_rect()
        self.Xwalls = 520
        self.Ywalls = 352
        self.positionWalls = (self.Xwalls, self.Ywalls)
        
               
                   
  
    def start(self):
        self.game_over = False
        
        
        self.collisionWallsSprite = PG.sprite.Group()
        self.collisionWallsSprite.add(self.wallsSprite)
    #    self.collisionPlayer = PG.sprite.Group()
    #    self.collisionPlayer.add(self.player)

        self.spriteList = PG.sprite.Group()
        self.shock = PG.sprite.spritecollide(self.player, self.collisionWallsSprite, False, collided = None) # collided = None
        

        while self.game_over == False:
            for event in PG.event.get():
                if event.type == PG.QUIT:
                    self.game_over = True
                    PG.quit()
                    sys.exit()

       

         #   if self.shock :
          #      print("colision")

            self.player.handle_event(event)
            self.screen.blit(self.background, (0, 0))    
        
            
            self.screen.blit(self.wallsSprite.image, self.wallsSprite.rect)    
            self.screen.blit(self.player.image, self.player.rect)
            self.screen.blit(self.enemy.imageBroom, self.enemy.rect)
 
        
                
            PG.display.flip()
            self.clock.tick(20)
                    
        

if __name__ == '__main__':
    PG.init()
    game = Game()
    game.start()
   
            
            

'''
(self.player.left_states, self.player.topleft) = self.player.handle_event(event)
(xAnt, yAnt) = (self.player.left_states, self.player.right_states)

if self.player.spritecollide(self.wallsSprite.rect):
    (self.player.left_states, self.player.topleft) = (xAnt, yAnt)   '''