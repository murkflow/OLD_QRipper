from PIL import Image as img
import re

qr = img.open('1.png')
pix = qr.load()
w, h = qr.size
redxy = []

# Select all red pixels (missing data)
def grabber():
    x = 0
    y = 0
    while y < 29:
        while x < 29:
            r,g,b,p = pix[x,y]
            if r==255 and g==0:
                redxy.append((x,y))
            x+=1
        x=0
        y+=1
grabber()

# Didn't finish the rest.

qr.save("result.png", format="png")
