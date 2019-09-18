import sys

import pygame

from models.player import Executus
from models.actions import Collision, Breaks
from models.enemies import Brooms
from models.items import Bottle
import settings


class Game(pygame.sprite.Sprite):

    def __init__(self):
        self.width_window = 1040
        self.height_window = 704

        self.white = (255, 255, 255)
        self.black = (0,   0,   0)
        self.green = (0,   255,   0)

        self.score = 0  # this will keep track of the score

        # load all the sound
        pygame.mixer.init()
        pygame.mixer.music.load("{0}{1}".format(settings.ASSETS_PATH, "gameLoops.mp3"))  # background music
        self.knockSound = pygame.mixer.Sound("{0}{1}".format(settings.ASSETS_PATH, "swoosh.wav"))
        self.hitSound = pygame.mixer.Sound("{0}{1}".format(settings.ASSETS_PATH, "glass_break.wav"))
        self.broomHit = pygame.mixer.Sound("{0}{1}".format(settings.ASSETS_PATH, "wail_cat.wav"))
        pygame.mixer.music.play(-1)

        self.executusMeow = pygame.mixer.Sound("{0}{1}".format(settings.ASSETS_PATH, "Cat_Meow.wav"))  # cat sound

        # GAME SCREEN
        self.screen = pygame.display.set_mode((self.width_window, self.height_window))
        self.background = pygame.image.load("{0}{1}".format(settings.ASSETS_PATH, "indoor.png"))
        pygame.display.set_caption("Executus time !")
        self.font_name = pygame.font.match_font('Arial')
        self.clock = pygame.time.Clock()

        # PLAYER
        # add Executus to Game
        self.player = Executus((self.width_window/10, self.height_window/4))
        self.playerImageLives = pygame.image.load("{0}{1}".format(settings.ASSETS_PATH, "gus 2.png"))  # lives (3), upper right of screen.
        self.player.update

        # BOTTLES creation and position
        self.positions = [(720, 602), (868, 600)]
        self.bottle1 = Bottle(self.positions[0])
        self.bottle2 = Bottle(self.positions[1])

        self.wallsBg = pygame.image.load("{0}{1}".format(settings.ASSETS_PATH, "walls.png"))
        self.wallsSprite = pygame.sprite.Sprite()
        self.wallsSprite.image = self.wallsBg
        self.wallsSprite.rect = self.wallsBg.get_rect()
        self.Xwalls = 520
        self.Ywalls = 352
        self.positionWalls = (self.Xwalls, self.Ywalls)

        # GROUPS SPRITES
        # add sprites in (def knock) to breack bottles
        self.broken = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()  # ad brooms to the sprites group

        self.allSprites = pygame.sprite.Group()

        self.bottles = pygame.sprite.Group()
        self.bottles.add(self.bottle1)
        self.bottles.add(self.bottle2)
        self.allSprites.add(self.bottles)

        # add break bottles to draw in screen
        self.breackBottles = pygame.sprite.Group()

        # class, definitions
        self.brooms = Brooms()

        # collisions loop : player & objets
        self.collisions_frame = {}
        self.collisions_frame['playerHit'] = []
        self.collisions_frame['player'] = []

        for i in range(0, 8):
            breackBottle = pygame.image.load("{0}{1}".format(settings.ASSETS_PATH, "breackBottle.png"))

            tombstoneOrigin = pygame.image.load("{0}{1}".format(settings.ASSETS_PATH, "Tombstone.png"))
            tombstone = pygame.transform.scale(tombstoneOrigin, (70, 60))
            self.collisions_frame['player'].append(tombstone)

            img_playerHit = pygame.transform.scale(breackBottle, (32, 32))
            self.collisions_frame['playerHit'].append(img_playerHit)

        # as we need multiple eneimies we will use a for loop
        for i in range(8):
            brooms = Brooms()
            self.enemies.add(brooms)
            self.allSprites.add(brooms)

    def text(self, surface, text, size, x, y):  # function to draw text
        font = pygame.font.SysFont(self.font_name, size)
        textSurface = font.render(text, True, self.white)
        textRect = textSurface.get_rect()
        textRect.midtop = (x, y)
        surface.blit(textSurface, textRect)

    def lives(self, surf, x, y, lives, img):  # total lives (3)
        for i in range(lives):
            img_rect = img.get_rect()
            img_rect.x = x + 30*i
            img_rect.y = y
            surf.blit(img, img_rect)

    def lifeBar(self, surf, x, y, total):   # life : status / position
        if total < 0:
            total = 0
        bar_length = 100
        bar_height = 10
        fill = (total/100)*bar_length
        exteriorLifeRect = pygame.Rect(x, y, bar_length, bar_height)
        insideLifeRect = pygame.Rect(x, y, fill, bar_height)
        # life points (green)
        pygame.draw.rect(surf, self.green, insideLifeRect)
        # outer rectangle (whilte) ,life frame
        pygame.draw.rect(surf, self.white, exteriorLifeRect, 2)

    def start(self):
        self.game_play = True

        # we will use this class to add movement to the player
        self.speed = 4
        self.stop = 0
        self.xMove = 0
        self.yMove = 0

        while self.game_play:
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    self.game_play = False
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.player.knock()
                        breaks = Breaks(self.player.rect.x, self.player.rect.y)
                        self.allSprites.add(breaks)
                        self.broken.add(breaks)

            # check whether broken hit
            hits = pygame.sprite.groupcollide(self.broken, self.bottles, True, True)
            if hits:
                self.hitSound.play()
            for hit in hits:
                self.score += 1
                expl = Collision(hit.rect.center, 'playerHit',self.collisions_frame)
                self.breackBottles.add(expl)
                self.breackBottles.add(self.bottles)

            # here we see whether it will hit or not
            hits = pygame.sprite.spritecollide(self.player, self.enemies, True, pygame.sprite.collide_circle)
            for hit in hits:
                self.broomHit.play()  
                expl1 = Collision(hit.rect.center, 'playerHit',self.collisions_frame)
                self.allSprites.add(expl1)
                brooms = Brooms()
                self.allSprites.add(brooms)
                self.enemies.add(brooms)
                self.player.shield -= 50

                if self.player.shield <= 0:
                    self.death_explosion = Collision(self.player.rect.center, 'player', self.collisions_frame)
                    self.allSprites.add(self.death_explosion)
                    self.player.hide()
                    self.player.player_lives -= 1
                    self.player.shield = 100

                if hits == False:
                    pygame.sprite.Group.clear()
                    hits = self.allSprites.empty()

            if self.player.player_lives == 0 and not self.death_explosion.alive():
                self.game_play = False

            self.screen.blit(self.background, (0, 0))
            self.text(self.screen, str(self.score),18, self.width_window/2, 10)
            self.lifeBar(self.screen, 5, 5, self.player.shield)
            self.lives(self.screen, self.width_window-100, 5,self.player.player_lives, self.playerImageLives)

            self.screen.blit(self.player.image, self.player.rect)
            self.allSprites.draw(self.screen)

            self.player.handle_event(event)
            self.allSprites.update()
            self.breackBottles.draw(self.screen)

            pygame.display.flip()
            self.clock.tick(20)
