import PIL
from PIL import Image
from PIL import ImageEnhance
from IPython.display import display
import pandas as pd

# Could either add the jpegs to a list then interate through to paste them together;
# or dynamically name the jpegs, save them to a file, then paste them together.

jpegs = [] #List to hold transformed images
multipliers = [.1, .5, .9]

im = Image.open('headshotGit.jpeg')
im = im.convert('RGB')

#Ideally this would be refactored to a function to be less repetative
for i in range (3):

    # transform red channel
    if i == 0:
        for j in range (3):
            r, g, b = im.split()
            r = r.point(lambda q: q * multipliers[j])
            out = Image.merge('RGB', (r, g, b))
            out.show()
            jpegs.append(out)

    # transform green channel
    elif i == 1:
        for j in range (3):
            r, g, b = im.split()
            g = g.point(lambda q: q * multipliers[j])
            out = Image.merge('RGB', (r, g, b))
            out.show()
            jpegs.append(out)

    # transform blue channel
    elif i == 2:
        for j in range (3):
            r, g, b = im.split()
            b = b.point(lambda q: q * multipliers[j])
            out = Image.merge('RGB', (r, g, b))
            out.show()
            jpegs.append(out)

    
    # out.save("TransformedImage.jpg")

