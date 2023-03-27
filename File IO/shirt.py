#In a file called shirt.py, implement a program that expects exactly two command-line arguments:

#in sys.argv[1], the name (or path) of a JPEG or PNG to read (i.e., open) as input
#in sys.argv[2], the name (or path) of a JPEG or PNG to write (i.e., save) as output
#The program should then overlay shirt.png (which has a transparent background) on the input after resizing and cropping
# the input to be the same size, saving the result as its output.

#Open the input with Image.open, per pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.open, resize and crop
# the input with ImageOps.fit, per pillow.readthedocs.io/en/stable/reference/ImageOps.html#PIL.ImageOps.fit, using default
# values for method, bleed, and centering, overlay the shirt with Image.paste,
# per pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.Image.paste, and save the result with Image.save,
# per pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.Image.save.

#The program should instead exit via sys.exit:

#if the user does not specify exactly two command-line arguments,
#if the input’s and output’s names do not end in .jpg, .jpeg, or .png, case-insensitively,
#if the input’s name does not have the same extension as the output’s name, or
#if the specified input does not exist.
#Assume that the input will be a photo of someone posing in just the right way, like these demos, so that,
#when they’re resized and cropped, the shirt appears to fit perfectly.

import sys

from PIL import Image

sys.argv[1].lower()
sys.argv[2].lower()
root1,ext1 = sys.argv[1].split(".")
root2,ext2 = sys.argv[2].split(".")

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")

elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")

elif ext1 != ext2:
    sys.exit("files with different extensions")

elif sys.argv[2].endswith(".png") or sys.argv[1].endswith(".jpeg") or sys.argv[1].endswith(".jpg"):
    try:
        shirt = Image.open("shirt.png")   # You can open an image (e.g., shirt.png) with code like:
        input = Image.open(sys.argv[1])
        size = shirt.size           #You can get the width and height, respectively, of that image as a tuple with code like:
        resized_input = input.resize(size)
        resized_input.paste(shirt, (0,0), mask = shirt)  #And you can overlay that image on top of another (e.g., photo) with code like
#wherein resized_input represents the image to overlay and shirt represents a “mask” indicating which pixels in photo to update.
        resized_input.save(sys.argv[2])
    except FileNotFoundError:
        sys.exit("File does not exist")
else:
    sys.exit("Incorrect file extension")