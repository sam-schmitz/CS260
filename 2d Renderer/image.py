# image.py
#   Class for manipulation of simple raster images


import array

# needed for img.show()
import ppmview


class Image:

    r"""Simple raster image. Allows pixel-level access and saving
    and loading as PPM image files.

    Examples:
    >>> img = Image((320, 240))    # create a 320x240 image
    >>> img.size
    (320, 240)
    >>> img[200,200]  # get color at pixel (200,200)
    (0, 0, 0)
    >>> img[200, 100] = (255, 0, 0) # set pixel to bright red
    >>> img[200, 100]   # get color of the pixel back again
    (255, 0, 0)
    >>> img.save("reddot.ppm")    # save image to a ppm file
    >>> img = Image((2, 3))
    >>> img[0,0] = 148, 103, 82
    >>> img[1,2] = 13, 127, 255
    >>> img.getdata()  # dump image data in ppm format
    b'P6\n2 3\n255\n\x00\x00\x00\r\x7f\xff\x00\x00\x00\x00\x00\x00\x94gR\x00\x00\x00'
    >>> img.load("wartburg.ppm")  # load a ppm image
    >>> img.size
    (640, 470)
    >>> img[350, 220]
    (148, 103, 82)
    >>> img.clear((255,255,255))  # make image all white
    >>> img.save("blank.ppm")     # blank.ppm is 640x470 all white
    """

    def __init__(self, fileorsize):
        """Create an Image from ppm file or create blank Image of given size.
        fileorsize is either a string giving the path to a ppm file or
        a tuple (width, height)
        """

        if type(fileorsize) == str:
            self.load(fileorsize)
        else:
            width, height = fileorsize
            self.size = (width, height)
            self.pixels = array.array("B", [0 for i in range(3*width*height)])
        self.viewer = None

    def __setitem__(self, pos, rgb):
        """ Set the color of a pixel.
        pos in a pair (x, y) giving a pixel location where (0, 0) is
            the lower-left pixel
        rgb is a triple of ints in range(256) representing
            the intensity of red, green, and blue for this pixel.
        """
        pix = self._base_i(pos)
        try:
            self.pixels[pix], self.pixels[pix+1], self.pixels[pix+2] = rgb[0], rgb[1], rgb[2]
        except:
            pass

    def __getitem__(self, pos):
        """ Get the color of a pixel
        pos is a pair (x, y) giving the pixel location--origin in lower left
        returns a triple (red, green, blue) for pixel color.
        """
        pix = self._base_i(pos)
        return self.pixels[pix], self.pixels[pix+1], self.pixels[pix+2]

    def save(self, fname):
        """ Save image as ppm in file called fname """
        f = open(fname, "wb")
        f.write(b"P6 \n")
        size = str(self.size[0]) +" " + str(self.size[1]) + "\n"
        f.write(size.encode())
        f.write(b"255 \n")
        self.pixels.tofile(f)
        f.close()

    def getdata(self):
        """ Get image information as bytes in ppm format
        """
        s = str(self.size[0]) + " " + str(self.size[1])
        return b"P6\n" + s.encode() + b"\n255\n" + self.pixels.tobytes()

    def load(self, fname):
        """load raw PPM file from fname.
        Note 1: The width and height of the image will be adjusted
                to match what is found in the file.

        Note 2: This is not a general method for all PPM files, but
                works for most
        """
        self.file = open(fname, "rb")   #open the file
        self.file.readline()    #all pmms are p6
        size = self.file.readline().decode()    #grab the image size
        size = size.strip("\n")
        self.size = tuple(map(int, size.split()))
        self.file.readline()    #should always be 16bit color
        self.pixels = array.array("B", [])
        self.pixels.fromfile(self.file, self.size[0] * self.size[1] * 3)



    def clear(self, rgb):
        """ set every pixel in Image to rgb
        rgb is a triple: (R, G, B) where R, G, & B are 0-255.
        """
        for i in range(len(self.pixels.tolist()) // 3):
            self.__setitem__((i%self.size[0], i//self.size[0]), rgb)
            #self.pixels[i*3], self.pixels[(i*3)+1], self.pixels[(i*3)+2] = rgb[0], rgb[1], rgb[2]

    def show(self):
        """ display image using ppmview """
        if not (self.viewer and self.viewer.isalive()):
            self.viewer = ppmview.PPMViewer("PPM Image")
        self.viewer.show(self.getdata())

    def unshow(self):
        """ close viewing window """
        if self.viewer:
            self.viewer.close()
            self.viewer = None

    def _base_i(self, loc):
        px, py = loc
        return 3 * ((self.size[1] - 1 - py) * self.size[0] + px)

    def invert_color(self): #inverts the colors in the image
        for i in range(len(self.pixels.tolist()) // 3):
            pix = i * 3
            rgb = self.pixels[pix], self.pixels[pix+1], self.pixels[pix+2]
            rgb = (255 - rgb[0], 255 - rgb[1], 255 - rgb[2])
            self.pixels[pix], self.pixels[pix+1], self.pixels[pix+2] = rgb[0], rgb[1], rgb[2]

    def grayscale(self):    #turns the colors in the image to black and white
        for i in range(len(self.pixels) // 3):
            pix = i * 3
            rgb = self.pixels[pix], self.pixels[pix+1], self.pixels[pix+2]
            l = int(.299*rgb[0] + .589*rgb[1] + .114*rgb[2])
            self.pixels[pix], self.pixels[pix+1], self.pixels[pix+2] = l, l, l


if __name__ == '__main__':
    import doctest
    doctest.testmod()
