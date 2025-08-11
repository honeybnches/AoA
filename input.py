import pygame
def keysNow():return pygame.key.get_just_pressed()
def keysAll():return pygame.key.get_pressed()
class Input:
    def __init__(self):
        self.x=0
        self.y=0
        self.dX="w"
        self.dY="s"
        self.index0=1
        self.index1=1
    def update(self):
        #Movement Controls
        self.anim="idle"
        if keysNow()[pygame.K_MINUS]:
            self.index1-=1
            print("down")
        if keysNow()[pygame.K_EQUALS]:
            self.index1+=1
            print("up")
        if keysNow()[pygame.K_LEFTBRACKET]:
            self.index0-=1
            print("left")
        if keysNow()[pygame.K_RIGHTBRACKET]:
            self.index0+=1
            print("right")
        if keysAll()[pygame.K_DOWN] and keysNow()[pygame.K_RIGHT]:self.x+=0.05;self.y-=0.1;self.dX="e";self.dY="s";self.anim="run"
        if keysAll()[pygame.K_DOWN] and keysNow()[pygame.K_LEFT]:self.x+=0.05;self.y-=0.1;self.dX="w";self.dY="s";self.anim="run"
        elif keysAll()[pygame.K_DOWN]:self.y+=0.1;self.dY="s";self.anim="run"

        if keysAll()[pygame.K_LEFT] and keysNow()[pygame.K_UP]:self.y-=0.05;self.x-=0.1;self.dX="w";self.dY="n";self.anim="run"
        if keysAll()[pygame.K_LEFT] and keysNow()[pygame.K_DOWN]:self.y+=0.05;self.x-=0.1;self.dX="w";self.dY="s";self.anim="run"
        elif keysAll()[pygame.K_LEFT]:self.x-=0.1;self.dX="w";self.anim="run"

        if keysAll()[pygame.K_RIGHT] and keysNow()[pygame.K_UP]:self.y-=0.05;self.x+=0.1;self.dX="e";self.dY="n";self.anim="run"
        if keysAll()[pygame.K_RIGHT] and keysNow()[pygame.K_DOWN]:self.y+=0.05;self.x+=0.1;self.dX="e";self.dY="s";self.anim="run"
        elif keysAll()[pygame.K_RIGHT]:self.x+=0.1;self.dX="e";self.anim="run"

        if keysAll()[pygame.K_UP] and keysNow()[pygame.K_RIGHT]:self.x-=0.05;self.y+=0.1;self.dX="e";self.dY="n";self.anim="run"
        if keysAll()[pygame.K_UP] and keysNow()[pygame.K_LEFT]:self.x-=0.05;self.y+=0.1;self.dX="w";self.dY="n";self.anim="run"
        elif keysAll()[pygame.K_UP]:self.y-=0.1;self.dY="n";self.anim="run"
        return self.x/2,self.y/2,self.dX,self.dY,self.index0,self.index1,self.anim


