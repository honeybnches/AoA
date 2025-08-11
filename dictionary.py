import json,pygame,time
from re import S
from os.path import join,exists,splitext
from os import makedirs,listdir
from pygame import key,mouse
dictCache={}

class Settings:
    
    def __init__(self):
        settings=cacheDict("settings")
        gfx=settings["graphics"]
        sfx=settings["audio"]
        dbg=settings["debug"]
        self.vsync=False
        self.vulkan=False
        self.screenWidth=gfx["screenWidth"]
        self.screenHeight=gfx["screenHeight"]
        self.fullscreen=True
        self.debug=False
        self.bench=False
        if gfx["fullscreen"] == "False":
            self.fullscreen=False
        self.opengl=True
        if gfx["vulkan"]=="True":self.vulkan=True;self.opengl=False
        self.borderless=True
        if gfx["borderless"]=="False":self.borderless=False
        self.resizable=True
        if gfx["resizable"]=="False":self.resizable=False
        if gfx["vsync"]=="True":self.vsync=False
        self.zoom=gfx["zoom"]
        self.fps=gfx["fps"]
        self.aps=gfx["aps"]
        if dbg["console"]=="True":self.debug=True
        if dbg["benchmark"]=="True":self.bench=True

class Inputs:
    def __init__(self,debug):
        inp=cacheDict("input")
        self.keys=inp["keyboard"]
        self.mouse=inp["mouse"]
        self.debug=debug
        mouse_name_to_button = {
        #1,  # left click
        #2,  # middle click
        #3,  # right click
        #4,  # scroll up
        #5   # scroll down
        }

    def kState(self,bttn):
        # 0 open, 1 pressed, 2 released, 3 held
        state=0
        #print(key.get_just_pressed())
        #print(key.key_code(self.keys[bttn]))
        if key.get_just_pressed()[key.key_code(self.keys[bttn])]:state+=1
        if key.get_pressed()[key.key_code(self.keys[bttn])]:state+=2
        elif state==1 and key.get_just_pressed()[key.key_code(self.keys[bttn])]:state+=1
        
        if self.debug: print(str(bttn)+":"+str(state))
        #debug
        return state

    def mState(self,bttn):
        # 0 open, 1 pressed, 2 released, 3 held
        if bttn.startswith("mouse"):bttn=int(bttn.removeprefix("mouse"))
        if bttn.startswith("m"):bttn=int(bttn.removeprefix("m"))
        state=0
        if mouse.get_just_pressed()[bttn]:down=True;state+=1
        if mouse.get_pressed()[bttn]:state+=2
        elif state==1 and mouse.get_just_released()[bttn]:state+=1
        
        #debug
        if self.debug: print(str(bttn)+":"+str(state))
        return state

def fileDict(file):
        return join("data\\config",file)

def cacheDict(file):
    if file not in dictCache:
        dictCache[file]=json.load(open(fileDict(file),"r+"))
    return dictCache[file]
def crashDict(file):
    if file in dictCache and exists(fileDict(file)) and dictCache[file] != cacheDict(file):
       
       json.dump(dictCache[file],open(fileDict(file),mode="w+"),indent=4)