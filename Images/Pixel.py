from Images.Position import Position

class Pixel:
    def __init__(self, RGBList: list, pos: Position) -> None:
        self.colorList = [color for color in RGBList] # create new list
        self.pos = pos
        self.size = len(RGBList)*4 # size of the RGBList in Bytes
        
    def setRGB(self, cList: list) -> None:
        self.c = [color for color in cList] # overwrite previous values
        
    def getRGB(self) -> tuple:
        return tuple(self.c) # Return an immutable tuple copy of the list
        
