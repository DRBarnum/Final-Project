import ggame
from ggame import App, RectangleAsset, ImageAsset, Sprite, LineStyle, Color, Frame, CircleAsset, PolygonAsset, TextAsset

SCREEN_WIDTH = 700
SCREEN_HEIGHT = 700

# Barrel
class Barrel(Sprite):
    brown = Color(0x996633, 1.0)
    Black = Color(1,0)
    yellow = Color(0xfdd835, 1.0)
    noline = LineStyle(1, Black)
    asset = CircleAsset(25, noline, brown)

    
    def __init__(self, position):
        super().__init__(Barrel.asset, position)
        self.vx = 0
        self.vy = 0
        self.vr = 0
        self.fxcenter = self.fycenter = 0

    
# THE WORLD
class Kong(App):
    
    def __init__(self, width, height):
        super().__init__(width, height)
        black = Color(0, 1)
        yellow = Color(0xffeb3b, 1.0)
        white = Color(0xfafafa, 1.0)
        liner = LineStyle(1, white)
        line = LineStyle(1, black)
        self.play = False
        self.x = 50
        self.y = 250
        self.ComicSans = True
        bg_asset=RectangleAsset(width, height, line, black)
        bg=Sprite(bg_asset, (0, 0))
        text = TextAsset("Press ENTER To Start", style='40pt Comic Sans MS', fill= Color(0xffeb3b, 1), width=700)
        self.prompt = Sprite(text,(self.x, self.y))
        Kong.listenKeyEvent("keydown", "enter", self.playing)
        #Kong.listenKeyEvent("keyup", "enter", self.sans)
        
    def sans(self,event):
        self.prompt.destroy()


    def playing(self, event):
        self.sans(0)
        self.play = True
        if self.play == True:
            player((50, 640))
            black=Color(1, 0)
            Black=Color(0, 1)
            Red = Color(0xF44366, 1.0)
            noline=LineStyle(1000, Black)
            oline= LineStyle(0, Red)
            Blue = Color(0x558b24, 1.0)
            Wall(PolygonAsset([(0, 670), (0, 700), (700, 680), (700, 650)], oline, Red))
            Wall(PolygonAsset([(0, 480), (0, 510), (600, 580), (600, 550)], oline, Red))
            Wall(PolygonAsset([(100, 380), (100, 350), (700, 260), (700, 290)], oline, Red))
            Wall(PolygonAsset([(0, 150), (0, 180), (600, 180), (600, 150)], oline, Red))
            ladder(RectangleAsset(10, 105, oline, Blue), (600, 550))
            ladder(RectangleAsset(10, 150, oline, Blue),(300, 515))
            ladder(RectangleAsset(10, 215, oline, Blue), (350, 309))
            ladder(RectangleAsset(10, 150, oline, Blue), (100, 348))
            ladder(RectangleAsset(10, 100, oline, Blue), (220, 150))
            ladder(RectangleAsset(10, 175, oline, Blue), (270, 150))
            ladder(RectangleAsset(10, 125, oline, Blue), (600, 150))

            
            
   
        
            

            
            
# THE WALLS
class Wall(Sprite):
    Red = Color(0xF44366, 1.0)
    noline = LineStyle(0, Red)

    
    def __init__(self, asset):
        super().__init__(asset, (0,0))
        self.vx = 0
        self.vy = 0
        self.vr = 0
        self.fxcenter = self.fycenter = 0
        
        
class ladder(Sprite):
    Blue = Color(0x558b24, 1.0)
    noline = LineStyle(0, Blue)
    
    def __init__(self, asset, position):
        super().__init__(asset, position)
        self.vx = 0
        self.vy = 0
        self.vr = 0
        self.fxcenter = self.fycenter = 0
        
class Ladder(Sprite):
    Blue = Color(0x558b24, 1.0)
    noline = LineStyle(0, Blue)
    Asset = RectangleAsset(10, 150, noline, Blue)
    
    def __init__(self, position):
        super().__init__(Ladder.Asset, position)
        self.vx = 0
        self.vy = 0
        self.vr = 0
        self.fxcenter = self.fycenter = 0
        
class lAdder(Sprite):
    Blue = Color(0x558b24, 1.0)
    noline = LineStyle(0, Blue)
    Asset = RectangleAsset(10, 213, noline, Blue)
    
    def __init__(self, position):
        super().__init__(lAdder.Asset, position)
        self.vx = 0
        self.vy = 0
        self.vr = 0
        self.fxcenter = self.fycenter = 0
        
        
class laDder(Sprite):
    Blue = Color(0x558b24, 1.0)
    noline = LineStyle(0, Blue)
    Asset = RectangleAsset(10, 145, noline, Blue)
    
    def __init__(self, position):
        super().__init__(laDder.Asset, position)
        self.vx = 0
        self.vy = 0
        self.vr = 0
        self.fxcenter = self.fycenter = 0
        
class ladDer(Sprite):
    Blue = Color(0x558b24, 1.0)
    noline = LineStyle(0, Blue)
    Asset = RectangleAsset(10, 70, noline, Blue)
    
    def __init__(self, position):
        super().__init__(ladDer.Asset, position)
        self.vx = 0
        self.vy = 0
        self.vr = 0
        self.fxcenter = self.fycenter = 0
        
class laddEr(Sprite):
    Blue = Color(0x558b24, 1.0)
    noline = LineStyle(0, Blue)
    Asset = RectangleAsset(10, 175, noline, Blue)
    
    def __init__(self, position):
        super().__init__(laddEr.Asset, position)
        self.vx = 0
        self.vy = 0
        self.vr = 0
        self.fxcenter = self.fycenter = 0
        
class laddeR(Sprite):
    Blue = Color(0x558b24, 1.0)
    noline = LineStyle(0, Blue)
    Asset = RectangleAsset(10, 124, noline, Blue)
    
    def __init__(self, position):
        super().__init__(laddeR.Asset, position)
        self.vx = 0
        self.vy = 0
        self.vr = 0
        self.fxcenter = self.fycenter = 0
        
class player(Sprite):
    purple = Color(0x9575cd, 1.0)
    white = Color(0xfafafa, 1.0)
    line= LineStyle(1, white)
    asset = RectangleAsset(25, 25, line, purple)

    def __init__(self, position):
        super().__init__(player.asset, position)
        self.vx = 0
        self.vy = 5
        self.vr = 0
        self.a = self.collidingWithSprites(Wall)
        self.fxcenter = self.fycenter = 0.25
        self.YourDad = True
        self.YourUncle = False
        self.You = False
        Kong.listenKeyEvent("keydown", "right arrow", self.MoveRIGHT)
        Kong.listenKeyEvent("keyup", "right arrow", self.MoveOff)
        Kong.listenKeyEvent("keydown", "left arrow", self.MoveLEFT)
        Kong.listenKeyEvent("keyup", "left arrow", self.MoveOff)
        Kong.listenKeyEvent("keydown", "up arrow", self.JumpOn)
        Kong.listenKeyEvent("keyup", "up arrow", self.JumpOff)
        Kong.listenKeyEvent("keydown", "right arrow", self.falling)
        Kong.listenKeyEvent("keydown", "left arrow", self.falling)
       

    def step(self):
        self.vy = self.vy + 1.25
        self.y += self.vy
        self.a = self.collidingWithSprites(Wall)
        if len(self.a) != 0:
            self.y -= self.vy
            self.vy = 0
            self.YourDad = False
        else:
            self.YourDad = True
        if self.You == True:
            self.vy = -30
            self.You = False
        if self.YourDad == True:
            self.YourUncle = True
        else:
            self.YourUncle = False
        self.x += self.vx
        self.a = self.collidingWithSprites(Wall)
        if len(self.a) != 0:
            self.x -= self.vx
            self.vx = 0
            self.YourDad = False
        else:
            self.YourDad = True

    def falling(self, event):
        if self.YourDad == True:
            self.vy = self.vy + 1 
    
    def MoveRIGHT(self, event):
        if len(self.a) == 0:
            self.YourDad = True
        if self.YourDad == False:
            self.vx = 5
        else:
            self.vx = 5
            self.vy = 5
    
    def MoveLEFT(self, event):
        if len(self.a) == 0:
            self.YourDad = True
        if self.YourDad == False:
            self.vx = -5
        else:
            self.vx = -5
            self.vy = 5
        
    def MoveOff(self, event):
        self.vx = 0
        self.vy = 5

    def JumpOn(self, event):
        if len(self.a) == 0:
            self.YourDad = True
        if self.YourUncle == False:
            if self.YourDad == True:
                self.vy = -15
        else:
            self.vy = 5

    def JumpOff(self, event):
        self. vy = self.vy + 1
        
            

myapp = Kong(SCREEN_WIDTH, SCREEN_HEIGHT)
myapp.run()
