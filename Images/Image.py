from Images.Pixel import Pixel
from Images.Position import Position

class Image:
    def __init__(self, fileName: str) -> None: # Load in bytearray representing image
        self.pixelList = []; i = 0
        pList: list = []
        for byte in open(fileName, "r"):
            pList.append(byte)
            if i % 3 == 0:
                self.pixelList.insert(Pixel(pList, Position(i)))
            i+=1

    def getPixelList(self) -> list:
        return self.pixelList
        