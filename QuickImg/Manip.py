from PIL import Image, ImageFilter, ImageChops

class Manip:

    def __init__(self):
        self.path = ""
        self.resultPath = ""

    def showImage(self):
        with Image.open(self.path) as im:
            im.show()

    def showLastResult(self):
        with Image.open(self.resultPath) as im:
            im.show()

    def resize(self, width, height):
        with Image.open(self.path) as im:
            if(height == -1):
                w = int(width)
                h = int(im.size[1] * (width/float(im.size[0])))
            elif(width == -1):
                w = int(im.size[0] * (height/float(im.size[1])))
                h = int(height)
            else:
                w = int(width)
                h = int(height)
            print(f"Creating new image with dimensions {w}x{h}")
            resizedIm = im.resize((w,h))
            ext = self.path[self.path.rindex("."):]
            if(self.path.find("/") != -1):
                name = self.path[self.path.rindex("/")+1:self.path.rindex(".")]
            else:
                name = self.path[:self.path.rindex(".")]
            self.resultPath = f"{name}{w}x{h}{ext}"
            resizedIm.save(self.resultPath)


    def validPath(self):
        if(self.path == ""):
            print("No path")
            return False
        return True

    def help(self):
        print('Possible command list - use "quit" to quit')
        print("path \t: Takes input to set image path. If none is given then it prints current path.")
        print("resize \t: Resizes image.")
        print("show \t: Opens the image.")


    