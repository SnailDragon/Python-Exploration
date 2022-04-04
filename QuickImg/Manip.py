from PIL import Image, ImageOps, ImageColor

class Manip:

    def __init__(self):
        self.path = ""
        self.resultPath = ""

    def grayscale(self):
        with Image.open(self.path) as im:
            greyIm = ImageOps.grayscale(im)
            name, ext = self._namegen()
            self.resultPath = f"{name}grayscale{ext}"
            greyIm.save(self.resultPath)

    # def recolor(self, col):
    #     with Image.open(self.path) as im:
    #         HSVim = im.convert('HSV')
    #         data = HSVim.getdata()
    #         hue = col[0]
    #         sat = col[1]
    #         newData = []
    #         for pix in data:
    #             newData.append((hue,sat,pix[2]))
    #         HSVim.putdata(newData)
    #         name, ext = self._namegen()
    #         colhex = ImageColor.getcolor(col, '#rrggbb')
    #         self.resultPath = f"{name}{colhex}{ext}"
    #         HSVim.save(self.resultPath)

    def splitRGB(self):
        with Image.open(self.path) as im:
            im = im.convert('RGB')
            channels = im.split()
            chanNames = ["r","g","b"]
            for (chan, index) in zip(channels, range(3)):
                data = chan.getdata()
                newrdata = []
                for i in data:
                    newCol = [0,0,0]
                    newCol[index] = i
                    newrdata.append(tuple(newCol))
                full = chan.convert('RGB')
                full.putdata(newrdata)
                name, ext = self._namegen()
                self.resultPath = f"{name}{chanNames[index]}{ext}"
                full.save(self.resultPath)

    def splitBW(self):
        with Image.open(self.path) as im:
            im = im.convert('RGB')
            r, g, b = im.split()
            name, ext = self._namegen()
            r.save(f"{name}rbw{ext}")
            g.save(f"{name}gbw{ext}")
            self.resultPath = f"{name}bbw{ext}"
            b.save(self.resultPath)


    def showImage(self):
        with Image.open(self.path) as im:
            im.show()

    def showLastResult(self):
        try:
            with Image.open(self.resultPath) as im:
                im.show()
        except FileNotFoundError:
            print("Last result file not found using path: " + self.resultPath)

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
            name, ext = self._namegen()
            self.resultPath = f"{name}{w}x{h}{ext}"
            resizedIm.save(self.resultPath)

    def validPath(self):
        if(self.path == ""):
            print("No path")
            return False
        return True

    def help(self):
        print('''Possible command list - use "quit" to quit
grayscale : Outputs the image in grayscale
path      : Takes input to set image path. If none is given then it prints current path.
resize    : Resizes image.
show      : Opens the image.
showlast  : Opens the image at the path last output to.
split     : Splits the image into 3 images made from each RGB channel
splitbw   : Splits the image into 3 grayscale images made from each RGB channel 
        ''')
    
    def _namegen(self):
        ext = self.path[self.path.rindex("."):]
        if(self.path.find("/") != -1):
            name = self.path[self.path.rindex("/")+1:self.path.rindex(".")]
        else:
            name = self.path[:self.path.rindex(".")]
        return name, ext


    