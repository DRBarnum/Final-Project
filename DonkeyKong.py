import ggame
from ggame import App, RectangleAsset, ImageAsset, Sprite, LineStyle, Color, Frame, CircleAsset, PolygonAsset

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
        black=Color(1, 0)
        Black=Color(0, 1)
        noline=LineStyle(1000, Black)
        bg_asset=RectangleAsset(width, height, noline, black)
        bg=Sprite(bg_asset, (0, 0))
        Wall((0,0))
        wall((0,0))
        wAll((0,0))
        waLl((0,0))
        ladder((600, 550))
        Ladder((300, 515))
        lAdder((350, 309))
        laDder((100, 348))
        ladDer((220, 150))
        laddEr((270, 150))
        laddeR((600, 150))
        
        

            
            
# THE WALLS
class Wall(Sprite):
    Red = Color(0xF44366, 1.0)
    noline = LineStyle(0, Red)
    asset = PolygonAsset([(0, 670), (0, 700), (700, 680), (700, 650)], noline, Red)
    
    
    def __init__(self, position):
        super().__init__(Wall.asset, position)
        self.vx = 0
        self.vy = 0
        self.vr = 0
        self.fxcenter = self.fycenter = 0
        
    
        
class wall(Sprite):
    Red = Color(0xF44366, 1.0)
    noline = LineStyle(0, Red) 
    Asset = PolygonAsset([(0, 480), (0, 510), (600, 580), (600, 550)], noline, Red) 

    
    def __init__(self, position):
        super().__init__(wall.Asset, position)
        self.vx = 0
        self.vy = 0
        self.vr = 0
        self.fxcenter = self.fycenter = 0
        
class wAll(Sprite):
    Red = Color(0xF44366, 1.0)
    noline = LineStyle(0, Red) 
    Asset = PolygonAsset([(100, 380), (100, 350), (700, 260), (700, 290)], noline, Red) 

    
    def __init__(self, position):
        super().__init__(wAll.Asset, position)
        self.vx = 0
        self.vy = 0
        self.vr = 0
        self.fxcenter = self.fycenter = 0
        
class waLl(Sprite):
    Red = Color(0xF44366, 1.0)
    noline = LineStyle(0, Red) 
    Asset = PolygonAsset([(0, 150), (0, 180), (600, 180), (600, 150)], noline, Red) 

    
    def __init__(self, position):
        super().__init__(waLl.Asset, position)
        self.vx = 0
        self.vy = 0
        self.vr = 0
        self.fxcenter = self.fycenter = 0

class ladder(Sprite):
    Blue = Color(0x558b24, 1.0)
    noline = LineStyle(0, Blue)
    Asset = RectangleAsset(10, 105, noline, Blue)
    
    def __init__(self, position):
        super().__init__(ladder.Asset, position)
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
    Asset = RectangleAsset(10, 145, noline, Blue)
    
    def __init__(self, position):
        super().__init__(laDder.Asset, position)
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
    brown = 
    

    
    
            

myapp = Kong(SCREEN_WIDTH, SCREEN_HEIGHT)
myapp.run()
