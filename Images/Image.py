from Images.Pixel import Pixel
from Images.Position import Position

class Image:
    def __init__(self, fileName: str) -> None: # Load in bytearray representing image
        self.pixelList = []; i = 0

        # Metadata for Image
        self.length: int = 0
        self.width: int = 0
        self.type: str = ""

        for byte in open(str, "r"):
            pass
        # Every image has a length and width, need to do some research on those

    def getPixelList(self) -> list:
        return self.pixelList
        