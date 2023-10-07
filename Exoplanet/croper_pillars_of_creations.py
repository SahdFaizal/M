from PIL import Image
import math
def crop(filename, number):
    im = Image.open(filename)
    w, h = im.size
    unit = w // math.sqrt(number)
    i = 0
    for n in range(round(math.sqrt(number))):
        for m in range(round(math.sqrt(number))):
            im1 = im.crop(((m*unit), n*unit, unit*(m+1), unit*(n+1)))
            im1.save(str(i) + ".png")
            i += 1
    
crop("Exoplanet.png", 238144)
