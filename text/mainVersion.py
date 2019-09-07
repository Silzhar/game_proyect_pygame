import pygame , sys
import player
from pygame.locals import *
import pygame.event as GAME_EVENTS




class Game(pygame.sprite.Sprite):
    
    def __init__(self): 
        self.width_window = 1040
        self.height_window = 704

        self.white = (255, 255, 255)
        self.black = (  0,   0,   0)
        self.green = (0,   255,   0)

        self.score = 0 # this will keep track of the score
        
        pygame.mixer.init()
        pygame.mixer.music.load('gameLoops.mp3')   #  background music
        pygame.mixer.music.play(-1)
        
        self.executusMeow = pygame.mixer.Sound('Cat_Meow.wav')    #  cat sound
    

        # GAME SCREEN  
        self.screen = pygame.display.set_mode((self.width_window, self.height_window))   
        self.background = pygame.image.load('indoor.png')
        pygame.display.set_caption("Executus time !")
        self.font_name = pygame.font.match_font('Arial')
        self.clock = pygame.time.Clock() 

        self.player = player.Executus((self.width_window/10, self.height_window/4)) # add Executus to Game
        self.playerImageLives =  self.player.sheet         #  pygame.transform.scale(player,(34,28))
        self.player.update  

        

        self.wallsBg = pygame.image.load('walls.png')
        self.wallsSprite = pygame.sprite.Sprite()
        self.wallsSprite.image = self.wallsBg
        self.wallsSprite.rect = self.wallsBg.get_rect()
        self.Xwalls = 520
        self.Ywalls = 352
        self.positionWalls = (self.Xwalls, self.Ywalls)


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
        self.game_over = False
        
        
        self.collisionWallsSprite = pygame.sprite.Group()
        self.collisionWallsSprite.add(self.wallsSprite)


        self.spriteList = pygame.sprite.Group()

        

        while self.game_over == False:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game_over = True
                    pygame.quit()
                    sys.exit()

       

        

            self.player.handle_event(event)
            self.screen.blit(self.background,(0,0))
            self.text(self.screen,str(self.score),18,self.width_window/2,10)
            self.lifeBar(self.screen,5,5,self.player.shield)
            self.lives(self.screen,self.width_window-100,5,self.player.player_lives,self.playerImageLives)
            self.screen.blit(self.wallsSprite.image, self.wallsSprite.rect)    
            self.screen.blit(self.player.image, self.player.rect)
       
 
        
                
            pygame.display.flip()
            self.clock.tick(20)
                    
        

if __name__ == '__main__':
    pygame.init()
    game = Game()
    game.start()
   
            