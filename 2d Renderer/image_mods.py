#image_mods.py
#By: Sam Schmitz
#applys the image filters from image.py

from image import Image

if __name__ == '__main__':
    wart = Image("wartburg.ppm")
    print("The default Image")
    wart.show()
    print("image being shown")
    input("press <Enter>")
    wart.unshow()
    print("The Inverted Image")
    wart.invert_color()
    wart.show()
    input("press <Enter>")
    wart.unshow()
    print("The Black ang White Image")
    wart.grayscale()
    wart.show()
    input("press <Enter>")
    wart.unshow()
