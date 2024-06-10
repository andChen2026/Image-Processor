# Image-Processor
### This program will be able to:
1. Perform Operations on different image types
2. Convert one image type to another
3. Compress/Decompress an image file
4. Redo/Undo operations performed on an image file
5. Allow the user to view/maintain a history via logs
### Skills:
1. Python programming language
2. Bit manipulation
3. Input/Output 
4. Image manipulation
5. Image processing
6. Data Structures: Stacks, Queues
7. Algorithms: Burrows-Wheeler 
### Files:
1. Image.py - A class representation of an image    
    - Different image extensions will be represented differently via metadata
    - A list will be used to represent the pixels making the image
    - The length and width of the list will be stored as two fields to allow for efficient retrieval
2. Pixel.py - A class representation of a pixel
    - 3 fields: R, G, and B
    - Each field will have a range from 0 to 255
    - mutators that allow modifications of a pixel field
3. ImageTools.py - A class to store the low level operations:
    - Compressor
    - Decompressor
    - Converter
4. ImageProcessor.py - A class to store the general operations:
    - augment(): Change the dimensions of the image
    - crop(): remove parts of the image
    - saturate(): saturate an image by a percentage
    - rotate(): rotate an image by a specified amount
    - insert(): another image on top of this one
    - cut(): cut a part of an image from another image
    - fill(): fill parts of an image with another color
    - reduce(): reduce the quality of an image
    - scale(): zoom into a certain portion of an image by a percentage
    - delete(): remove this image
    - create(): create a new image 
    - save(): save the image we created
    - invert(): invert an image
    - redo(): redo the last operation performed
    - undo(): undo the last operation performed
    - upload(): uploads this image to an SQL database
    - changePixel(): changes a pixel at x and y
5. Tester.py - A program to conduct tests on the ImageProcessor
### Upcoming Features (No particular order)
- Graphical User Interface 
- Stylus Support
- Database connection
- Remote Image Database
- Collaboration between users
- Addition of Plugins
- Real-time drawing competitions
