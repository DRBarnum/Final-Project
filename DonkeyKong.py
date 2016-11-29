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
        Barrel((100,100))
        

            
            
# THE WALLS
class Wall(Sprite):
    Red = Color(0xF44366, 1.0)
    noline = LineStyle(0, Red)
    asset = PolygonAsset([(0, 700), (0, 600), (700, 400), (700, 600)], noline, Red)
    
    def __init__(self, position):
        super().__init__(Wall.asset, position)
        self.vx = 0
        self.vy = 0
        self.vr = 0
        self.fxcenter = self.fycenter = 0
       

    
        

    
            

myapp = Kong(SCREEN_WIDTH, SCREEN_HEIGHT)
myapp.run()
