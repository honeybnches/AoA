import pygame
from os.path import join
from data.scripts.dictionary import cacheDict
tileCache={}

global font12,font36,font48,font6,font4,font8
pygame.font.init()
font6=pygame.font.Font(None, 6)
font8=pygame.font.Font(None, 8)
font4=pygame.font.Font(None, 4)
font12=pygame.font.Font(None, 12)
font36=pygame.font.Font(None, 36)
font48=pygame.font.Font(None, 48)
fontx=pygame.font.Font(None, 0)
def fileFont(file):return join("data\\media\\fonts",file)
    

class Text:
    def __init__(self,text,screen,row=None,size=None,color=None,wA=None,wB=None,hA=None,hB=None) -> None:
        self.text=text
        if wA==None:self.wA=1;
        else:self.wA=wA;
        if wB==None:self.wB=0;
        else:self.wB=wB;
        if hA==None:self.hA=1;
        else:self.hA=hA
        if hB==None:self.hB=0;
        else:self.hB=hB
        self.row=row
        self.screen=screen
        if size==None:self.size=12;self.font=font12
        else: self.size=size
        if self.size==12:self.font=font12
        elif self.size==6:self.font=font6
        elif self.size==4:self.font=font4
        elif self.size==8:self.font=font8
        elif self.size==36:self.font=font36
        elif self.size==48:self.font=font48
        
        if color != None:self.color=color
        else:self.color="white"
        self.AA=True
    def draw(self):
        text=self.font.render(self.text,antialias=self.AA,color=self.color)
        #ax+b=y
        if self.row!=None:self.screen.blit(text,text.get_rect(center=(int(text.width*self.wA+self.wB),int(self.row[0]*text.height*self.row[1]+self.hB))))
        else:self.screen.blit(text,text.get_rect(center=(int(text.width*self.wA+self.wB),int(text.height*self.hA+self.hB))))