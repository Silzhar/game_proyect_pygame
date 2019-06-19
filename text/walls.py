import pygame
import main




class Limits(pygame.sprite.Sprite):
    def __init__(self, position):
        self.shape_color = (40, 210, 250)
        self.rectangles.image = main.screen
        

    def Walls(self,rectangles):
        if rectangles.type == pygame.ACTIVEEVENT :
        
            # dibuja 3 rectángulos
            self.pygame.draw.rect( self.shape_color, (25, 25, 350, 100), 1)
            self.pygame.draw.rect( self.shape_color, ((25, 150), (350, 100)), 4)
            self.pygame.draw.rect( self.shape_color, pygame.Rect((25, 275, 350, 100)), 0)
        
        return

    # actualiza la pantalla
  #  pygame.display.flip()

       
'''

wallsBg = pygame.image.load('walls.png')       
       
color = (255, 255, 255)

wall1 = pygame.draw.polygon(wallsBg, color, [(53, 492),(53, 529),(495, 529), (495, 492)])  # colores
shape_color = (40, 210, 250)




        self.image = self.wall1.subsurface(self.wall1.dimensions())
        self.rect = self.image.get_rect()

                
    def dimensions(self, limits):

        
     
        self.height = 53
        self.width = 495
        self.x = 492
        self.y = 529  
        
        
        color = (255, 255, 255)

wall1 = pygame.draw.polygon(wallsBg, color, [(53, 492),(53, 529),(495, 529), (495, 492)])
wall1Limit = pygame.sprite.Sprite() 
wall1Limit.image = wall1
wall1Limit.rect = wall1Limit.get_rect() 

        
        
        '''
        
