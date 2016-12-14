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

# THE WALLS
class wall(Sprite):
    Red = Color(0xF44366, 1.0)
    noline = LineStyle(0, Red)

    
    def __init__(self, asset, position):
        super().__init__(asset, position)
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
        self.a = self.collidingWithSprites(wall)
        self.b = self.collidingWithSprites(ladder)
        self.fxcenter = self.fycenter = 0.25
        self.YourDad = True
        self.YourUncle = False
        self.You = False
        self.YourAunt = False
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
        self.a = self.collidingWithSprites(wall)
        self.b = self.collidingWithSprites(ladder)
        if len(self.b) != 0:
            self.You = True
        if len(self.b) == 0:
            self.You == False
        if len(self.a) != 0:
            self.y -= self.vy
            self.vy = 0
            self.YourDad = False
        else:
            self.YourDad = True
        if self.YourDad == True:
            self.YourUncle = True
        else:
            self.YourUncle = False
        self.x += self.vx
        self.a = self.collidingWithSprites(wall)
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
        if self.You == True:
            self.vy = -5
        if len(self.a) == 0:
            self.YourDad = True
        if self.YourUncle == False:
            if self.YourDad == True:
                self.vy = -18
        else:
            self.vy = 5

    def JumpOff(self, event):
        self. vy = self.vy + 1
        

    

class trophy(Sprite):
    yellow = Color(0xffca28, 1.0)
    white = Color(0xfafafa, 1.0)
    liner = LineStyle(1, white)
    
    def __init__(self, asset, position):
        super().__init__(asset, position)
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
        self.ComicSans = True
        bg_asset=RectangleAsset(width, height, line, black)
        bg=Sprite(bg_asset, (0, 0))
        text = TextAsset("Press ENTER To Start", style='40pt Comic Sans MS', fill= Color(0xffeb3b, 1), width=700)
        self.prompt = Sprite(text,(50, 250))
        Kong.listenKeyEvent("keydown", "enter", self.playing)

    def playing(self, event):
        self.prompt.destroy()
        self.play = True
        if self.play == True:
            player((50, 640))
            black=Color(1, 0)
            Black=Color(0, 1)
            Red = Color(0xF44366, 1.0)
            noline=LineStyle(1000, Black)
            oline= LineStyle(0, Red)
            white = Color(0xfafafa, 1.0)
            yellow = Color(0xffca28, 1.0)
            liner = LineStyle(1, white)
            Blue = Color(0x558b24, 1.0)
            wall(RectangleAsset(700, 30, oline, Red), (0, 670))
            wall(RectangleAsset(550, 30, oline, Red), (0, 500))
            wall(RectangleAsset(550, 30, oline, Red), (150, 330))
            wall(RectangleAsset(600, 30, oline, Red), (0, 160))
            wall(RectangleAsset(100, 30, oline, Red), (100, 50))
            ladder(RectangleAsset(10, 170, oline, Blue), (550, 500))
            ladder(RectangleAsset(10, 170, oline, Blue), (300, 500))
            ladder(RectangleAsset(10, 170, oline, Blue), (400, 330))
            ladder(RectangleAsset(10, 170, oline, Blue), (150, 330))
            ladder(RectangleAsset(10, 100, oline, Blue), (250, 160))
            ladder(RectangleAsset(10, 170, oline, Blue), (330, 160))
            ladder(RectangleAsset(10, 170, oline, Blue), (600, 160))
            ladder(RectangleAsset(10, 110, oline, Blue), (150, 50))
            trophy(RectangleAsset(25, 25, liner, yellow), (100, 25))
            
    def step(self):
        for ship in self.getSpritesbyClass(player):
            ship.step()

myapp = Kong(SCREEN_WIDTH, SCREEN_HEIGHT)
myapp.run()
