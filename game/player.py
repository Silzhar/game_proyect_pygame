
import pygame

class Executus(pygame.sprite.Sprite):
    def __init__(self, position):
        self.sheet = pygame.image.load('spliteCat.png')
        self.sheet.set_clip(pygame.Rect(0, 0, 30, 30))
        self.image = self.sheet.subsurface(self.sheet.get_clip())
        self.rect = self.image.get_rect()
        self.rect.topleft = position
        self.frame = 0
      
                                                    
        self.right_states = { 0: ( 0, 0, 30, 28 ), 1: (32 , 0, 30, 28), 2: (64 , 0, 30, 28)}
        self.up_states = { 0: ( 0, 30, 30, 30 ), 1: (32 , 30, 30, 30), 2: (64 , 30, 30, 30)}
        self.down_states = { 0: ( 0, 60, 30, 30 ), 1: (32 , 60, 30, 30), 2: (64 , 60, 30, 30)}
        self.left_states = { 0: ( 0, 90, 30, 50 ), 1: (32 , 90, 30, 50), 2: (64 , 90, 30, 50)}
        #   ( 0, 0, 50, 30 )    pos y , pos x, large ,alt
        
    
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
                
                