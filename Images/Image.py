from Images.Pixel import Pixel
from Images.Position import Position

class Image:
    def __init__(self, fileName: str) -> None: # Load in bytearray representing image
        self.pixelList = []; i = 0

        # Metadata for Image
        self.length: int = 0
        self.width: int = 0
        self.type: str = ""

        pList: list = []
        for byte in open(fileName, "r"):
            pList.append(byte)
            if i % 3 == 0:
                self.pixelList.insert(Pixel(pList, Position(i//3)))
            i+=1
        # Every image has a length and width, need to do some research on those

    def getPixelList(self) -> list:
        return self.pixelList
        