import pygame

import settings

 # Need this class to break the bottles (I have not managed to do it with pyagame modules).
class Breaks(pygame.sprite.Sprite): 
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.attackImage = pygame.image.load("{0}{1}".format(settings.ASSETS_PATH, "attack.png"))
        self.image = pygame.transform.scale(self.attackImage, (10, 10))
        self.rect = self.image.get_rect()
        self.radius = int(self.rect.width/2)
        self.rect.bottom = y
        self.rect.centerx = x+24
        self.attackImage = -2

    def update(self):
        self.rect.y + self.attackImage
        if self.rect.y < 0:
            self.kill()

# Need Collision to get the frame of the image animation and its center.
# Later,you can delete if you want the image.
class Collision(pygame.sprite.Sprite):
    def __init__(self, center, object_id, collisions_frame):
        pygame.sprite.Sprite.__init__(self)

        self.collisions_frame = collisions_frame
        self.object_id = object_id
        self.image = self.collisions_frame[object_id][0]
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.frame = 0
        self.last_update = pygame.time.get_ticks()
        self.frame_rate = 75

    def update(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > self.frame_rate:
            self.last_update = now
            self.frame += 1

            if self.frame == len(self.collisions_frame[self.object_id]):
                self.kill()

            else:
                center = self.rect.center
                self.image = self.collisions_frame[self.object_id][self.frame]
                self.rect = self.image.get_rect()
                self.rect.center = center
