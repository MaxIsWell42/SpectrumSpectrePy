import sys
import io
import os
from colorthief import ColorThief

fileName = "static/Peacock-1-650x425.jpg"

def colorDetect():
    # Give the package an image to analyze
    color_thief = ColorThief(fileName)
    # get the dominant color
    dominant_color = color_thief.get_color(quality=1)
    # build a color palette
    palette = color_thief.get_palette(color_count=6)
    print("Dominant color: \n{}\nPalette: \n{}".format(dominant_color, palette) )

