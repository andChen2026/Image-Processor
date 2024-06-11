from Images.Image import Image

class ImageProcessor:
    def __init__(self, PImage: Image) -> None: # Image to be processed
        self.image = PImage 
        self.L = len(self.image.getPixelList)
        