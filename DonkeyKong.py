import ggame
from ggame import App, RectangleAsset, ImageAsset, Sprite, LineStyle, Color, Frame, CircleAsset

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800

# Barrel
class Barrel(Sprite):
    brown = Color(0x996633, 1.0)
    Black = Color(1,0)
    yellow = Color(0xfdd835, 1.0)
    noline = LineStyle(1, Black)
    asset = CircleAsset(50, noline, brown)
    rect = RectangleAsset(50, 50, noline, yellow)
    
    

    
# THE WORLD
class Kong(App):
    
    def __init__(self, width, height):
        super().__init__(width, height)
        black=Color(1, 0)
        Black=Color(0, 1)
        noline=LineStyle(1000, Black)
        bg_asset=RectangleAsset(width, height, noline, black)
        bg=Sprite(bg_asset, (0, 0))
    

myapp = Kong(SCREEN_WIDTH, SCREEN_HEIGHT)
myapp.run()