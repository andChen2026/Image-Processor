from Images.Image import Image
from Images.Position import Position

class ImageProcessor:
    def __init__(self, PImage: Image) -> None: # Image to be processed
        self.image = PImage 
        self.L = len(self.image.getPixelList)
        
    def save(self, Name: str) -> Image: # Returns the image modified and saves it in current directory
        pass

    def remove(self) -> None: # Removes the current image
        pass

    def isEqual(self, Img1: Image, Img2: Image) -> bool: # Has the image been modified/touched?
        pass

    def reverse(self) -> None: # Reverse the current image
        pass

    def saturate(self, factor: float) -> None: # Saturate the current image by a factor
        pass

    def reduceQuality(self, factor: float) -> None: # Reduce the quality of the image by a factor
        pass

    def fill(self, pos: Position, color: str) -> None: # Perform flood fill
        pass

    def invert(self) -> None: # Invert each pixel
        pass

    def rotate(self, degrees: float) -> None:
        pass

    def insert(self, Other: Image, Pos: Position) -> None: # Inserts another image at a position
        pass

    def augment(self, width: int, length: int) -> None: # Stretch or squish an image in any directions
        pass

    def PittColors(self) -> None: # Give each Pixel a hue of Blue/Gold
        pass

    def crop(self, pos: Position) -> None: # Crops a certain part of the image
        pass

    def undo(self) -> None: # Undo the last move
        pass

    def redo(self) -> None: # Redo the last move
        pass

    def upload(self) -> None: # Upload this modified image to a database
        pass