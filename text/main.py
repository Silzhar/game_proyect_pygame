import pygame
import player


pygame.init()

        
width_window = 1040
height_window = 704
        
screen = pygame.display.set_mode((width_window, height_window))
background = pygame.image.load('indoor.png')
pygame.display.set_caption("Executus time !")
clock = pygame.time.Clock()
player = player.Executus((width_window/10, height_window/10))



game_over = False

while game_over == False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
                        
    player.handle_event(event)
    screen.blit(background, (0, 0))
    screen.blit(player.image, player.rect)
                
    pygame.display.flip()
    clock.tick(20)
                
pygame.quit()
            
            
