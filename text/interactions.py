import pygame , random
import mainVersion

main = mainVersion

class Collision(pygame.sprite.Sprite):
    def __init__(self,center,size):
        pygame.sprite.Sprite.__init__(self)
        self.collisionFrame ={}
        self.collisionFrame['playerHit']=[]
        self.collisionFrame['player']=[]

        self.size = size
        self.image = self.collisionFrame[size][0]
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
            if self.frame == len(self.collisionFrame[self.size]):
                self.kill()
            else :
                center = self.rect.center
                self.image = self.collisionFrame[self.size][self.frame]
                self.rect = self.image.get_rect()
                self.rect.center = center


# we create the class for moving enemies 
class Brooms(pygame.sprite.Sprite):
    def __init__(self): 
        pygame.sprite.Sprite.__init__(self)
        broom = pygame.image.load('I+S/broom.png')
        self.imageOrigin = pygame.transform.scale(broom,(13,32))
        self.image = self.imageOrigin.copy()
        self.rect = self.image.get_rect()
        self.radius = int(self.rect.width*0.9/2)

        self.rect.x = random.randrange(0,main.Game.width_window-8)
        self.rect.y = random.randrange(100,main.Game.height_window-400)
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
        if self.rect.y > main.Game.height_window:
            self.rect.x = random.randrange(0,main.Game.width_window-500)
            self.rect.y = random.randrange(-100,-40)
            self.speedBrooms = random.randrange(1,4)


class Bottle(pygame.sprite.Sprite):
    def __init__(self, position):  
        pygame.sprite.Sprite.__init__(self)
        bottleOne = pygame.image.load('I+S/bottle.png')
        self.image = pygame.transform.scale(bottleOne,(12,30))   
        self.rect = self.image.get_rect()
        positions = [(720,602),(868,600)]
        self.rect = positions

    '''
    def update(self):
        all_sprites.add(bottles)
        all_sprites.draw(screen)   '''
