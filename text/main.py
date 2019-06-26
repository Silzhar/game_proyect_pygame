import pygame
import player
import walls

from pygame.locals import *


pygame.init()

        
width_window = 1040
height_window = 704


        
screen = pygame.display.set_mode((width_window, height_window))
background = pygame.image.load('indoor.png')
pygame.display.set_caption("Executus time !")
clock = pygame.time.Clock() 

player = player.Executus((width_window/10, height_window/4))


wallsBg = pygame.image.load('walls.png')
wallsSprite = pygame.sprite.Sprite()
wallsSprite.image = wallsBg
wallsSprite.rect = wallsBg.get_rect()

#wallsLimits = walls.Limits((0, 0))
wallsLimits = walls
wallsLimits = pygame.sprite.Sprite()
# wallsLimits = walls.get_rect()


collisions = pygame.sprite.collide_rect(wallsSprite, player)


game_over = False

while game_over == False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
    
   # walls.Limits((0, 0))            
    player.handle_event(event)
    
    screen.blit(background, (0, 0))    # screen.blit(walls, (0, 0))

   # screen.blit(walls, walls.rect)
    screen.blit(wallsSprite.image, wallsSprite.rect)    
    screen.blit(player.image, player.rect)
    
    if collisions == True :
        player.update( player) == None

                
    pygame.display.flip()
    clock.tick(20)
                
pygame.quit()


            
            
