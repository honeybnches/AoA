
from re import S
import pygame,data.dictionary
from os import listdir
from os.path import isfile,join
from pygame import K_LEFT,K_RIGHT,K_DOWN,K_UP,K_LEFTBRACKET,K_RIGHTBRACKET
from random import randint
from data.sprite import Sprite
from data.image import cacheImg



mobs={
                    "cult1-1":{
                        "health":2,
                        "shield":1,
                        "buff":None,
                        "x":50,
                        "y":50,
                        "style":"aggWiz",
                        "dead":"no",
                        "dX":"l",
                        "dY":"d"
                        }
            }
char={
    "hlth":"1",
    "x":0,
    "y":0,
    "anim":"idle",
    "dX":"l",
    "dY":"d",
    "dead":"no",
    "w":32,
    "h":64}


class Poll:
    def init(self,screen,types,zoom):
        self.screen=screen
        items=[x for x in listdir(join("sprites",types)) if not isfile(x)]
        self.charIndex=0
        self.animIndex=0
        self.chars=items
        self.anims=[x.split("_")[0] for x in listdir(join("sprites",types,self.chars[self.charIndex])) if not isfile(x)]
        self.anim=self.anims[self.animIndex]
        self.sprite =Sprite(types,self.chars[self.charIndex],self.screen,0,screen.width/2,0,screen.height/2)
        self.width=32
        self.height=64
        self.types=types
        self.anim=self.anims[self.animIndex]
    def update(self,zoom):
        #ChangeOut sprites
        self.width=32*zoom
        self.height=64*zoom
        self.anim=self.anims[self.animIndex]
        
        self.sprite =Sprite(self.types,self.chars[self.charIndex],self.screen,char["x"],self.screen.width/2,char["y"],self.screen.height/2)
        #self.sprite.scaleIndex(self.char)
    def draw(self,tick,deltaTime):
        self.sprite.cycle(self.anim,char["dX"]+char["dY"],tick,deltaTime)




class GameLoop:
    def __init__(self,screen,zoom):
        self.screen=screen
        self.bg0=Sprite("wrld","arena",self.screen,0,self.screen.width/2,0,self.screen.height/2-90)
        self.bg1=Sprite("wrld","arena",self.screen,0,self.screen.width/2,0,self.screen.height/2)
        self.controller=mobController()
        self.poll=Poll()
        self.bg1.scale(4.20)
        self.bg0.scaleIndex("side1","sprites","0",3)
        self.controller.init(self.screen,mobs,char)
        self.poll.init(self.screen,"char",zoom)

    def tick(self,deltaTime):
        if (deltaTime%randint(1,5000)==0 or deltaTime%120000==0):
            None

    def update(self,tick,keys,keysAlt,zoom):
        self.controller.update(char)
        self.poll.update(zoom)


    def draw(self,tick,deltaTime):
        self.bg0.render("side1","sprites","0")
        self.bg1.render("ground1","sprites","0")
        self.poll.draw(tick,deltaTime)
        self.controller.draw(tick,deltaTime)

           
class mobController:

    def init(self,screen,mobs,player):
        self.screen=screen
        self.mobs=mobs
        self.player=player
        for mob in self.mobs:
            mob2=mob.split("-")[0]
            self.mobs[mob]["x"]=randint(0,screen.width)
            self.mobs[mob]["y"]=randint(0,screen.height)
            mobData=cacheImg("char",mob2)
            key=list(mobData.keys())[1]
            if type(mobData[key])==dict:
                key2=list(mobData[key].keys())[0]
                if type(mobData[key][key2])==dict:
                    key3=list(mobData[key][key2].keys())[0]
                    data=mobData[key][key2][key3]
                else:data=mobData[key][key2]
            else:
                data=mobData[key]
            self.mobs[mob]["width"]=data.width
            self.mobs[mob]["height"]=data.height
    def tick(self):None
    def update(self,player):
        self.player=player
        for mob in self.mobs:
            if self.mobs[mob]["style"]=="aggWiz":
                anim="idle"
                #enumerate player sectors
                p0=char["x"];p1=p0+char["w"];p2=char["y"]+char["h"];p3=char["y"]
                #enumerate mob sectors
                m0=self.mobs[mob]["x"];m1=m0+self.mobs[mob]["width"];m2=self.mobs[mob]["y"]+self.mobs[mob]["height"];m3=self.mobs[mob]["y"]
                for mob_ in self.mobs:
                    if mob_ != mob:
                        m_0=self.mobs[mob_]["x"];m_1=m0+self.mobs[mob_]["width"];
                        m_2=self.mobs[mob_]["y"]+self.mobs[mob_]["height"];m_3=self.mobs[mob_]["y"]
                        
                        if m0<m_1+10:self.mobs[mob_]["x"]+=2;self.mobs[mob_]["dX"]="l";anim="run"
                        if m1>m_0-10:self.mobs[mob_]["x"]-=2;self.mobs[mob_]["dX"]="r";anim="run"
                        if m3<m_2-10:self.mobs[mob_]["y"]+=2;self.mobs[mob_]["dY"]="u";anim="run"
                        if m2+10>m_3:self.mobs[mob_]["y"]-=2;self.mobs[mob_]["dY"]="d";anim="run"
                if m0>p1+50:self.mobs[mob]["x"]-=2;self.mobs[mob]["dX"]="l";anim="run"
                if m1<p0-50:self.mobs[mob]["x"]+=2;self.mobs[mob]["dX"]="r";anim="run"
                if m3>p2-50:self.mobs[mob]["y"]-=2;self.mobs[mob]["dY"]="u";anim="run"
                if m2+50<p3:self.mobs[mob]["y"]+=2;self.mobs[mob]["dY"]="d";anim="run"

            self.mobs[mob]["sprite"]=Sprite("chars",mob.split("-")[0],self.screen,0,self.mobs[mob]["x"],0,self.mobs[mob]["y"])
            self.mobs[mob]["sprite"].scale(4)
            self.mobs[mob]["anim"]=anim
            
    def spawn(self):
        moblin=list(mobs.keys())[-1]
        mob=moblin.split("-")
        count=int(mob[-1])+1
        if mob[0]+"-"+str(count) not in self.mobs:
            self.mobs[mob[0]+"-"+str(count)]=self.mobs[moblin]
            self.mobs[mob[0]+"-"+str(count)]["x"]=randint(0,self.screen.width)
            self.mobs[mob[0]+"-"+str(count)]["y"]=randint(0,self.screen.height)
    def draw(self,tick,deltaTime):

        for mob in self.mobs:
            #self.mobs[mob]["sprite"].cycle(self.mobs[mob]["anim"],self.mobs[mob]["dX"]+self.mobs[mob]["dY"],tick,deltaTime)
            self.mobs[mob]["sprite"].render("idle","ld","1")