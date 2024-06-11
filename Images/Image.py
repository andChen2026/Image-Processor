from Images.Pixel import Pixel
from Images.Position import Position
class Image:
    def __init__(self, fileName: str) -> None:
        self.bitStream = [byte for byte in open(str, "r")] # Get a contiguous byteArray
        self.pixelList = []

        i = 0
        pList: list = []
        for byte in self.bitStream:
            pList.append(byte)
            if i % 3 != 0:
                self.pixelList.insert(Pixel(pList, Position(i)))
            i+=1