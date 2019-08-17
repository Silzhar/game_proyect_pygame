import pygame as PG, sys
import player
from pygame.locals import *
import pygame.event as GAME_EVENTS

class Menu():
    def __init__(self, options): # initial  options
        self.options = options
        self.totalOptions = len(self.options)
        self.select = 0
        self.pressed = False
    
    def actualize(self):   # change the value of self.pressed with the directional
        myKey = PG.key.get_pressed()

        if not self.pressed:
            if myKey.K_UP:
                self.select -= 1
            elif PG.K_DOWN:
                self.select += 1
            elif myKey.K_RETURN:  # invokes the function associated with the option
                title, function = self.options[self.select]
                print("select option :")



    def menuWindow(self):  # , screen
        width_window = 1020
        height_window = 680   

        self.initialScreen = PG.display.set_mode((width_window, height_window)) 
        self.backgroundInitial = PG.image.load('E&A relieve color.jpg')
        self.fontInitial = PG.font.Font('font.ttf', 48)
        self.fontInitial.render("- PAUSE -",1,(255, 255, 0))


    def menuExit(self):
        sys.exit(0)




class Game(PG.sprite.Sprite):
    
    def __init__(self): 
        width_window = 1040
        height_window = 704
 
        self.menu = Menu # initial menu
        self.options = [
                    ('PLAY', self.start),
                    ('OPTIONS'),  # , optionsMenu
                    ('EXIT', self.menu.menuExit)
                ]
        
        self.menu = Menu(self.options)
                               
        
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
        

        self.wallsBg = PG.image.load('walls.png')
        self.wallsSprite = PG.sprite.Sprite()
        self.wallsSprite.image = self.wallsBg
        self.wallsSprite.rect = self.wallsBg.get_rect()
        
        
        
    def Collisions(self, direction):
        self.collisionWallsSprite = PG.sprite.Group()
        self.collisionWallsSprite.add(self.wallsSprite)
        self.collisionPlayer = PG.sprite.Group()
        self.collisionPlayer.add(self.player)

    '''    
    def reStart(self, event):
        width_window = 1020
        height_window = 680   

        self.initialScreen = PG.display.set_mode((width_window, height_window)) 
        self.backgroundInitial = PG.image.load('E&A relieve color.jpg')
        self.clock = PG.time.Clock()
        self.fontInitial = PG.font.Font('font.ttf', 48)
        self.fontInitial.render("- PAUSE -",1,(255, 255, 0))

    
        self.game_started = False
     #   self.screenReStart = PG.display.set_mode( (0, 0))

        self.screen.blit(self.wallsSprite.image, self.wallsSprite.rect)    
        self.screen.blit(self.player.image, self.player.rect)


        if self.player.handle_event == PG.KEYDOWN:
            if event.key == PG.K_SPACE:
                if self.game_started == False:
                    self.game_started == True
                else:
                    self.game_started == False  '''
        
                   
  
    def start(self):
        self.game_over = False
        
        while self.game_over == False:
            for event in PG.event.get():
                if event.type == PG.QUIT:
                    self.game_over = True
                    PG.quit()
                    sys.exit()

            
         #   self.reStart(Game)
            self.player.update(self.Collisions(self.player))   
            self.player.handle_event(event)
            self.screen.blit(self.background, (0, 0))    
        
            self.menu.menuWindow()
            self.screen.blit(self.wallsSprite.image, self.wallsSprite.rect)    
            self.screen.blit(self.player.image, self.player.rect)
 
        
                
            PG.display.flip()
            self.clock.tick(20)
                    
        

if __name__ == '__main__':
    PG.init()
    game = Game()
    game.start()
    menu = Menu 
    

