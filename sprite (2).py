import pygame
import json,pygame,time
from re import S
from os.path import join,exists,splitext
from os import makedirs,listdir
spriteCache={}
sheetCache={}
from data.scripts.text import Text
from data.scripts.input import Input
from data.scripts.dictionary import cacheDict
from data.scripts.image import cacheImg
imgCache={}
def cacheSheet(folder,sheet):
    if sheet not in sheetCache:
        sheetCache[sheet]=pygame.image.load(join("sprites",folder,sheet,"Atlas.png")).convert_alpha()
    return sheetCache[sheet]
def cacheFairies(folder,sprite,scale):

    if folder not in spriteCache:spriteCache[folder]={}
    if sprite not in spriteCache[folder]:spriteCache[folder][sprite]={}
    sheetData=cacheDict("spriteMap")[folder][sprite]
    if spriteCache[folder][sprite]=={}:
        row=0
        for anim in sheetData["map"]:
            if sheetData[anim][-1]==4:
                
                ne=[]
                nw=[]
                se=[]
                sw=[]
                i=0
                while i<sheetData[anim][0]:
                    ne.append(fileFairy(cacheSheet(folder,sprite),i,row,sheetData["dims"],scale))
                    i+=1
                i=0
                row+=1
                while i<sheetData[anim][0]:
                    nw.append(fileFairy(cacheSheet(folder,sprite),i,row,sheetData["dims"],scale))
                    i+=1
                i=0
                row+=1
                while i<sheetData[anim][0]:
                    se.append(fileFairy(cacheSheet(folder,sprite),i,row,sheetData["dims"],scale))
                    i+=1
                i=0
                row+=1
                while i<sheetData[anim][0]:
                    sw.append(fileFairy(cacheSheet(folder,sprite),i,row,sheetData["dims"],scale))
                    i+=1
                row+=1
                
                spriteCache[folder][sprite][anim]={}
                spriteCache[folder][sprite][anim]["ne"]=ne
                spriteCache[folder][sprite][anim]["nw"]=nw
                spriteCache[folder][sprite][anim]["se"]=se
                spriteCache[folder][sprite][anim]["sw"]=sw
            elif sheetData[anim][-1]==2:
                se=[]
                sw=[]
                while i<sheetData[anim][0]:
                    se.append(fileFairy(cacheSheet(folder,sprite),i,row,sheetData["dims"],scale))
                    i+=1
                i=0
                row+=1
                while i<sheetData[anim][0]:
                    sw.append(fileFairy(cacheSheet(folder,sprite),i,row,sheetData["dims"],scale))
                    i+=1
                row+=1
                spriteCache[folder][sprite][anim]={}
                spriteCache[folder][sprite][anim]["se"]=se
                spriteCache[folder][sprite][anim]["sw"]=sw
    return spriteCache[folder][sprite]

def fileFairy(sheet,frame,row,dims, scale):
    dims=tuple(dims)
    image = pygame.Surface(dims,pygame.SRCALPHA)
    print(frame)
    print(row)
    rect=((frame * dims[0]), (row*dims[1]), dims[0], dims[1])
    image.blit(sheet, (0, 0),rect)
    image = pygame.transform.scale(image, (dims[0] * scale, dims[1] * scale))
    return image

class Fairy:
    
    def __init__(self,folder,sprite:str,screen,wA=None,wB=None,hA=None,hB=None,scale=4):
        
        if wA==None:self.wA=1;
        else:self.wA=wA;
        if wB==None:self.wB=0;
        else:self.wB=wB;
        if hA==None:self.hA=1;
        else:self.hA=hA
        if hB==None:self.hB=0;
        else:self.hB=hB
        
        self.folder=folder
        self.frame=0
        self.index0=0
        self.screen = screen
        self.sprite=sprite
        self.spriteMap=cacheFairies(folder,sprite,scale)
        self.anim="idle"
        self.dX="e"
        self.dY="s"
        self.slides=list(self.spriteMap[self.anim].keys())
        self.sheet=self.spriteMap[self.anim][self.dY+self.dX]
        self.anims=list(self.spriteMap.keys())
        self.input=Input()
    def scaleIndex(self,file,slide,index,zoom):

            self.sprt[file][slide][index]=pygame.transform.scale_by(self.sprt[file][slide][index],1/imgCache[self.name]["zoom"])
            self.sprt[file][slide][index]=pygame.transform.scale_by(self.sprt[file][slide][index],zoom)
    def poll(self,anim):
        return 
    def tick(self,tick):
        self.slides=list(self.spriteMap[self.anim].keys())
        
        if tick:self.index0+=1;print(self.index0);self.frame+=1
        if self.index0>=len(self.slides):self.index0=0
    def update(self):
            
            self.wB,self.hB,self.dX,self.dY,self.char0,self.anim0,self.anim=self.input.update()
            if self.anim0<=0:self.anim0=0
            self.anim=self.anims[self.anim0]
            self.slides=list(self.spriteMap[self.anim].keys())
            Text(str(self.anim),self.screen,None,48,"white",-1,self.screen.width,-1,self.screen.height).draw()
            if len(self.spriteMap[self.anim])==2:self.dY="s"
            self.image=self.spriteMap[self.anim][self.dY+self.dX][self.index0]
    
    def draw(self):
            self.screen.blit(self.image,self.image.get_rect(center=(int(self.image.width*self.wA+self.wB),int(self.image.height*self.hA+self.hB))))



class Sprite:
    
    def __init__(self,folder,image:str,screen,wA=None,wB=None,hA=None,hB=None):
        
        if wA==None:self.wA=1;
        else:self.wA=wA;
        if wB==None:self.wB=0;
        else:self.wB=wB;
        if hA==None:self.hA=1;
        else:self.hA=hA
        if hB==None:self.hB=0;
        else:self.hB=hB
        
        self.index0=0
        self.screen = screen
        self.name=image
        self.sprt=cacheImg(folder,image)
        self.frames=0
        self.frametime=0
    def scale(self,zoom):
        if self.sprt["zoom"]!=zoom:
            oldZoom=self.sprt["zoom"]
            del self.sprt["zoom"]
            for file in self.sprt:
                    if type(self.sprt[file])==dict:
                        for slide in self.sprt[file]:
                            if type(self.sprt[file][slide])== dict:
                                for frame in self.sprt[file][slide]:
                                    self.sprt[file][slide][frame]=pygame.transform.scale_by(self.sprt[file][slide][frame],1/oldZoom)
                            else:
                                self.sprt[file][slide]=pygame.transform.scale_by(self.sprt[file][slide],1/oldZoom)
                    else:
                        self.sprt[file]=pygame.transform.scale_by(self.sprt[file],1/oldZoom)

            for file in self.sprt:
                if type(self.sprt[file])==dict:
                    for slide in self.sprt[file]:
                        if type(self.sprt[file][slide])== dict:
                            for frame in self.sprt[file][slide]:
                                self.sprt[file][slide][frame]=pygame.transform.scale_by(self.sprt[file][slide][frame],zoom)
                        else:
                            self.sprt[file][slide]=pygame.transform.scale_by(self.sprt[file][slide],zoom)
                        
                else:
                    self.sprt[file]=pygame.transform.scale_by(self.sprt[file],zoom)
            
            imgCache[self.name]=self.sprt
            imgCache[self.name]["zoom"]=zoom


    def cycle(self,file,slide,tick,deltaTime):
            self.sprtSheet=self.sprt[file][slide]
            keys=list(self.sprtSheet.keys())
            if tick and self.index0<len(keys):
                self.index0+=1
                #print(self.index0)
            else:self.index0=0
            key=keys[self.index0]
            self.image=self.sprtSheet[key]
            self.screen.blit(self.image,self.image.get_rect(center=(int(self.image.width*self.wA+self.wB),int(self.image.height*self.hA+self.hB))))
            #Text(str(self.frametime),self.screen,None,48,"white",-(1/2),self.screen.width,(1/2),0).draw()

    def scaleIndex(self,file,slide,index,zoom):

            self.sprt[file][slide][index]=pygame.transform.scale_by(self.sprt[file][slide][index],1/imgCache[self.name]["zoom"])
            self.sprt[file][slide][index]=pygame.transform.scale_by(self.sprt[file][slide][index],zoom)

    def render(self,file,slide,index):
            if file==None and slide==None:self.image=self.sprt[index]
            elif file==None:self.image=self.sprt[slide][index]
            else:self.image=self.sprt[file][slide][index]
            self.h=self.image.height
            self.w=self.image.width
            self.screen.blit(self.image,self.image.get_rect(center=(int(self.image.width*self.wA+self.wB),int(self.image.height*self.hA+self.hB))))

class SpriteSheet:
    def __init__(self,tray,sprite,screen,wA=None,wB=None,hA=None,hB=None):
        
        if wA==None:self.wA=1;
        else:self.wA=wA;
        if wB==None:self.wB=0;
        else:self.wB=wB;
        if hA==None:self.hA=1;
        else:self.hA=hA
        if hB==None:self.hB=0;
        else:self.hB=hB
        sMap=cacheDict("spriteMap")

        def cycle(self,anim,tick,deltaTime):

            keys=list(self.sprtSheet.keys())
            if tick and self.index0<len(keys):
                self.index0+=1
                print(self.index0)
            else:self.index0=0
            key=keys[self.index0]
            self.image=self.sprtSheet[key]
            self.screen.blit(self.image,self.image.get_rect(center=(int(self.image.width*self.wA+self.wB),int(self.image.height*self.hA+self.hB))))
            Text(str(self.frametime),self.screen,None,48,"white",-(1/2),self.screen.width,(1/2),0).draw()

disp=0
def dumpSprites(screen):
        row=0;column=0
        global disp
        if pygame.key.get_pressed()[pygame.K_RIGHT]:disp+=3
        if pygame.key.get_pressed()[pygame.K_LEFT]:disp-=3

        for folder in spriteCache:
                        for sprite in spriteCache[folder]:
                            for anim in spriteCache[folder][sprite]:
                                
                                for direction in spriteCache[folder][sprite][anim]:
                                    for image in spriteCache[folder][sprite][anim][direction]:
                                            screen.blit(image,image.get_rect(center=(32+column*64,64+row*128+disp)))
                                            column+=1
                                    row+=1;column=0
                                row+=1;column=0