import pygame
import player
import base64
import json
#import StringIO
import gzip

pygame.init()

widthTiled = 0
heightTiled = 0
widthMap = 0
heightMap = 0


matrizMap = []
        
width_window = 1040
height_window = 704
        
screen = pygame.display.set_mode((width_window, height_window))
background = pygame.image.load('indoor.png')
pygame.display.set_caption("Executus time !")
clock = pygame.time.Clock()
player = player.Executus((width_window/10, height_window/10))


def load_map(level):
    
    global widthTiled, heightTiled, widthMap, heightMap
    
    f = open(background +".json","r")
    data = json.load(f)
    f.close()
    
    widthTiled = data["widthTiled"]
    heightTiled = data["heightTiled"]
    widthMap = data["widthMap"]
    heightMap = data["heightMap"]
    
    for item in data["layers"]:
        indoorMap = item["data"]
        
        
    #print indoorMap
    
    indoorMap = base64.decodestring(indoorMap)
    
    #print indoorMap
    
    string = gzip.zlib.decompress(indoorMap);
    
    #print string 
    
    exitNumbers = []
    
    for idx in xrange(0, len(string), 4):
        val = ord(str(string[idx])) | (ord(str(string[idx +1]))  << 8) | \
        (ord(str(string[idx + 2]))  << 16) | (ord(str(string[idx + 3])) << 24)
        exitNumbers.append(val)
        
    #print exitNumbers
    
    
    for i in range(0, len(exitNumbers), widthMap):
        matrizMap.append(exitNumbers[i:i+widthMap])
        
        
    for i in range(heightMap):
        print (matrizMap[i])
        
    return
    
def array_tileset(background):
    
    x = 0
    y = 0
    
    fileTiles = []
    
    for i in range(29):
        
        for j in range(27):
            file = cut(background,(x, y, 16, 16))
            fileTiles.append(file)
            x += 18
            
        x = 0
        y += 18
        
    return fileTiles

def cut(background, rectForm):
    rect = pygame.Rect(rectform)
    image = pygame.Surface(rect,size).convert()
    image.blit(background,(0, 0),rect)
    return image

    


load_map(background)

files = array_tileset(background)

while True:
    
    time = clock.tick(60)
    
    for i in range(heightMap):
        for j in range(widthMap[i][j]):
            nimum = matrizMap[i][j]
            tileImg = files[minum -1]
            tileImag = pygame.transform.scale(tileImg,(tileWidth*2, tileHeight*2))
            screen.blit(tileImg, (j*tileWidth*2, i*tileHeight* 2 + 100))
            
    pygame.display.update()

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
            

