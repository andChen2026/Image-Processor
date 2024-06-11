from Images.Position import Position

class Pixel:
    def __init__(self, RGBList: list, pos: Position) -> None:
        self.c = [color for color in RGBList] # create new list
        pass
        
    def setRGB(self, cList: list) -> None:
        self.c = [color for color in list] # overwrite previous values
        
    def getRGB(self) -> tuple:
        return tuple(self.c) # Return an immutable tuple copy of the list
        
