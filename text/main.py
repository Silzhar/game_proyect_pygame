import pygame
import player
from pygame.locals import *


pygame.init()

        
width_window = 1040
height_window = 704
        
screen = pygame.display.set_mode((width_window, height_window))
background = pygame.image.load('indoor.png')
walls = pygame.image.load('walls.png')
pygame.display.set_caption("Executus time !")
clock = pygame.time.Clock()

player = player.Executus((width_window/5, height_window/5))
wallsSprite = pygame.sprite.Sprite()
wallsSprite.image = walls
wallsSprite.rect = walls.get_rect()

direction = player.update(move) # need solution !
collisions = pygame.sprite.collide_rect(wallsSprite, player)

    

game_over = False

while game_over == False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
                        
    player.handle_event(event)
    screen.blit(background, (0, 0))    # screen.blit(walls, (0, 0))
    if collisions == True:
        player.update(direction) == 0
        

                  
        
    screen.blit(player.image, player.rect)
                
    pygame.display.flip()
    clock.tick(20)
                
pygame.quit()


            
            
