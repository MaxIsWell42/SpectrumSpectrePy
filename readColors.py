import sys
import io
import os
from colorthief import ColorThief
from urllib.request import urlopen


def colorDetect(image):
    # Read the URL into an image, future feature
    # fd = urlopen(image)
    # f = io.BytesIO(fd.read())
    
    f = "static/screenshot.png"

    # Give the package an image to analyze
    color_thief = ColorThief(f)
    # get the dominant color
    dominant_color = color_thief.get_color(quality=1)
    # build a color palette
    palette = color_thief.get_palette(color_count=6)
    print("Dominant color: \n{}\nPalette: \n{}".format(dominant_color, palette) )

