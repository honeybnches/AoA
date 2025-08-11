import pygame
from data.dictionary import cacheDict
from os.path import join
tileCache={}
def fileTile(file): return join("data\\media\\tiles",file+".png")
def cacheTile(hecks):
    if hecks not in tileCache:
        if hecks=="ZZ":tileCache[hecks]={"name":"None"}
        else:tileCache[hecks]={"name":pygame.image.load(fileTile(cacheDict("tiles")[hecks]["name"])).convert_alpha()}
    return tileCache[hecks]
class Tile:
    
    def __init__(self,tile:str,screen,x=1,a=1,c=0,y=1,b=1,d=0):
        self.screen = screen
        self.x=x
        self.y=y
        self.a=a
        self.b=b
        self.c=c
        self.d=d
        global font12,font36,font48,font6,font4,font8
        font6=pygame.font.Font(None, 6)
        font8=pygame.font.Font(None, 8)
        font4=pygame.font.Font(None, 4)
        font12=pygame.font.Font(None, 12)
        font36=pygame.font.Font(None, 36)
        font48=pygame.font.Font(None, 48)
        fontx=pygame.font.Font(None, 0)
        self.surface=cacheTile(tile)["name"]
        self.name=cacheDict("tiles")[tile]["name"]
        tile=self.surface
        if self.name=="None":
            self.mux=False
        else:self.mux=True
    def render(self):
        if self.mux:
            self.screen.blit(self.surface,self.surface.get_rect(center=(int(256*self.x+256*self.a+self.c),int(512*self.y+512*self.b+self.d))))

