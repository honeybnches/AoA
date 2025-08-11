import pygame
from os import listdir
from os.path import splitext,join
imgCache={}

def fileImgDir(folder,sprite): return join("sprites",folder,sprite)
def fileImg(folder,sprite,file): return join("sprites",folder,sprite,file+".png")

def cacheImg(folder,sprite):
    if sprite not in imgCache:
        imgCache[sprite]={"zoom":4}
        for file in listdir(fileImgDir(folder,sprite)):
            file=splitext(file)[0]
            naming=file.split("_")
            if naming[0] not in imgCache[sprite]: imgCache[sprite][naming[0]]={}
            if len(naming)==3:
                
                if naming[1] in imgCache[sprite][naming[0]]:
                    imgCache[sprite][naming[0]][naming[1]][naming[2]]=pygame.transform.scale_by(pygame.image.load(fileImg(folder,sprite,file)).convert_alpha(),imgCache[sprite]["zoom"])
                    if naming[1] in ["ld","lu"]:imgCache[sprite][naming[0]]["r"+naming[1][-1]][naming[2]]= pygame.transform.flip(pygame.transform.scale_by(pygame.image.load(fileImg(folder,sprite,file)).convert_alpha(),imgCache[sprite]["zoom"]), True, False)
                   
                elif imgCache[sprite][naming[0]]!={} and naming[1] not in imgCache[sprite][naming[0]]:
                    imgCache[sprite][naming[0]][naming[1]]={
                                                        naming[2]:pygame.transform.scale_by(pygame.image.load(fileImg(folder,sprite,file)).convert_alpha(),imgCache[sprite]["zoom"])
                                                        }
                    if naming[1] in ["ld","lu"]:imgCache[sprite][naming[0]]["r"+naming[1][-1]]={
                                                        naming[2]:pygame.transform.flip(pygame.transform.scale_by(pygame.image.load(fileImg(folder,sprite,file)).convert_alpha(),imgCache[sprite]["zoom"]), True, False)
                                                        }
                else:
                    imgCache[sprite][naming[0]]={
                                                    naming[1]:{
                                                        naming[2]:pygame.transform.scale_by(pygame.image.load(fileImg(folder,sprite,file)).convert_alpha(),imgCache[sprite]["zoom"])
                                                        }
                                                 }
                    if naming[1] in ["ld","lu"]:imgCache[sprite][naming[0]]={
                                                    "r"+naming[1][-1]:{
                                                        naming[2]:pygame.transform.flip(pygame.transform.scale_by(pygame.image.load(fileImg(folder,sprite,file)).convert_alpha(),imgCache[sprite]["zoom"]), True, False)
                                                        }
                                                 }
            elif len(naming)==2:
                if "sprites" in imgCache[sprite][naming[0]]:
                    imgCache[sprite][naming[0]]["sprites"][naming[1]]=pygame.transform.scale_by(pygame.image.load(fileImg(folder,sprite,file)).convert_alpha(),imgCache[sprite]["zoom"])
                else:imgCache[sprite][naming[0]]={
                                                    "sprites":{
                                                        naming[1]:pygame.transform.scale_by(pygame.image.load(fileImg(folder,sprite,file)).convert_alpha(),imgCache[sprite]["zoom"])
                                                        }

                                             }
            elif len(naming)==1:imgCache[sprite][naming[0]]=pygame.transform.scale_by(pygame.image.load(fileImg(folder,sprite,file)).convert_alpha(),imgCache[sprite]["zoom"])


    return imgCache[sprite]

class Img:
    
    def __init__(self,folder,image:str,screen,bg=False,wA=None,wB=None,hA=None,hB=None):
        
        if wA==None:self.wA=1;
        else:self.wA=wA;
        if wB==None:self.wB=0;
        else:self.wB=wB;
        if hA==None:self.hA=1;
        else:self.hA=hA
        if hB==None:self.hB=0;
        else:self.hB=hB
        self.screen = screen
        self.name=image
        self.image=cacheImg(folder,image)
        image=self.image
        self.x=0
        self.y=0
        self.h=image.height
        self.w=image.width
        self.rect=pygame.Rect(self.x,self.y,self.w,self.h)
    def render(self):
            self.screen.blit(self.image,self.image.get_rect(center=(int(self.image.width*self.wA+self.wB),int(self.image.height*self.hA+self.hB))))
